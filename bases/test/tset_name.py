import unittest
from name import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """name.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""

        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main() 
                                                                                                                                                                                                                                                                            import 'Janis Joplin') unittest.main()
