# Student Attendance Record

## Business Model

**Application Description:**
The business application is designed for teachers and students to check a student's eligibility for an attendance award. The eligibility criteria are based on the student's attendance record represented by a string.

### Eligibility Criteria
1. **Absences ('A')**: The student must have fewer than 2 absences in total.
2. **Lateness ('L')**: The student must not have been late for 3 or more consecutive days.

### Handling Various Cases:

Although the condition states, "The record only contains the following three characters," we still handle exceptions to ensure robustness against unexpected input or data corruption. Additionally, we convert letters to uppercase to account for potential human error.

We avoid making assumptions about a student's eligibility. If the string is empty or contains invalid symbols, we cannot determine if the student meets the criteria for the award. Therefore, we incorporate data verification to maintain accuracy and reliability.


1. **Empty String**:
   - If the attendance string `s` is empty, the student's eligibility cannot be determined due to the absence of data. The function will throw an `EmptyStringException` with the message "The data is empty, please check the string again."

2. **String Contains Symbols**:
   - If the attendance string `s` contains any characters other than 'A', 'L', or 'P', it is considered invalid, and the function will throw an `InvalidStringException` with the message "The data is invalid, please check the string again."

### Code Approach

**1. Solution using Loop:**

Although my initial approach to the task involved creating a loop with two conditions, I later decided to explore alternative solutions. The following is one of the solutions I considered:

```python

def if_student_gets_award(self, s):
        size = len(s)

        if s.replace("A", "").count('') <= size - 2 or "LLL" in s:
            return False

        return True
```

Although the method appears concise and straightforward, it is anticipated to be less efficient due to multiple passes over the string and the associated memory operations. Performance testing with long strings exceeding 100 characters demonstrated higher execution times compared to the loop-based solution. Additionally, the loop-based approach is likely to be more readable and comprehensible for other team members. Consequently, I opted to retain the loop and condition-based approach. This method involves creating counters for 'A' and 'L' characters to evaluate eligibility criteria effectively.


