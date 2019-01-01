#!/usr/bin/python3
import sys; sys.path[0] = ''

from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO
from datetime import date as Date
import unittest

import busy.future

class TestDate(TestCase):

    @mock.patch('busy.future.today', lambda : Date(2019,2,11))
    def test_today(self):
        t = busy.future.date_for('today')
        self.assertEqual(t, Date(2019, 2, 11))

if __name__ == '__main__': unittest.main()
