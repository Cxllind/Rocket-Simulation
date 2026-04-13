🚀 Rocket Ascent Simulation with PID‑Based Thrust Control
A physics‑driven simulation of a vertically ascending rocket using nonlinear dynamics, atmospheric drag, variable mass, and a PID controller tracking a target velocity‑vs‑altitude curve. The project includes trajectory optimisation, noise modelling, and full numerical integration using SciPy.


Full nonlinear rocket dynamics:
- Variable mass from fuel burn
- Thrust from mass‑flow rate and exhaust velocity
- Gravity varying with altitude
- Exponential atmospheric density model
- Quadratic drag force

Closed‑loop control:
- PID controller regulating velocity as a function of altitude
- Noise‑corrupted sensor inputs
- Throttle saturation and mass‑flow limits
- Integral error tracking

Trajectory optimisation:
- Cubic velocity‑vs‑height curve generated using differential evolution
- Custom scoring function to shape ascent profile

Simulation engine:
- Numerical integration with solve_ivp
- Event detection for peak altitude
- High‑resolution time sampling

Visualisation:
- Plots of altitude, velocity, acceleration, mass, fuel, and control error
