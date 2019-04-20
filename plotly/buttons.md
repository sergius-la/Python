# Custom Buttons

Hide / Show traces

```python

data = [trace1, trace2]

updatemenus = list([
    dict(type="buttons",
         buttons=list([
            dict(label = 'Show Trace 1',
                 method = 'update',
                 args = [{'visible': [True, False]},
                         {'title': 'Trace 1'}]),
            dict(label = 'Show Trace 2',
                 method = 'update',
                 args = [{'visible': [False, True]},
                         {'title': 'Trace 2'}]),
        ]),
    )
])
```