import re


class InvalidTimeFormat(Exception):
    def __init__(self, position_in_string: int, reason: str):
        self.position_in_string = position_in_string
        self.reason = reason

    def __str__(self):
        return repr(f"The parse failed at index {self.position_in_string} due to the following reason: {self.reason}.")


class Parser:
    def parse_timestamp(self, input: str) -> tuple[int, int]:
        """
        Validate that input matches the 24-hour clock time format HH:MM, 
        where HH and MM are digit combinations within the range 00-23 and 
        00-59, respectively. String that begin or end with whitespace but 
        still follow the format (for example " 00:23  ") are also accepted. 

        Exceptions:
            Raises an exception (of the base class Exception) if the input does not match the format. 

        Returns:
            A pair of integers representing the hour of the day and minute of the hour, respectively. 
        """
        input = input.strip()

        if len(input) != 5:
            raise InvalidTimeFormat(0, "the input is too long")

        hour_RE = re.compile("(00)|([0-1][0-9])|(2[0-3])")
        hour = 0

        if hour_RE.match(input, 0, 2) == None:
            raise InvalidTimeFormat(0, "no valid 2-digit hour found")
        else:
            hour = int(input[0:2])

        minute_RE = re.compile("[0-5][0-9]")
        minute = 0

        if input.find(":") == -1:
            raise InvalidTimeFormat(2, "no colon found")

        if minute_RE.match(input, 3, 5) == None:
            raise InvalidTimeFormat(3, "no valid 2-digit minute found")
        else:
            minute = int(input[3:5])

        return (hour, minute)

    def swedish_number_to_int(self, input: str) -> int:
        words = ["ett", "två", "tre", "fyra", "fem", "sex", "sju",
                 "åtta", "nio", "tio", "elva", "tolv"]

        try:
            integer_representation = words.index(input) + 1
            return integer_representation
        except ValueError:
            return -1

    def validate_answer_phrase(self, user_answer: str, correct_answer: str) -> bool:
        """
        Test if user_answer matches correct answer. The test is not
        case sensitive and words can be separated by sequences of 
        whitespace (multiple spaces for example).

        Exceptions:
            None 

        Returns:
            True if user_answer matches correct_answer. 
        """

        user_words = user_answer.strip().lower().split()
        correct_words = correct_answer.strip().lower().split()

        if len(user_words) != len(correct_words):
            return False

        for words in zip(user_words, correct_words):
            if words[0] != words[1]:
                return False

        return True
