# SQLite3

Connection to database, Curson
```python
connection = sqlite3.connect("<path>.sqlite3")
cursor = connection.cursor()
```

Get data from db
```python
query = "SELECT * FROM <table>"
db_data = [x[0] for x in cursor.execute(query).fetchall()]
```

Insert data into db
```python
cursor.execute("insert into <table> VALUES(?, ?)", (123, "<value>"))
connection.commit()
```