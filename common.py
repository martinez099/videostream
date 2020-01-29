import uuid


REDIS_HOST = "localhost"
REDIS_PORT = "6379 "

STREAM_KEY = 'videostream:{}'.format(str(uuid.uuid4()))
ENTRY_KEY = b'frame'


def log(msg):
    print(msg, flush=True)
