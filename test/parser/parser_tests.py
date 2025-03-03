import unittest
from source.parser.parser import Parser
from source.parser.parser import InvalidTimeFormat


class TestParseTimestamp(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_timestamp_00_00(self):
        expected = (0, 0)
        actual = self.parser.parse_timestamp("00:00")
        self.assertEqual(expected, actual)

    def test_parse_timestamp_05_59(self):
        expected = (5, 59)
        actual = self.parser.parse_timestamp("05:59")
        self.assertEqual(expected, actual)

    def test_parse_timestamp_23_59(self):
        expected = (23, 59)
        actual = self.parser.parse_timestamp("  23:59     ")
        self.assertEqual(expected, actual)

    def test_parse_error_not_long_enough(self):
        with self.assertRaises(InvalidTimeFormat) as error:
            self.parser.parse_timestamp("00")

        exception = error.exception
        self.assertEqual(exception.position_in_string, 0)

    def test_parse_error_random_input(self):
        with self.assertRaises(InvalidTimeFormat) as error:
            self.parser.parse_timestamp("asdav")

        exception = error.exception
        self.assertEqual(exception.position_in_string, 0)

    def test_parse_error_missing_colon(self):
        with self.assertRaises(InvalidTimeFormat) as error:
            self.parser.parse_timestamp("00 00")

        exception = error.exception
        self.assertEqual(exception.position_in_string, 2)

    def test_parse_error_invalid_hour(self):
        with self.assertRaises(InvalidTimeFormat) as error:
            self.parser.parse_timestamp("0h:00")

        exception = error.exception
        self.assertEqual(exception.position_in_string, 0)

    def test_parse_error_invalid_minute(self):
        with self.assertRaises(InvalidTimeFormat) as error:
            self.parser.parse_timestamp("00:mm")

        exception = error.exception
        self.assertEqual(exception.position_in_string, 3)


class TestScanSwedishWords(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_swedish_word_to_integer(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        input = ["ett", "två", "tre", "fyra", "fem", "sex",
                 "sju", "åtta", "nio", "tio", "elva", "tolv"]

        for i, word in enumerate(input, 0):
            actual = self.parser.swedish_number_to_int(word)
            self.assertEqual(actual, expected[i])


class TestValidateUserInput(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_validate_correct(self):
        self.assertTrue(self.parser.validate_answer_phrase(
            " HALV     Åtta ", "halv åtta"))

    def test_validate_incorrect(self):
        self.assertFalse(self.parser.validate_answer_phrase(
            " kvart tiLL nio ", "kvart i nio"))


if __name__ == '__main__':
    unittest.main()
