import unittest
import checker


class TestChecker(unittest.TestCase):
    def test_example_input(self):
        """
        Test that it can process and validate input from file
        """
        checked_ibans = checker.check_input_file("test/test_input.txt")
        self.assertEqual(
            set(checked_ibans),
            set(
                [
                    ("BE68539007547034", "valid"),
                    ("GB29NWBK60161331926819", "valid"),
                    ("dsfgfdsg", "invalid"),
                    ("NL91ABNA0417164300GB29NWBK60161331926819", "invalid"),
                    ("XX89370400440532013000", "invalid"),
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
