import unittest
from Wiggle_Obj_UI import get_obj


class TestGetSelection(unittest.TestCase):

    def test_get_obj_from_selection_with_0_len(self):
        element = []
        with self.assertRaises(Exception):
            get_obj(element)

    def test_get_obj_from_selection_with_2_len(self):
        element = ["1", "2"]
        with self.assertRaises(Exception):
            get_obj(element)

    def test_get_obj_from_selection_with_1_len(self):
        element = ["whatever"]
        self.assertEqual(get_obj(element), element[0])
