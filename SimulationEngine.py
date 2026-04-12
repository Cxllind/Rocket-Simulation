import numpy as np
from scipy import constants
from RocketLaunchControl import *

def Density(stateVector): #Calculates the density. Model only truly valid till about 10KM, but up to 100KM it is very rough as drag decreases rapidly
    h = stateVector[0]
    rowe0 = 1.225
    H = 8500
    
    density = rowe0 * np.exp(-h/H)
    return density

def Drag(stateVector):
    v = stateVector[1]
    Cd = 0.75 #average drag coefficient for a rocket
    A = 60 #approximate reference area for a rocket (like in NASA)
    p = Density(stateVector)
    drag = 0.5*p*A*Cd*np.square(v) * -sign(v)
    return drag

def g(stateVector): #Calculating the weight of the rocket using Newton's law of universal gravitation
    h = stateVector[0]
    g_Earth = (constants.G)*(5.97e24)/np.square(h + 6.37e6)
    return g_Earth

def dvdt(t, stateVector, Parameters):
    #Initialising values and calculating relevant ones
    h, v, mass, FuelMass, I = stateVector
    exhaustVelocity = Parameters[0]


    weight =  - mass * g(stateVector)
    drag = Drag(stateVector) #opposite direction to velocity
    Forces = weight + drag

    dmdt, error = PID(stateVector, Forces, Parameters)
    Thrust = - exhaustVelocity * dmdt
    Resultant = Thrust + drag 


    a = Resultant/ mass
    if h <= 0 and (a < 0 or v < 0): #Just making sure the thing doesn't fall out of bounds
        v, a = 0, 0

    return np.array([v, a, dmdt, dmdt, error])