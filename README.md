# Proxify [![python](https://img.shields.io/badge/Python-universal-white.svg?style=style=flat-square)](https://www.python.org/downloads/) ![version](https://img.shields.io/badge/Version-v1_(stable)-blue.svg?style=style=flat-square) [![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=style=flat-square)](https://github.com/UltimateHacke/XSStrike/blob/master/license.txt)

<img src='https://i.imgur.com/AidfpCt.png' />

Proxify is a python module for dumping usable proxies.</br>
It supports both python2 and python3 and can be install via pip as follows.
```
pip install proxify
```

## Documentation

The proxies returned by <b>proxify</b> are in following format:
```
protocol://ip_address:port
```
For example,
```
http://127.0.0.1:8080
```

To get 1 proxy you can simply do this:
``` python
import proxify
proxy = proxify.one()
```
Output:
```
http://103.74.244.199:8080
```
<hr />

To get many proxies, do this:
``` python
import proxify
proxy = proxify.many()
```
Output:
```
[u'http://47.88.32.46:3128', u'http://47.52.222.165:80', u'http://37.59.47.13:3128',
u'http://67.63.33.7:80', u'http://51.15.35.239:3128', u'http://185.82.212.95:8080',
u'http://151.80.140.233:54566', u'http://27.254.200.55:80', u'http://173.212.228.42:10059',
u'http://115.84.178.73:6666', u'http://47.88.242.10:80'
.....
u'http://54.207.104.166:8080']
```
<hr />

To dump a specific number of proxies, lets say '5'. You can do this:
``` python
import proxify
proxy = proxify.get(5)
```
Output:
```
[u'http://47.88.32.46:3128', u'http://47.52.222.165:80', u'http://37.59.47.13:3128',
u'http://67.63.33.7:80', u'http://51.15.35.239:3128']
```

### Note
By default, not passing parameters will be queried the list of new proxies,
while passing as arguments 'anonimous', 'uk', 'us' the respective lists will be queried.<br>
The many() function dumps 300 proxies which is also the maximum number of proxies you can dump with get() function. If you specify a number large than 300, it will automatically become 300.<br>
The one() function returns a string while many() and get() return a list.

#### Dependencies
- requests
- re
- random


Made with ![heart](https://cloud.githubusercontent.com/assets/4301109/16754758/82e3a63c-4813-11e6-9430-6015d98aeaab.png) by <a href=https://twitter.com/s0md3v>Somdev Sangwan</a>
