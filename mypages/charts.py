from typing import List
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
import numpy as np

COLORS = [
    '#FE2D01',
    '#016CFE',
    '#FEB101',
    '#FE018B',
    '#AAB7B8',
    '#212F3D'
]

'''
    clusters = ['Cluster 1', 'C 2', 'C 3', 'Plums', 'Grapes', 'Strawberries']
    years = ['number of papers', 'number of keyphrases', ]

    data = {'clusters': clusters,
            f'{years[0]}': [2, 1, 4, 3, 2, 4],
            f'{years[1]}': [5, 3, 3, 2, 4, 6],
            }

    source = ColumnDataSource(data=data)

    p = figure(x_range=clusters, title="Fruit counts by year",
               toolbar_location=None, tools="")

    p.vbar(x=dodge('clusters', -0.25, range=p.x_range), top=f'{years[0]}', width=0.2, source=source,
           color="#c9d9d3", legend_label="2015")

    p.vbar(x=dodge('clusters', 0.0, range=p.x_range), top=f'{years[1]}', width=0.2, source=source,
           color="#718dbf", legend_label="2016")


    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
'''


def build_bar_charts(x_range: List, y_names: List[str], y_data = List[List]):
    valid_y = lambda x: len(x) == len(x_range)
    if not (len(y_names) == len(y_data) and all(map(valid_y,y_data))):
        raise RuntimeError('The data shapes are not aligned.')


    if len(y_names) % 2 == 0:
        offsets = [-0.125 - 0.25*(i-1) for i in range(len(y_names)//2,0,-1)]
        offsets += [0.125 + 0.25*(i) for i in range(len(y_names)//2)]
    else:
        offsets = [-0.25 * i for i in range(len(y_names)//2,0,-1)]
        offsets.append(0)
        offsets += [0.25* (i+1) for i in range(len(y_names)//2)]

    data = {
        'x': x_range
    }
    for i,y in enumerate(y_data):
        data[f'y{i}'] = y
    source = ColumnDataSource(data)
    p = figure(x_range=x_range,
               tools = "box_zoom,save,reset",
               height=500,
               y_range=(0,np.max(y_data)+10)
               )

    for i,y in enumerate(y_data):
        p.vbar(x=dodge('x', offsets[i], range=p.x_range), top=f'y{i}', width=0.2, source=source,
               color=COLORS[i], legend_label=y_names[i])

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    return p

