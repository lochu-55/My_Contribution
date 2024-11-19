import warnings
import unittest

def example_warning():
    warnings.warn("This is a warning", UserWarning)

class TestWarnings(unittest.TestCase):
    def test_warning(self):
        with self.assertWarns(UserWarning):
            example_warning()

    def test_warning_message(self):
        with self.assertWarnsRegex(UserWarning, "warning"):
            example_warning()


if __name__ == "__main__":
    unittest.main(verbosity=2)
