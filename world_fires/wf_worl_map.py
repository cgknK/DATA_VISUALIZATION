# csv yazdırmayı da dene

import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

rows_limit = 5_000

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brights, dates, hover_texts = [], [], [], [], []
    all_rows_data_selected = []
    row_num = 1
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        bright = float(row[2])
        brights.append(bright)
        date = datetime.strptime(row[5], '%Y-%m-%d')
        dates.append(date)
        hover_texts.append(f"{date.strftime('%m/%d/%y')} - {bright} - {row[-1]}")
        
        row_num += 1
        if row_num == rows_limit:
            break

        all_rows_data_selected.append([lats[-1], lons[-1], brights[-1],
                dates[-1], hover_texts[-1]])

filename_saved_csv = 'data/my_world_fires_1_day.csv'
with open(filename_saved_csv, 'w', newline='') as f:
    w = csv.writer(f)
    for row in all_rows_data_selected:
        w.writerow(row)

print(lats[:5])
print(lons[:5])
print(brights[:5])
print("times\n", dates[:5])
print(hover_texts[:5])
print(len(lats))
print(len(lons))
print(len(brights))
print(len(dates))
print(len(hover_texts))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [0.025 * bright for bright in brights],
        'color': brights,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title=filename)

fig = {'data': data, 'layout': my_layout}
# plotly offline'a bak
offline.plot(fig, filename='world_fires.html')


#print(header_row)
#volume = time * brightness

