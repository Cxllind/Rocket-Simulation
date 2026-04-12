import numpy as np

def PeakEvent(t, stateVector, Parameters): #Event that returns whether or not the rocket has reached the max height
    Peak = Parameters[1]
    h = stateVector[0]
    return Peak - h
PeakEvent.terminal = False

def sign(x): #Calculates the sign of something, particularly useful when dealing with drag as it opposes velocity
    if x >= 0:
        return 1
    return -1

def TargetV(stateVector, Peak): #Function that callculates v(h), the target vertical velocity as a function of height
    h = stateVector[0]
    if h < Peak:
        return (-5.01e-12)*(h**3) + (2.51e-07)*(h**2) + (9.99e-2)*(h) + 5.00 #this is the target vertical velocity function generated from scipy.optimise
    return 7500

def PID(stateVector, Forces, Parameters):
    x, v, mass, FuelMass, I = stateVector
    exhaustVelocity, Peak, dmdtMax = Parameters

    noise = abs(0.05 * v)
    target =  TargetV(stateVector, Peak)
    error = target - v + np.random.uniform(-noise, noise)

    #hand tuned PID gains, edit so t
    kP = 2.25
    kI = 0.05
    kD = 0

    #Gives the calculated thrust and throttle outputted without the D term in the PID controller
    rawThrottle = kP*(error) + kI*(I)
    rawThrust = - rawThrottle*(exhaustVelocity * dmdtMax)
    rawAcceleration = (rawThrust + Forces)/ mass

    #After calculating raw values and the acceleration, we add the D term and bound the throttle between 1 and 0
    dedt = -rawAcceleration
    targetThrottle = rawThrust + kD*(dedt)
    targetThrottle = np.clip(targetThrottle, 0, 1.0)


    dmdt = targetThrottle * dmdtMax
    dmdt = np.clip(dmdt, dmdtMax, 0) #mass flow rate
    if FuelMass <= 0:
        dmdt = 0

    return dmdt, error