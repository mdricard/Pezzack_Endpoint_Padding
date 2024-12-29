import numpy as np
import matplotlib.pyplot as plt
from BiomechTools import low_pass


npad = 40       # 20 points at start 20 points at end
# Read Pezzack
data = np.genfromtxt('d:/pezzack.csv', delimiter=',', skip_header=1)
x = data[:, 0]
y = data[:, 1]

dt = x[1] - x[0]
n = len(y)
#new_x = np.arange(0, (n + npad) * dt, dt)
new_x = np.zeros(n + npad)
k = 20
i = 0
while i < n:
    new_x[k] = x[i]
    i += 1
    k += 1
i = 19
iv = -dt
while i >= 0:
    new_x[i] = iv
    i -= 1
    iv -= dt
i = n
while i < (n + npad):
    new_x[i] = new_x[i-1] + dt
    i += 1


new_y = np.zeros(n + npad)
i = 0
j = int(npad / 2)
while i < n:
    new_y[j] = y[i]
    i += 1
    j += 1

minus_10 = n - 11
# Fit a 3rd order polynomial to the data
fit_first_10 = np.polyfit(x[0:9], y[0:9], 3)
fit_last_10 = np.polyfit(x[minus_10: n-1], y[minus_10: n-1], 3)
new_y[0:20] = np.polyval(fit_first_10, new_x[0:20])
new_y[len(new_x)-20:len(new_x)] = np.polyval(fit_last_10, new_x[len(new_x)-20:len(new_x)])
sm_y = low_pass(new_y, 1/dt, 4.0)
plt.plot(new_x, new_y, 'b', label='Original padded 20 pts')
plt.plot(new_x, sm_y, 'r', label='Smoothed padded')
plt.plot( x, y, 'o', label='Original data')
plt.legend()
plt.show()

vel = np.zeros(n + npad)
accel = np.zeros(n + npad)
for i in range(1, (n + npad) - 1):
    vel[i] = (sm_y[i+1] - sm_y[i-1]) / (2 * dt)
vel[0] = (sm_y[1] - sm_y[0]) / dt
vel[n + npad - 1] = (sm_y[n + npad - 1] - sm_y[n + npad - 2]) / dt
plt.plot(vel)
plt.show()

for i in range(2, (n + npad) - 2):
    accel[i] = (vel[i+1] - vel[i-1]) / (2 * dt)
accel[0] = accel[2]
accel[1] = accel[2]
accel[n + npad - 2] = accel[n + npad - 3]
accel[n + npad - 1] = accel[n + npad - 3]

plt.plot(accel)
plt.vlines(20, -20.0, 60, 'r', 'dotted')
plt.vlines(n + 20, -20.0, 60, 'r', 'dotted')
plt.show()

# Plot the data and the fitted polynomial
plt.plot(x, y, 'o', label='data')
plt.plot(new_x[0:19], np.polyval(fit_first_10, new_x[0:19]), '-', label='First 10 fitted polynomial')
plt.plot(new_x[len(new_x)-20:len(new_x)], np.polyval(fit_last_10, new_x[len(new_x)-20:len(new_x)]), '-', label='Last 10 fitted polynomial')
plt.legend()
plt.show()
