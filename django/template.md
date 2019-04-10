# Template

## Template inheritance

### Extends

```html
{% extends 'blog/base.html' %}
```

### Include
https://docs.djangoproject.com/es/1.10/ref/templates/builtins/#include

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

***

## Images
`<img src="/static{{path.0}}">`