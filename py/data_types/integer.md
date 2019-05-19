# Integer

### [_Stack Overflow: Integer overflow_](https://stackoverflow.com/questions/45528637/checking-integer-overflow-in-python#45528715) 

```python
if (abs(num) > (2 ** 31 - 1)):
    return False
```

## Data Conversion

#### `int` -> `string`

```python
num_str = str(10)
num_str.__str__(10)
```

#### `int` -> `float`

#### `list` -> `int`

[_Stack Overflow: list to int_](https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number)

```python
nums = [1, 2, 3]
magic = lambda nums: int(''.join(str(i) for i in nums))
num = magic(nums)
```