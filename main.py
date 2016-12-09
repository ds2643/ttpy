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

def template_test_string(func_name):
    ''' outputs string for function name '''
    assert(isinstance(function_name, str))
    return "test_" + func_name

if __name__ == "__main__":
    source_path = sys.argv[1] # first argument is source path
    source_ast = program_as_ast(source_path)
