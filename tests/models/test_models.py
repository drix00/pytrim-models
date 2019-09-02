#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_models

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


"""

# Copyright 2019 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules.
from trim.models import __author__, __email__, __version__, __copyright__, __project_name__

# Globals and constants variables.


def test_author():
    assert __author__ != ""


def test_email():
    assert __email__ != ""


def test_version():
    assert __version__ != ""


def test_current_version():
    assert __version__ == '0.1.0'


def test_copyright():
    assert __copyright__ != ""


def test_project_name():
    assert __project_name__ != ""
