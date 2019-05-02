# multiprocessing

Call function with execution timer

```python
from multiprocessing import Process
import time

def get_res(arg):
    pass

def execute(arg, timeout=90):
    process = Process(target=get_dir_res, args=(arg))
    start = time.clock()
    res = process.start()
    while process.is_alive():
        if time.clock() - start > timeout:
            process.terminate()
            execute(arg)
        if not process.is_alive():
            break
    return res
```