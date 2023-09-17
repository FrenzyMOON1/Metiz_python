import pygal
from die import Die

die_1 = Die(16)
die_2 = Die(16)

results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_sides = die_1.num_sides + die_2.num_sides
for i in range(2, max_sides + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two Dx 10000 times."
hist.x_labels = [str(x) for x in range(2, max_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(f'D{die_1.num_sides} + D{die_2.num_sides}', frequencies)
hist.render_to_file('die_visual.svg')
