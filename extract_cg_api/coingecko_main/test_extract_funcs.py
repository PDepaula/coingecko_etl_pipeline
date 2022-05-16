import unittest
import undo_pagination as up

class TestExtractFuncs(unittest.TestCase):

    def test_undo_pagination(self):
        result = up.undo_pagination()
        self.assertIsNotNone(up.scp_json)
        self.assertIsNotNone(up.meme_json)
        self.assertIsNotNone(up.gamefi_json)
