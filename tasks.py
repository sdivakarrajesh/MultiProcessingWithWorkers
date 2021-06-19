from celery import Celery
from downloader import YTDownloader
import requests

state_server = "http://localhost:8787/"

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')


@app.task
def add(x, y):
    return x + y


def set_as_succeeded(url):
    requests.post(state_server + 'succeeded', data={"url": url})
    

def set_as_failed(url):
    requests.post(state_server + 'failure', data={"url": url})


@app.task(acks_late=True)
def download(trailer):
    try:
        YTDownloader.download(trailer)
        set_as_succeeded(trailer)
    except Exception as e:
        print("%s: %s" % (e, trailer))
        set_as_failed(trailer)
