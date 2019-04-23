# CSV

## Reading

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