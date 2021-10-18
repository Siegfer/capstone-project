FLASK_ENV=development
FLASK_APP=leaf_it_to_me.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:///leaf_it_to_me.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
