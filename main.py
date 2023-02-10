import numpy as np
import matplotlib.pyplot as plt

import classes

system = classes.Solar_System()
system.add_body(pos=(-8,0))
system.add_body(pos=(8,0))

for body in system.contents:
    print(body.pos)

fig = plt.figure(figsize=(5,4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-system.size[0], system.size[0]), ylim=(-system.size[1], system.size[1]))
ax.set_aspect('equal')
ax.grid()

for body in system.contents:
    ax.plot(body.pos, 'o')

fig.show()

system.update_bodies()

for body in system.contents:
    ax.plot(body.pos, 'o')

fig.show()

done = input("done")