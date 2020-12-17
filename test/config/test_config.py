import unittest

from  tomlconfig.tomlutils import TomlParser

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = TomlParser('influxdb.toml')

    def test_parser(self):
        # test_int = self.parser.get('test_int', 0)
        # test_str = self.parser.get('test_str', "str")
        # test_float = self.parser.get('test_float', 1.23)
        # test_bool = self.parser.get('test_bool', False)
        # test_list = self.parser.get('test_list', [])
        test_nested_1 = self.parser.get(['influxdb', 'test', 'abc'], '0')
        print(test_nested_1)
        test_nested_2 = self.parser.get('influxdb.test.abc', '0')
        print(test_nested_2)
        # self.assertNotEqual(toml_str, None)

if __name__ == '__main__':
    unittest.main()
