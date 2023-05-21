import matplotlib.pyplot as plt

from die import Die

d6 = Die()

results = [d6.roll() for roll_num in range(1000)]
print(min(results))
print(max(results))
print(sum(results) / 1000)

frequencies = [results.count(value) for value in range(1,7)]

print(frequencies)
print(sum(frequencies))

plt.style.use('classic')
fig, ax = plt.subplots()
bar_names = [ str(v) for v in range(1, len(frequencies) + 1)]
print(bar_names)

freq_list = [v for v in range(1, len(frequencies) + 1)]
print(freq_list)

ax.bar(bar_names, frequencies)

plt.show()