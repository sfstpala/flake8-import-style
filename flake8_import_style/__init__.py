import ast

import pkg_resources


I801 = "I801 use 'import {module}' instead of 'from {module} import {names}'"


class I8(object):
    """Complain about all "from x import y" style imports."""

    name = "import-style"
    version = pkg_resources.get_distribution(__package__).version

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for i in ast.walk(self.tree):
            if isinstance(i, ast.ImportFrom):
                message = I801.format(
                    module=(i.module or "..."),
                    names=", ".join(i.name for i in i.names))
                yield (i.lineno, i.col_offset, message, "I801")
