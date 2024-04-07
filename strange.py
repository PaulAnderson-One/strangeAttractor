from scipy.integrate import solve_ivp
import math
import numpy as np
import matplotlib.pyplot as plt

def duff(t, state, d, a, b, g, w):
    (x,y)=state
    dydt = [y,  -a * x - b * x * x * x - d*y +g * math.cos(w * t)]
    return dydt

def pend(t, state,s,b,r):
    # theta, omega = y
    # dydt = [omega, -b*omega - c*np.sin(theta)]
    # return dydt
    (x,y,z)=state
    # dydt= [y - x, r * x - y−x*z,  x*y − b*z]
    dydt = [s*(y - x),  x*(r-z) - y, x * y - b * z]
    return dydt

y0 = [1.0,1.0,1.0]

sigma = 10.0
beta = 8.0 / 5.0
rho = 28.0
p=(sigma,beta,rho)
# t = np.linspace(0, 10, 101, args=p)

from scipy.integrate import odeint
# result_solve_ivp = solve_ivp(pend,(0.0,40),y0, args=p,method='LSODA', t_eval=t)

y0 = [1.0, 1.0]

d = 0.02
a = 1
b = 5
g = 8
w = 0.5
p=(d,a,b,g,w)

M=2000
tmin=0
period = 2*math.pi/w
tmax=M*period
dt = tmax/M
nn = int(period/dt)
t = np.arange(tmin, tmax, dt)
for i in t:
    print(math.sin(i))
result_solve_ivp = solve_ivp(duff,(tmin,tmax),y0, args=p,method='LSODA', t_eval=t)

fig = plt.figure()
# ax = fig.add_subplot(1, 2, 1, projection='3d')
# ax.plot(result_solve_ivp[:, 0],
#         result_solve_ivp[:, 1],
#         result_solve_ivp[:, 2])
# ax.set_title("odeint")

if 1==1:
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(result_solve_ivp.y[0, 0::], result_solve_ivp.y[1, 0::], marker=".", linewidths=0)

    # ax.plot(result_solve_ivp.y[0, :], result_solve_ivp.y[1, :])
    ax.set_title("solve_ivp")

    plt.show()

if 1==2:
    ax = fig.add_subplot(1, 1,1, projection='3d')
    ax.plot(result_solve_ivp.y[0, :],
            result_solve_ivp.y[1, :],
            result_solve_ivp.y[2, :])
    ax.set_title("solve_ivp")

    plt.show()