import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    def test1(self):
        pw = ''
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))


if __name__ == '__main__':
    unittest.main()
