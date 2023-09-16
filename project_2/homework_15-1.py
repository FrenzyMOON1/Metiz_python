import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [i ** 3 for i in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20)
plt.show()
