import ast
import unittest

import flake8_import_style


class I8Test(unittest.TestCase):

    def test_run(self):

        tree = ast.parse("import mod")
        i8 = flake8_import_style.I8(tree)
        self.assertEqual(list(i8.run()), [])

        tree = ast.parse("import mod as mod1")
        i8 = flake8_import_style.I8(tree)
        self.assertEqual(list(i8.run()), [])

        tree = ast.parse("from . import obj")
        i8 = flake8_import_style.I8(tree)
        self.assertEqual(list(i8.run()), [(
            1,
            0,
            "I801 use 'import ...' instead of 'from ... import obj'",
            "I801",
        )])

        tree = ast.parse("from .. import obj")
        i8 = flake8_import_style.I8(tree)
        self.assertEqual(list(i8.run()), [(
            1,
            0,
            "I801 use 'import ...' instead of 'from ... import obj'",
            "I801",
        )])

        tree = ast.parse("from mod import obj")
        i8 = flake8_import_style.I8(tree)
        self.assertEqual(list(i8.run()), [(
            1,
            0,
            "I801 use 'import mod' instead of 'from mod import obj'",
            "I801",
        )])
