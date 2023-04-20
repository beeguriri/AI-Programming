import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return 8 * (x - 10) * np.sin(0.5 * x - 5) + 200

def fd(x):
    return 4 * (x - 10) * np.cos(0.5 * x - 5) + 8 * np.sin(0.5 * x - 5)

x_min = -30
x_max = 30
x = np.linspace(x_min, x_max, 200)
y = f(x)
r = 0.01 # learning rate
x_est = 25 # starting point
y_est = f(x_est)

# i : interval
def animate(i):
    global x_est
    global y_est

    x_est = x_est - fd(x_est) * r
    y_est  = f(x_est)

    scat.set_offsets([[x_est, y_est]])
    text.set_text(f"Value : {y_est}")
    line.set_data(x, y)
    return line, scat, text


def init():
    line.set_data([],[])
    return (line,)


fig, ax = plt.subplots()
ax.set_xlim([x_min, x_max])
ax.set_ylim([-5, 500])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
(line, ) = ax.plot([], [])
scat = ax.scatter([], [], c='red')
text = ax.text(-25,450,"")

ani = animation.FuncAnimation(fig, animate, 30,
                              init_func=init, interval=100,
                              blit=True)
plt.show()

# Matplotlib
# - plt. (한개)
# - subplots (여러개)
# - subplot2grid (여러개)
