import matplotlib.pyplot as plt
from matplotlib import ticker

x_values = list(range(1, 400))
y_values = [x ** 2 for x in x_values]

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
            edgecolor='none', s=40)
plt.axis([0, 500, 0, 200000])
plt.savefig('first_plot.png', bbox_inches='tight')
plt.show()
