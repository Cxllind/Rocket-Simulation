import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from SimulationEngine import *

mass = 300000 #starting mass including fuel
fuelMass = 0.8 * mass
stateVector = np.array([0, 0, mass, fuelMass, 0]) #[position, speed, mass, fuelMass errorIntegral]

exhaustVelocity = 3000
Peak = 100000 #Peak height is 100Km, or in space
dmdtMax = - 400
Parameters = [exhaustVelocity, Peak, dmdtMax]

mins = 10
RunTime = 60 * mins
frames = 60 * RunTime


results = solve_ivp(
    dvdt, 
    t_span = [0, RunTime], 
    t_eval = np.linspace(0, RunTime, frames), 
    y0 = stateVector,
    events = PeakEvent,
    args = (Parameters,)
)


#extracting the height, velocity and mass at specific times during the simulation
t = results.t
y, v, m, fuelM, Ierror = results.y
dvdh = np.gradient(v, y)
a = v * dvdh
error = np.gradient(Ierror, t)


#plots each graph in order
plt.xlabel('time/ s')
plt.ylabel('Altitude/ m')
plt.plot(t, y)
plt.show()


plt.xlabel('time/ s')
plt.ylabel('vertical Speed/ m/s')
plt.plot(t, v)
plt.show()

plt.xlabel('time/ s')
plt.ylabel('acceleration / m/s^2')
plt.plot(t, a)
plt.show()

plt.xlabel('time/ s')
plt.ylabel('Rocket Mass/ Kg')
plt.plot(t, m)
plt.show()

plt.xlabel('time/ s')
plt.ylabel('Fuel Mass/ Kg')
plt.plot(t, fuelM)
plt.show()

plt.xlabel('time/ s')
plt.ylabel('Velocity error/ m/s')
plt.plot(t, error)
plt.show()