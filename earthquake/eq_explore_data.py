import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data_30_day_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

"""
filename = 'data/readable_eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
"""

"""
json header incele
noindent_file = 'data/noindent_eq_data_1_day_m1.json'
deneme_eq_data = []
with open(noindent_file, 'w') as f:
    for row in all_eq_data:
        deneme_eq_data += row + '\n'
    json.dump(deneme_eq_data, f)
"""

all_eq_dicts = all_eq_data['features']
print(len(all_eq_data))
print(type(all_eq_data))
print(type(all_eq_dicts))
print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map the earthquakes.
"""
Neden Scattergeo() yu [] wrapperlıyoruz, We create the Scattergeo object inside 
this list ➋, because you can plot more than one data set on any visualization 
you make. _Anlamadım
"""
#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    # Buradaki scattergeo'nun 's' ilk karakteri neden küçük?
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    # 'text' lons ve lats değerleri kontrol edilmeli, ve hover_texts eleman 
    #sayısı diğerleri ile eşleşmez ise bir noktada birden fazla etiket veya
    #(eksik olma durumu için) boş etiketler mi olur?
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
automated_title = all_eq_data['metadata']['title']
my_layout = Layout(title=automated_title)

fig = {'data': data, 'layout': my_layout}
# plotly offline'a bak
offline.plot(fig, filename='global_earthquakes.html')