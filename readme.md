# Getting started

The processes should be started in the following order

1. Install all the python dependencies
```
pip install requirements.txt
```
2. Start a redis server to maintain the task queue

```
docker run -d -p 6379:6379 redis
```

3. Start the flask server to maintain the status completion for each video

```
python server.py
```

4. Starting n-number of worker

```
celery -A tasks worker --loglevel=INFO
```

5. Assign tasks the worker


```
python app.py
```

