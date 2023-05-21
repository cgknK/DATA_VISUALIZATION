# Bu plotly.xyz xyz'yi kullanmak neden zorunlu, neden kapsamıyor?
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() + die_2.roll()
    if result < 13 and result > 1:
        results.append(result)
    else:
        print(f"Hata {result}")

#print(results)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for v in range(2, max_result + 1):
    frequency = results.count(v)
    frequencies.append(frequency)

#print(frequencies)

# Visualize the results.
x_values = list(range(2, max_result + 1))
# data(yani Bar()) neden [] ile sarmalanıyor?
#Bir yukarıdaki list() ile [] aynı mı?
data = [Bar(x=x_values, y=frequencies)]
print(type(data))
# Bu data nasıl bir list?
print(data)

data_deneme = Bar(x=x_values, y=frequencies)
print(type(data_deneme))
print(data_deneme)

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency o result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', 
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, 
        filename='d6_d6.html')

