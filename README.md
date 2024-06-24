# Student Attendance Record

You are given a string s representing an attendance record for a student where each character signifies
whether the student was absent, late, or present on that day. The record only contains the following three
characters:
&#39;A&#39;: Absent.
&#39;L&#39;: Late.
&#39;P&#39;: Present.
The student is eligible for an attendance award if they meet both of the following criteria:
The student was absent (&#39;A&#39;) for strictly fewer than 2 days total.
The student was never late (&#39;L&#39;) for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

Example 1:
Input: s = &quot;PPALLP&quot;
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example 2:
Input: s = &quot; PPALLL&quot;
Output: false

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

**1. Solution using only one condition:**

Although my initial approach to the task involved creating a loop with two conditions, I later decided to explore alternative solutions. The following is one of the solutions I considered:

```python

def if_student_gets_award(self, s):
        size = len(s)

        if s.replace("A", "").count('') <= size - 2 or "LLL" in s:
            return False

        return True
```

Although the method appears concise and straightforward, it is anticipated to be less efficient due to multiple passes over the string and the associated memory operations. Performance testing with long strings exceeding 100 characters demonstrated higher execution times compared to the loop-based solution. Additionally, the loop-based approach is likely to be more readable and comprehensible for other team members. Consequently, I opted to retain the loop and condition-based approach. This method involves creating counters for 'A' and 'L' characters to evaluate eligibility criteria effectively.

**2. Solution using loop:**

In this solution, the if_student_gets_award method is designed to determine if a student is eligible for an attendance award based on their attendance record. The method processes the input string s to check two conditions: the student was absent fewer than 2 days in total, and the student was never late for 3 or more consecutive days.

Steps:
Convert to Uppercase:

The input string s is converted to uppercase to ensure consistency and handle potential human error in data entry.
Empty String Check:

The method raises an EmptyStringException if the input string s is empty, as it cannot determine eligibility from an empty record.
Invalid Character Check:

The method raises an InvalidStringException if the input string contains any characters other than 'A', 'L', or 'P', ensuring data integrity.
Initialize Counters:

Right after that we are checking The student was never late (&#39;L&#39;) for 3 or more consecutive days condition - if String s contains substring "LLL", then the counter, absence_count is initialized to keep track of the number of absences.
Iterate through characters.
Return result.

If neither condition for ineligibility is met, the method returns True, indicating the student is eligible for the award. This approach ensures robustness by checking for empty strings and invalid characters, enhances readability through clear structure and comments, maintains efficiency by processing the string in a single pass, and improves error handling by raising exceptions for invalid input.
