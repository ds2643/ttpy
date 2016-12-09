# pytest unit tests

import main as m

def test_program_as_ast():
    result = m.program_as_ast("./data/example.py") # TODO: relative file path
    assert (isinstance(result, redbaron.redbaron.RedBaron))

def test_collect_f_names():
    PATH = "./data/example.py"
    str_repr = open(path, 'r').read()
    ast = RedBaron(str_repr)
    result = m.collect_f_names(ast)
    EXPECTED_NO_FUNCTIONS = 3
    contents_as_expected = ("foo" in result and "bar" in result and "baz" in result)
    assert (len(result) == EXPECTED_NO_FUNCTIONS and contents_as_expected)

def test_template_test_str():
    sample_func_name = "foo"
    actual = m.template_test_str(sample_func_name)
    EXPECTED = "test_foo"
    assert (actual == EXPECTED)
