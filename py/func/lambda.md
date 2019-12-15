# Lambda

**Finding strings with given substring in list**
```python
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms'] 
subs = 'Geek'
res = list(filter(lambda x: subs in x, test_list)) 
```