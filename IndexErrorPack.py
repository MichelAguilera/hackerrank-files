import sys
import linecache
import ast
import astunparse

def find_index_error():
    tb = sys.exc_info()[2]
    frame = tb.tb_frame
    lineno = tb.tb_lineno
    filename = frame.f_code.co_filename
    line = linecache.getline(filename, lineno, frame.f_globals)
    class find_index_error_node(ast.NodeVisitor):
        def visit_Subscript(self, node):
            expr = astunparse.unparse(node).strip()
            try:
                eval(expr, frame.f_globals, frame.f_locals)
            except IndexError:
                print("%s causes IndexError" % expr)
    find_index_error_node().visit(ast.parse(line.strip(), filename))