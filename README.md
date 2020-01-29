# videostream
This is a video streaming sample implementation using Redis streams.

It assumes a running Redis instance on localhost:6379.

## Prerequisites

- Python 3 including pip
- Redis 5
- a built-in webcam

## Setup

```pip install -r requirements.txt```

## Run

- run one producer 

```python3 producer.py```

- run one or multiple consumers

```python3 consumer.py```
