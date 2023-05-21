import plotly.express as px
import plotly.graph_objs as go
from plotly import offline

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

fig = px.scatter(
        x=rw.x_values, y=rw.y_values)

x_axis_config = {'title': 'L/R'}
y_axis_config = {'title': 'U/D'}
my_layout = go.Layout(title='Random walk',
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': fig, 'layout': my_layout}, 
        filename='rw_plotly.html')