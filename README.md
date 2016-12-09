*Please note this project is not yet complete or ready for use.*

# ttpy
Test templating tool for python projects.

This tool is intended to quickly template unit tests for pytest. The resulting template does not contain any useful test logic, but saves the programmer time fetching function names and provides motivating for good test coverage (in the sense of having at least a test per function in source).

## Use

at the command line, indicate the source file for which to generate a pytest template.
`$> python ttpy [source] [output]`
e.g.,
`$> python ttpy main.py tests.py`

ttpy parses the source file to find functions than constructs a test template for each function in the source file.
*in source:*
    `def append(x, xs):
        ''' add something to a list '''
        return x ++ xs
    `
*result:*
    `def test_append():
        # TODO: write test!
        assert(false)
    `

