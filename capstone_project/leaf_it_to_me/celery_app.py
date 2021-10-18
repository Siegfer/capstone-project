from leaf_it_to_me.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("leaf_it_to_me.tasks.example",)
