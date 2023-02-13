import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.use("TkAgg")

import classes

system = classes.Solar_System()
system.add_body(pos=(-8,0), vel=(0.1,1.5))
system.add_body(pos=(8,0), vel=(0,-1.5))

iterations = 1000

for i in range(iterations):
    system.update_bodies()

fig = plt.figure(figsize=(5,4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-system.size[0], system.size[0]), ylim=(-system.size[1], system.size[1]))
ax.set_aspect('equal')
ax.grid()

points = []
for i in system.contents:
    point, = ax.plot([],[],'x')
    points.append(point)

def animate(i):
    for idx, body in enumerate(system.contents):
        points[idx].set_data(body.positions[i][0], body.positions[i][1])
    
    return points

ani = animation.FuncAnimation(
    fig, animate, iterations, interval=0.1, blit=True)

plt.show()

# for body in system.contents:
#     body.positions = np.array(body.positions)
#     ax.plot(body.positions[:,0], body.positions[:,1], 'o')

# plt.show()