# BeautifulSoup

```python
from bs4 import BeautifulSoup
```

Open html template as `soup`
```python
with open(os.path.join(os.path.dirname(__file__), "template.html")) as file:
    soup = BeautifulSoup(file)
```

Change value in the tag by `id` 

`<tag_name id="tag_id"> Value </tag_name>`
```python
tag = soup.find(id="id_name")
tag.string = "New Value"
```

[Stack overflow: Create a new tag](https://stackoverflow.com/questions/21356014/how-can-i-insert-a-new-tag-into-a-beautifulsoup-object)
```python
new_tag = soup.new_tag("a", href="http://www.example.com")
```

Insert new tag into body
```python
div = "<div>New div</div>"
soup.body.append(div)
```

[Stack overflow: Remove tags: html, head](https://stackoverflow.com/questions/14822188/dont-put-html-head-and-body-tags-automatically-beautifulsoup)
```python
soup.body.next
```