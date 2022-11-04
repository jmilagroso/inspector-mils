"""
tests/test_inspector.py
"""

from unittest import TestCase
from inspector_mils.inspector import inspect


class TestInspectorMils(TestCase):
    """
    TestInspectorMils
    """

    @inspect
    def test_should_success(self):
        """
        test should success
        """

        self.assertIsInstance(self, TestInspectorMils)
        self.assertEqual(str(self), 'test_should_success (test_inspector.TestInspectorMils)')

    @inspect
    def test_should_fail(self):
        """
        test should success
        """

        self.assertIsInstance(self, TestInspectorMils)
        self.assertNotEqual(str(self), 'test_should_success (test_inspector.TestInspectorMils)')
