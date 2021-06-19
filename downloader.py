from __future__ import unicode_literals
import youtube_dl
import json
from tqdm import tqdm
import atexit
import time
import uuid

trailers = {}
failed = {}
succeeded = {}

# try:
#     with open("failed.json") as f:
#         failed = json.loads(f.read())
#     with open("succeeded.json") as f:
#         succeeded = json.loads(f.read())
# except Exception as e:
#     pass



# with open("trailers.json") as f:
#     trailers = json.loads(f.read())
#     for x in trailers.keys():
#         if x in succeeded or x in failed:
#             del trailers[x]


# def save_state():
#     with open("failed.json", 'w+') as f:
#         f.write(json.dumps(failed))

#     with open("succeeded.json", "w+") as f:
#         f.write(json.dumps(succeeded))


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        raise ValueError(msg)

class YTDownloader(object):
    
    @staticmethod
    def download(url):
        ydl_opts = {
            'format': '18',
            'outtmpl': './v3/' + str(uuid.uuid4()) + ".%(ext)s",
            'logger': MyLogger(),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            # result = ydl.extract_info(
            #     url,
            # )

# for trailer in tqdm(trailers.keys()):
#     try:
#         YTDownloader.download(trailer)
#         succeeded[trailer] = trailers.get(trailer)
        
#     except Exception as e:
#         print("%s: %s" % (e, trailer))
#         failed[trailer] = trailers[trailer]
#     save_state()
#     time.sleep(1)


# atexit.register(save_state)
