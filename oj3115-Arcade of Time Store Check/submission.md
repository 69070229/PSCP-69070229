# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3115/Arcade of Time: Store Check
```

OJ submission ID, if submitted:

```text
580523
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
3-6 hours
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
From my understanding, first you receive the number of arcade games and the time that you need to calculate how many arcade are open at that time
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
My first plan is to make an array of 1441 slots for every minute of the day, all starting at 0, and then loop through each store to read its start and stop time. For each store I loop from start to stop-1 and add 1 to every one of those minutes, so the store gets counted in each minute it’s open, and I stop before stop because the store is already closed at that minute. After all the stores are done, the array already knows how many stores are open at any minute, so I just read the check times and print out the value at each one.
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
We receive the input of the number of stores and the number of check times as integers, and then we use a for loop in the range of the store amount to get each store’s start and stop time as integers. Then, instead of adding 1 to every minute the store is open, we only mark the two points where the count changes by doing diff[start] += 1 and diff[stop] -= 1, so each store only costs 2 operations. After that, we loop from minute 0 to 1440 keeping a running total and store it back into the array, which turns those changes into the actual number of open stores at each minute. Subtracting at stop instead of stop + 1 is what makes the store count as closed at that exact minute. Then we read the check times as a list of integers and print the value at each one out, joined into a single line with " ".join(str(diff[k]) for k in time)
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
I use this test case to check whether my code work as intended or not
```

Input:

```text
2 6
100 200
200 300
99 100 199 200 299 300
```

Expected output:

```text
0 1 1 1 1 0
```

Actual output:

```text
0 1 1 1 1 0
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
I use this test case to check whether my code works as intended or not
```

Input:

```text
4 5
0 1440
0 1
500 501
1439 1440
0 1 500 1439 1440
```

Expected output:

```text
2 1 2 2 0
```

Actual output:

```text
2 1 2 2 0
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
I use this test case to check whether my code work as intended or not
```

Input:

```text
3 7
600 700
650 750
1000 1100
600 650 700 749 750 800 1050
```

Expected output:

```text
1 2 1 1 0 0 1
```

Actual output:

```text
1 2 1 1 0 0 1
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text

```

What did they help with?

```text

```

What did you still do by yourself?

```text

```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
