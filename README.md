This repository contains different testing techniques.

#### [doctest](https://docs.python.org/3/library/doctest.html)

Here doctest is used for _encode_ function in morse module.

To run tests you should write in your command line:
```commandline
python3 -m doctest -o IGNORE_EXCEPTION_DETAIL -v morse.py
```
You should get the same output as in _results.txt_ file. 
