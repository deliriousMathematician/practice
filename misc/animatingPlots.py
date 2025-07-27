import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0, 25, 0.1)
y = np.sin(x)

# line plot
sin = ax.plot(x[0], y[0], label=r'$y=\sin{x}$')[0]
ax.set(xlim=[0,30], ylim=[-1.5,1.5], xlabel='x', ylabel='y')
ax.legend()

def update(frame):
    sin.set(xdata=x[:frame], ydata=y[:frame])
    return sin

## scatter plot
# sin = ax.scatter(x[0], y[0])
# ax.set(xlim=[0,30], ylim=[-1.5,1.5], xlabel='x', ylabel='y')

# def update(frame):
#     data = np.stack([x[frame], y[frame]]).T
#     sin.set_offsets(data)
#     return sin

ani = ani.FuncAnimation(fig=fig, func=update, frames=250, interval=10)
plt.show()
