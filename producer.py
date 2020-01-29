import cv2
import redis

from common import REDIS_HOST, REDIS_PORT, ENTRY_KEY, STREAM_KEY, log

cam = cv2.VideoCapture(0)
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
r.flushdb()

try:
    while True:

        # read from built-in webcam
        _, frame = cam.read()

        # encode frame
        _, buffer = cv2.imencode('.jpg', frame)

        # add to stream
        r.xadd(STREAM_KEY, {ENTRY_KEY: buffer.tostring()}, maxlen=1000)

except (KeyboardInterrupt, InterruptedError):
    log('quitting ...')

cam.release()
r.close()
