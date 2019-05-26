# CSV

```python
import csv
```

## Reading

[_Stack Overflow: Read CSV_](https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module)

```python
@staticmethod
    def get_csv_values(path, collumn) -> list:
        res = []
        with open(path, "r") as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                res.append(row[collumn])
        return res
```

## Writing

## Appending
```python
def append_in_csv(path, row):
        """ 
        :path: to file
        :row: of values
        """
        with open(path, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()
```