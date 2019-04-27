# exec()

```python
# Execute from file
x_dict = {}
with open("<file.py>") as file:
    exec(file.read(), x_dict)
```