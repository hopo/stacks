# Log Rotation
	
### 1. Rotration of logs based on criteria
1. size
2. age (daily, weekly, monthly)

### 2. Compression
### 3. Maintain logs for a defined period

- - -

`etc/logrotate.conf`
+ primary (global) config file for all logs
	- can be overrriden by context-sesitive files. i.e. apache

> (default)

`etc/logrotate.d/`
+ httpd - used to rotate Apache logs


### 참고자료
> http://blog.weirdx.io/post/20441
