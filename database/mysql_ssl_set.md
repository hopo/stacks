
# mysql database SSL set and connect

## connect mysql

```
$ mysql -h {hostname} \
		--ssl-ca={pem_path} \
		--ssl-mode=REQUIRED \
		-u {username} \
		-P {port_number} \
		-p
```


## mysql database ssl check

```
mysql> \s;

mysql> SHOW SESSION STATUS LIKE 'Ssl_cipher';
```
