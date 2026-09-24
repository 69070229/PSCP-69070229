# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3357/Giraffe
```

OJ submission ID, if submitted:

```text
653329
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
15-30 minutes
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
So there are N giraffes standing in a row and each one has a neck height. A giraffe can eat in peace if its neck is taller than the one on its left AND taller than the one on its right. I need to count how many giraffes are like that. The tricky part is the two giraffes at the ends, since they only have one neighbor, so they only need to beat that one neighbor. The problem also says no two giraffes next to each other have the same height, so I don't have to worry about ties.
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
At first I just wanted to loop through every giraffe and compare it with the one on the left and the one on the right. The problem was that the first giraffe has nobody on its left and the last giraffe has nobody on its right, so heights[i - 1] and heights[i + 1] would go out of range (and i - 1 on the first one would wrongly wrap around to the last element in Python). My first idea was to write separate if cases for the first giraffe, the last giraffe, and all the ones in the middle, but that looked really long and messy.
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
Instead of three separate cases, I kept one loop and made the check for each side a simple true/false thing. For the left side, it's fine if i is 0 (no left neighbor) or if the giraffe is taller than the one before it. For the right side, it's fine if i is the last index (no right neighbor) or if the giraffe is taller than the one after it. Because Python stops checking as soon as the first part of an "or" is true, it never reaches the out-of-range index. If both sides are fine, I add 1 to the count. At the end I print the count. It only goes through the list once so it's way fast enough for N up to 100.
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
1 5 2 4 3 20 7 9 6
```

Expected output:

```text
4
```

Actual output:

```text
4
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
I use this test case to check whether my code work as intended or not
```

Input:

```text
5 4 6 9 7 3
```

Expected output:

```text
2
```

Actual output:

```text
2
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
7
```

Expected output:

```text
1
```

Actual output:

```text
1
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
