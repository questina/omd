This repository contains different testing techniques.

## [doctest](https://docs.python.org/3/library/doctest.html)

Doctest is used for _encode_ function in morse module. To run tests you should write in your command line:
```commandline
python3 -m doctest -o IGNORE_EXCEPTION_DETAIL -v morse.py
```

You can run it without -v option, but it will not write you explained output about tests. 

You should get the same output as in _results/results_doctest.txt_ file. 


## pytest.mark.parametrize

Test is used for _decode_ function in morse module. To run tests you should write in your command line:
```commandline
python3 -m pytest tests/test_decode.py
```

To get explained output, add -v flag:
```commandline
python3 -m pytest -v tests/test_decode.py
```

You should get the same output as in _results/results_mark_parametrize.txt_ file. 

## [unittest](https://docs.python.org/3/library/unittest.html)

Unittest is used for _fit_transform_ function in one_hot_encoder module. To run tests you should write in your command line:
```commandline
python3 -m unittest tests/test_one_hot_encoder_ut.py
```

To get explained output, add -v flag:
```commandline
python3 -m unittest -v tests/test_one_hot_encoder_ut.py
```

You should get the same output as in _results/results_unittest.txt_ file. 

## [pytest](https://docs.pytest.org/en/7.4.x/)

Pytest is used for _fit_transform_ function in one_hot_encoder module. To run tests you should write in your command line: 
```commandline
python3 -m pytest tests/test_one_hot_encoder_pt.py
```

To get explained output, add -v flag:
```commandline
python3 -m pytest -v tests/test_one_hot_encoder_pt.py
```

You should get the same output as in _results/results_pytest.txt_ file.

## unittest.mock
Unittest is used for _what_is_year_now_ in what_is_year_now module. To run tests you should write in your command line:
```commandline
python3 -m unittest tests/test_what_is_year_now.py
```

To get explained output, add -v flag:
```commandline
python3 -m unittest -v tests/test_what_is_year_now.py
```

If you want to get your code coverage report you should make sure that you installed
coverage tool:
```commandline
python3 -m pip install coverage
```

After that run following commands:

```commandline
python3 -m coverage run -m unittest tests/test_what_is_year_now.py
coverage report -m what_is_year_now.py
```

You will see a report in your console. If you want to generate html report run:
```commandline
coverage html what_is_year_now.py
```

You should get the same output as in _results/results_unittest_mock.txt_ file.