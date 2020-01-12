import cv2
import numpy
import redis

from common import REDIS_HOST, REDIS_PORT, STREAM_NAME, ENTRY_KEY, log

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

while True:

    buffer = r.xread({STREAM_NAME: '$'}, block=1000, count=1)

    if not buffer:
        log('could not read from stream')
        break

    frame = cv2.imdecode(numpy.frombuffer(buffer[0][1][0][1][ENTRY_KEY], numpy.uint8), 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        log('quitting ...')
        break

r.close()
