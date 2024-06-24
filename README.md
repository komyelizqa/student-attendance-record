# Student Attendance Record

## Business Model

**Application Description:**
The business application is designed for teachers and students to check a student's eligibility for an attendance award. The eligibility criteria are based on the student's attendance record represented by a string.

### Eligibility Criteria
1. **Absences ('A')**: The student must have fewer than 2 absences in total.
2. **Lateness ('L')**: The student must not have been late for 3 or more consecutive days.

### Handling Various Cases:

Although we have the condition "The record only contains the following three characters:",
we still handle exceptions to ensure robustness in case of unexpected input or data corruption. Also we uppercase letters in case of human error.

We don't want to make assumptions about student's eligibility, so if we have empty string or symbols, we don't know if student meets creterias for award or not. Therefore, we need to make a data verification.


1. **Empty String**:
   - If the attendance string `s` is empty, the student's eligibility cannot be determined due to the absence of data. The function will throw an `EmptyStringException` with the message "The data is empty, please check the string again."

2. **String Contains Symbols**:
   - If the attendance string `s` contains any characters other than 'A', 'L', or 'P', it is considered invalid, and the function will throw an `InvalidStringException` with the message "The data is invalid, please check the string again."

### Code Approach

**1. Solution using Loop:**

Although after first reading of the task, my first thought about solution was to make a loop with two conditions, but after some time I decided to move without it, so my first solutions is the next one:

```python

def if_student_gets_award(self, s):
        size = len(s)

        if s.replace("A", "").count('') <= size - 2 or "LLL" in s:
            return False

        return True

Although the method looks short and simp[le, it expected to be slower due to multiple passes over the string and additional memory operations. Cheking long strings with more than 100 characters, the timing was higher than the one from loop solution, and loop solution could be easier readable and understandable for other team members. Therefore, I decided to keep the approach with loop and conditions. For 'A' and 'L' characters we create counters which we can check later for eligibility criteria. 


