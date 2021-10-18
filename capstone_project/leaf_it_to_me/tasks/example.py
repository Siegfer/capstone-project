from leaf_it_to_me.extensions import celery


@celery.task
def dummy_task():
    return "OK"
