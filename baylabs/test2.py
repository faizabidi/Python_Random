import matplotlib.pyplot as plt

xs = [1,2]
ys = [0,1]

ax = plt.subplot(aspect='equal')
ax.plot(xs, ys, '-')
ax.set_xlim(0,5)
ax.set_ylim(0,5)

plt.show()