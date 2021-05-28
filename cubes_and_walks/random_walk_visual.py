import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
    # ax.plot(rw.x_values, rw.y_values, linewidth=3)


    # Emphasize first and last point.
    ax.scatter(0, 0, c='green', edgecolors='none', s=75)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=75)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (Y/N)")
    if keep_running.lower() == 'n':
        break