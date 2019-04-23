```python
# NOTE: Execution time measurement - https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
import time

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
```