import uuid


REDIS_HOST = "localhost"
REDIS_PORT = "6379"

STREAM_KEY = 'videostream'
ENTRY_KEY = b'frame'


def log(msg):
    print(msg, flush=True)
