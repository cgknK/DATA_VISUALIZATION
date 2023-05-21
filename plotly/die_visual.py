# Bu plotly.xyz xyz'yi kullanmak neden zorunlu, neden kapsamıyor?
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die_6 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_6.roll()
    if result < 7 and result > 0:
        results.append(result)
    else:
        print(f"Hata {result}")

#print(results)

# Analyze the results.
frequencies = []
for v in range(1, die_6.num_sides + 1):
    frequency = results.count(v)
    frequencies.append(frequency)

#print(frequencies)

# Visualize the results.
x_values = list(range(1, die_6.num_sides + 1))
# data(yani Bar()) neden [] ile sarmalanıyor?
#Bir yukarıdaki list() ile [] aynı mı?
data = [Bar(x=x_values, y=frequencies)]
print(type(data))
# Bu data nasıl bir list?
print(data)

data_deneme = Bar(x=x_values, y=frequencies)
print(type(data_deneme))
print(data_deneme)

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency o result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, 
        filename='d6.html')

