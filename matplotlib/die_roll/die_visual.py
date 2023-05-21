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
freq_size = [v for v in range(len(frequencies))]
ax.scatter(freq_size, frequencies, c=freq_size, 
        cmap='Blues', edgecolors='none', s=10)

plt.show()