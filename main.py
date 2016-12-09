import os
import sys
import redbaron

def program_as_ast(path):
    ''' returns program (specified by path) as Python abstract syntax tree (Redbaron)'''
    try:
        str_repr = open(path,'r').read()
    except:
        print("specified file doesn't exist") #TODO replace with proper error
    return RedBaron(str_repr)

def collect_f_names(ast):
    ''' given a program represented as a redbaron abstreact syntax tree, return a list of all functions defined within the context of that source file '''
    f_def_nodes = ast.find_all("DefNode")
    return [node[0].name for node in f_def_nodes]

def template_test_name(func_name):
    ''' outputs string for function name '''
    assert(isinstance(function_name, str))
    return "test_" + func_name

def test_str(func_name):
    indent = "\s\s\s\s"
    new_line = "\n"
    name = template_test_name(func_name)
    def_line = "def " + name + "():" + new_line
    doc_string = indent + "\"\"\"" + "testing: " + name +"\"\"\"" + new_line
    reminder = indent + "# TODO: write test..." + new_line
    failing_assertion = indent + "assert (false)" + new_line
    res = def_line + doc_string + reminder + failing_assertion + new_line
    assert(isinstance(res, str))
    return res

def generate_test_program(func_names):
    assert (isinstance(func_names, list))
    program = ''.join([test_str(func_name) for func_name in func_names])
    return program

def write_to_file(path, prog_str):
    ''' write program to  specified path '''
    # TODO assert path is not currently occupied
    exists = os.path.isfile(path)
    assert (not exists)
    f = open(path, 'r+')
    header = "# automatically generated pytest template with ttpy \n"
    f.write((header + prog_str))
    f.close()

if __name__ == "__main__":
    src_path = sys.argv[1]
    dst_path = sys.argv[2]
    assert (src_path.endswith(".py"))
    assert (dst_path.endswith(".py"))

    src_ast = program_as_ast(src_path)
    func_names = collect_f_names(src_ast)
    test_program_str = generate_test_program(func_names)
    write_to_file(dst_path, test_program_str)
    print("the test file can be found at ", dst_path)
