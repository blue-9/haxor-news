# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import print_function
from __future__ import division

import mock
import os
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from hncli.haxor import Haxor


class HaxorTest(unittest.TestCase):

    def setUp(self):
        self.haxor = Haxor()

    def test_set_get_fuzzy(self):
        self.haxor.set_fuzzy_match(True)
        assert self.haxor.get_fuzzy_match()
        self.haxor.set_fuzzy_match(False)
        assert not self.haxor.get_fuzzy_match()
