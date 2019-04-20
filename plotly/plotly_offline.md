# Plotly Offline

Get output in the HTML format

```python
div = plotly.offline.plot(
    {"data": data, "layout": layout},
    include_plotlyjs=False, 
    output_type='div')
```

```python
import plotly.offline
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[20, 14, 23, 25, 22],
    marker=dict(
        color=['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)']),
)

data = [trace0]
layout = go.Layout(
    title='Least Used Feature',
)

plotly.offline.plot(
    {"data": data,
    "layout": layout},
    image='jpeg', image_filename='test')
```
