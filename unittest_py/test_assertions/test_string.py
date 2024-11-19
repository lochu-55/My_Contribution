import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """Test that 'foo' is converted to 'FOO'."""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Test string case checking."""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Test string splitting."""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
