# Template

## Template inheritance

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