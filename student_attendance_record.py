from exceptions import EmptyStringException, InvalidStringException


class StudentAttendanceRecord:

    def if_student_gets_award(self, s):
        s = s.upper()  # convert all characters to uppercase

        # raise an exception if the string is empty
        if not s:
            raise EmptyStringException()

        # raise an exception if the string contains invalid characters
        if any(char not in 'ALP' for char in s):
            raise InvalidStringException()

        # check condition with 3 or more days late
        if "LLL" in s:
            return False

        # initialize counters for absences
        absence_count = 0

        # iterate through each character in the string
        for char in s:
            if char == 'A':
                absence_count += 1
            # Return false if absence count is more than 1
            if absence_count > 1:
                return False
        # return true if both conditions are satisfied
        return True


if __name__ == "__main__":
    student_record = StudentAttendanceRecord()

    test_cases = ["PPALLP", "PPALLL", "AA", "PALLP", "ALPLL", "", "PPLLA!", "ppallallalll", "ppplppplpppl"]

    for test in test_cases:
        try:
            print(f"Testing '{test}': {student_record.if_student_gets_award(test)}")
        except (EmptyStringException, InvalidStringException) as e:
            print(f"Testing '{test}': {e}")

