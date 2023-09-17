import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.scatter(rw.x_value, rw.y_value, s=0.2)
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none',
                s=100)
    plt.savefig('random_walk.png', bbox_inches='tight')
    plt.show()
    keep_running = input('One more? Y/N: ')
    if keep_running.lower() == 'n':
        break
