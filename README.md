# inspector_mils

[![CodeFactor](https://www.codefactor.io/repository/github/jmilagroso/inspector_mils/badge)](https://www.codefactor.io/repository/github/jmilagroso/inspector_mils)
[![travis](https://travis-ci.com/jmilagroso/pii_crypt.svg?branch=master)](https://travis-ci.com/jmilagroso/pii_crypt.svg?branch=master)
[![codecov](https://codecov.io/gh/jmilagroso/inspector_mils/branch/master/graph/badge.svg?token=HMC508346L)](https://codecov.io/gh/jmilagroso/inspector_mils)
[![python3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![python3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![python3.6](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

Inspect functions' arguments and keywords arguments at runtime using decorator.

## Installation
To download inspector-mils, either fork this github repo or simply use Pypi via pip
```sh
pip install inspector-mils
```

## Usage
Import `inspect` decorator.
```sh
from inspector_mils.inspector import inspect
```

Add `@inspect` to your function.
```sh
@inspect
def my_func_sample1(a, b):
  pass

my_func_sample1("param1", "param2")
```
Output
```sh
[2022-11-04 02:42:45.151303] Starting inspect..
[2022-11-04 02:42:45.151888] my_func_sample1() called..
[2022-11-04 02:42:45.151937] args: ('param1', 'param2')
[2022-11-04 02:42:45.151978] kwargs: {}
[2022-11-04 02:42:45.152060] Ending inspect..
```
