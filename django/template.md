# Template

- [Stack Overflow - Django & Bootstrap Template](https://stackoverflow.com/questions/10157059/how-can-i-use-bootstrap-with-django)

- [Docs](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-template-tags-and-filters)

## Template inheritance

### Extends

```html
{% extends 'blog/base.html' %}
```

### Include

[_Django docs: Include_](https://docs.djangoproject.com/es/1.10/ref/templates/builtins/#include)

```html
{% include "app/includes/block.html" %}
```

***

## Variables
```html
{{ variable }}
```

***

## Blocks

### Title
```html
{% block title %}
    Default Title 
{% endblock %}
```

### Content
```html
{% block content %}
    Content
{% endblock %}
```

***

## Loops

### For-each loop
```html
{% for post in posts %}
   <h3> {{ post.title }} </h3>
{% endfor %}
```

***

## String format

### String float format
```html
{{ test.avg|floatformat:2 }}
```
### String truncatewords
```html
<p class="card-text">{{post.body|truncatewords:15}}</p>
```

***

## Static files

```html
{% load static %}
```

### Images

`<img src="/static{{path.0}}">`
