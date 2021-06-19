The processes should be started in the following order

# Install all the python dependencies

`pip install requirements.txt`

# Start a redis server to maintain the task queue

`docker run -d -p 6379:6379 redis`

# Start the flask server to maintain the status completion for each video

`python server.py`

# Starting n-number of worker

`celery -A tasks worker --loglevel=INFO`

# Assigning tasks the worker

Tasks can be assigned to the workers by running the python app by:

`python app.py`

