# Proxify [![python](https://img.shields.io/badge/Python-universal-white.svg?style=style=flat-square)](https://www.python.org/downloads/) ![version](https://img.shields.io/badge/Version-v1_(stable)-blue.svg?style=style=flat-square) [![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=style=flat-square)](https://github.com/UltimateHacke/XSStrike/blob/master/license.txt)

> Proxify is a python module for dumping usable proxies.

<p align="center">
  <img src="https://i.imgur.com/AidfpCt.png">
</p>

# How to install
+ In Linux
```
$ pip install --user proxify
```
+ In Windows
```
> pip install proxify
```

# How to use

The proxies returned by **proxify** are in following format:
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
--------

To get many proxies, do this:
``` python
import proxify
proxy = proxify.many()
```
------

To dump a specific number of proxies, lets say '5'. You can do this:
``` python
import proxify
proxy = proxify.get(5)
```

# What the functions do ?
|Function Name|What the do|
|----|----|
|many()|Returns the list of maximum proxies you can dump|
|get(n)|Returns the list of n proxies, _0 < n <= 300_ |
|one()|Returns the string of proxies|

