import cv2
import redis

import common

cam = cv2.VideoCapture(0)
r = redis.StrictRedis()

while True:

    try:

        ret, frame = cam.read()

        if not ret:
            common.log('could not read from camaera')
            break

        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            common.log('could not encode frame')
            break

        r.xadd(common.STREAM_NAME, {common.ENTRY_KEY: buffer.tostring()}, maxlen=1000)

    except (KeyboardInterrupt, InterruptedError):
        common.log('quitting ...')
        break

cam.release()
r.close()
