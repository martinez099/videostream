import cv2
import numpy
import redis

from common import REDIS_HOST, REDIS_PORT, STREAM_KEY, ENTRY_KEY, log

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

try:
    while True:

        # read from stream
        buffer = r.xread({STREAM_KEY: '$'}, block=1000, count=1)
        if not buffer:
            continue

        # decode image
        frame = cv2.imdecode(numpy.frombuffer(buffer[0][1][0][1][ENTRY_KEY], numpy.uint8), 1)

        # render framebuffer
        cv2.imshow('frame', frame)

        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            log('quitting ...')
            break

except (KeyboardInterrupt, InterruptedError):
    log('quitting ...')

r.close()
