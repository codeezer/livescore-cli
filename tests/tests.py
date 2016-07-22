#!/usr/bin/env python
# -*- coding:utf-8 -*-
from nose.tools import with_setup
from nose.tools import assert_true
import os


class WebTest():

    def test_file_exists_test():
        assert_true(os.path.isfile('resources/EPL.html'))


    @classmethod
    def setup():
        EPL = open('resources/EPL.html', 'rb+').read()

    @with_setup(setup)
    def test_
