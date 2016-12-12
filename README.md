# ttpy: test templating for Python projects
A script for templating pytest unit tests for Python projects in an automated manner. Given a Python program, ttpy traverses the abstract syntax tree for function names to generate a file containing empty test cases for each function. This approach saves the programmer wasted time searching the source file for all functions.

## Use
The program uses a simple command-line interface.

at the command line, indicate the source file for which to generate a pytest template.

    $> python ttpy [source path] [result path]

for example, one may call ttpy to generate tests for a file main.py with the result saved to test.py as follows:

    $> python ttpy main.py tests.py

ttpy parses the source file to find functions than constructs a test template for each function in the source file.

*in source:*
```python
def append(x, xs):
    ''' add something to a list '''
    return x + xs
```

*result:*
    ```python
       def test_append():
        # TODO: write test!
        assert(false)
    ```
## Dependencies
The tool assumes unit tests will be written in PyTest (), an alternative to Python's built-in unittest module.

Pytest features a number of advantages over unittest with [arguably better (or equivilent) functionality](http://halfcooked.com/presentations/pyconau2013/why_I_use_pytest.html).

Instructions for installing and using Pytest can be found [here](http://doc.pytest.org/en/latest/getting-started.html)

Additionally, this script uses [RedBaron](https://github.com/PyCQA/redbaron) to traverse the source file's abstract syntax tree.
