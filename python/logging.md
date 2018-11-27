# python logging : 파이썬 로깅


### 1) logging을 임포트 한 후 basicConfig()
+ filename
+ 로깅 레벨
+ format

```python
import logging
logging.basicConfig(
		filename='test-sample.log',
		level=logging.DEBUG,
		format='%(asctime)s : %(name)s : %(message)s'
	)

# When Call
logging.debug()
```

- - -

### 2) format : 로그레코드
_링크참고 (https://docs.python.org/3.6/library/logging.html#logrecord-attributes)_

- - -

### 3) 다르게
+ getLogger()
+ setLevel()
+ Formatter()
+ FileHandler() 	
+ setFotmatter()
+ addHandler() 	

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler) # Traceback

# When Call
logger.debug()
```

- - -

### 4) 다르게2
+ TimedRotatingFileHandler()

```python
web_log_file_handler = TimedRotatingFileHandler(
							filename="/home/system/logs/creditcard/creditcard.web.log",
							when="midnight",
							interval=1,
							encoding="utf-8"
						)
web_log_file_handler.setFormatter(
		Formatter(
			"[%(process)d:%(processName)s:%(thread)d:%(threadName)s] %(asctime)s : %(message)s [in %(filename)s:%(lineno)d]")
		)
web_logger.setLevel(logging.INFO)
web_logger.addHandler(web_log_file_handler)
```
_링크참고 (http://ash84.net/2015/11/04/logrotate-usage/)_
