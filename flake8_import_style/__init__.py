import ast

import pkg_resources


__version__ = pkg_resources.get_distribution(__package__).version

I801 = "I801 use 'import {stmt}' instead of 'from {module} import {names}'"


class I8(object):
    """Complain about all "from x import y" style imports."""

    name = "import-style"
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for i in ast.walk(self.tree):
            if isinstance(i, ast.ImportFrom):
                if i.module == "__future__":
                    continue
                module = ("." * i.level) + (i.module or "")
                names = ", ".join(i.name for i in i.names)
                if i.module is None:
                    # Relative imports don't work with the `import <>` syntax.
                    message = I801.format(
                        stmt=names,
                        module=module,
                        names=names)
                elif len(i.names) == 1:
                    message = I801.format(
                        stmt="{0}.{1}".format(i.module, names),
                        module=module,
                        names=names)
                else:
                    message = I801.format(
                        stmt=i.module,
                        module=module,
                        names=names)
                yield (i.lineno, i.col_offset, message, "I801")
