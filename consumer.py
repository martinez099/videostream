import cv2
import numpy
import redis

import common

r = redis.StrictRedis()

while True:

    buffer = r.xread({common.STREAM_NAME: '$'}, block=1000, count=1)

    if not buffer:
        common.log('could not read from stream')
        break

    frame = cv2.imdecode(numpy.frombuffer(buffer[0][1][0][1][common.ENTRY_KEY], numpy.uint8), 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        common.log('quitting ...')
        break

r.close()
