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

        # initialize counters for absences and consecutive late days
        absence_count = 0
        late_streak = 0

        # iterate through each character in the string
        for char in s:
            if char == 'A':
                absence_count += 1
            if char == 'L':
                late_streak += 1
                # return false if late count is more than 2
                if late_streak > 2:
                    return False
            else:
                # reset late streak if character is not 'L' - check consecutive late days
                late_streak = 0
            # return false if absence count is more than 1
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

