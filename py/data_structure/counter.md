```python
import collections

counter = collections.Counter([1, 1, 1, 2, 2, 3])
for elem, count in counter.items():
    print("{}: {}".format(elem, count))

for elem, count in counter.most_common():
    print("{}: {}".format(elem, count))
```