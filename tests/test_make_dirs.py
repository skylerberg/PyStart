import mock
import os
import unittest

import pystart


class TestMakeDirs(unittest.TestCase):

    @mock.patch(os.mkdir)
    def test_directory_structure(self, fake_mkdir):
        pystart.make_dirs()
