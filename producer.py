import cv2
import redis

from common import REDIS_HOST, REDIS_PORT, ENTRY_KEY, STREAM_NAME, log

cam = cv2.VideoCapture(0)
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
r.flushdb()

while True:

    try:

        ret, frame = cam.read()

        if not ret:
            log('could not read from camera')
            break

        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            log('could not encode frame')
            break

        r.xadd(STREAM_NAME, {ENTRY_KEY: buffer.tostring()}, maxlen=1000)

    except (KeyboardInterrupt, InterruptedError):
        log('quitting ...')
        break

cam.release()
r.close()
