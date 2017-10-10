## Getting started

### Create Twitter applicaton
[Follow these steps](http://python-twitter.readthedocs.io/en/latest/getting_started.html)


### Install [Python-Twitter API wrapper](https://github.com/bear/python-twitter)

```bash
    virtualenv --python=python3.5 venv
    source venv/bin/activate
    pip install python-twitter
```

### Using

Using the token/key from step 1 above
```bash
    CONSUMER_KEY = 'WWWWWWWW'
    CONSUMER_SECRET = 'XXXXXXXX'
    ACCESS_TOKEN = 'YYYYYYYY'
    ACCESS_TOKEN_SECRET = 'ZZZZZZZZ'
```

Run it
```bash
    (venv) test@ubuntu:~/workspace/python/twitter-mute$ python mute.py
```