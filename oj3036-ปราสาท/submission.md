# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3036/ปราสาท
```

OJ submission ID, if submitted:

```text
558545
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
1-3 hours
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
From my understanding, first you received the number, and you need to calculate how many times you need to break the wall to get to room number 1 as wall break as low as possible. If the input is 1, you get 0 because you don't need to break the wall
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
My first plan is to calculate the floor that we are at by using the pattern that we are given every last number of each floor is an exponent of 2 so we calculate the floor by using while loop to get the floor number if number is > the last floor number, we add the floor number. After we get the floor number, next we calculate the position of the number we are given by using the number that we are given minus the last number of the 1 lower floor that we are in and then we calculate how many time we need to break the wall by using the position and floor that we are in at the moment if the position is mod with 2 and return 0 we add the wall break by 1 minus row by 1 and the position by 1 if the position mod with 2 did not return 0 we add the wall break by 2 minus row  by 1 and the position that we are at right now minus by two but if the position minus by two and we get negative number the position is 1 and if the row is 0 then we print out the number of wall break
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
First, I received a number input as an integer, and we assign floor as 0, we calculate the floor by using while loop if number > (i+1)**2, we add 1 to i next we calculate the position by using number - i**2 that gonna give us the current position of the floor we are at. Then, we assign cost as 0 that gonna count how many time we need to break the wall to get to the room number 1 and we assign row = i and now we calculate the wall break using while loop if row > 0 we continue to next if p%2 == 0 we add the cost by 1 minus row by 1 and minus p by 1 if p%2 did not return 0 we add the cost by 2 minus row by 1 and assign p to max(p-2, 1) that help to check if p is negative or not after row hit 0 we print(cost)
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
I use this test case to check whether the math in this code works as intended or not
```

Input:

```text
100
```

Expected output:

```text
18
```

Actual output:

```text
18
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
I use this test case to check whether the math in this code works as intended or not
```

Input:

```text
1
```

Expected output:

```text
0
```

Actual output:

```text
0
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
I use this test case to check whether the math in this code works as intended or not
```

Input:

```text
67
```

Expected output:

```text
16
```

Actual output:

```text
16
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
