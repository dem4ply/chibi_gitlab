#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chibi_gitlab.urls import projects, merge_requests


class Test_projects( unittest.TestCase ):
    def setUp(self):
        pass

    def test_should_work(self):
        result = projects.get()
        self.assertTrue( result.ok )


class Test_merge_requests( unittest.TestCase ):
    def setUp(self):
        pass

    def test_should_work(self):
        result = merge_requests.get()
        self.assertTrue( result.ok )
