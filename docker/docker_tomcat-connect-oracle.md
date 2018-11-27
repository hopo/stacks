# Oracle and Tomacat
오라클 도커 'oracle-xe' and 톰캣8 도커 'was2'

### Make docker container 'was2'
+ Binding port volume link
	- link : between container and container

```
$ docker run -it --name was2 -p 8082:8080 \
> -v ~/webroot/:/usr/local/tomcat/webapps/ \
> --link oracle-xe:oracle-xe tomcat:8 /bin/bash
```
ex) --link name:alias
description) make hosts name'oracle-xe' in the container 'was2'

### Make db dump file
```
$ exp java/oracle file=java-oracle.dmp
```

### Dumpfile copy to oracle-xe(container)
```
$ docker cp java-oracle.dmp oracle-xe:/dump/
```

###Create user in oracleDB
```
$ sqlplus system/oracle
SQL> .....
SQL> exit
```

###Import dump file in to oracle-xe(container)
```
$ imp java/oracle fromuser=java touser=java file=java-oracle.dmp
```
