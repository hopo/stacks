# cron

```bash
$ crontab -e

#
# 15	10	   *	 *	   3-5   echo "$(date): checking in. >> /var/log/mycheckin"
# (m)   (h)    (dom) (moy) (wd)  (cmd)
```


### field / allowed values

field | allowed values
--- | ---
minute | 0-59
hour | 0-23
day of month | 1-31
month | 1-12 (or names, see below)
day of week | 0-7 (0 or 7 is Sun, or use names)


### 도움도구
+ crontab guru : https://crontab.guru



### 교육자료
+ Linux/Mac Tutorial: Cron Jobs - How to Schedule Commands with crontab : https://www.youtube.com/watch?v=QZJ1drMQz1A

