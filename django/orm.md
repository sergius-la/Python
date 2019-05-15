# Object-relational mapping

### Django migrate

```shell
./manage.py makemigrations
```

```shell
./manage.py migrate
```

### Mapping Existing database:
- `python manage.py inspectdb`
- `python manage.py inspectdb > models.py`

##  Lookups

```python
Model.objects.all() # Return all objects
post = Post.objects.get(slug__iexact="New-Slug") # Case insensetive
post = Post.objects.get(slug__contains="New") 
```

## Console

### Create model object from console
```shell
$ (vevn) python
$ import Post
$ pl = Post.objects.create(title="new post", slug="new_post", body="body text")
```














