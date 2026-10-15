# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3538/B - Fully pair?
```

OJ submission ID, if submitted:

```text
680444
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
30-60 minutes
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
From my understanding, you receive one line of small english letters and each letter is one student, and students with the same letter get paired together, so you need to find which letters still have one student left with no pair and print them in the order they first show up from left to right, but if everyone has a pair you print fully paired
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
My first plan is to loop through every letter in the input and count how many times each letter appears by storing it in a dict. Then I loop through the dict and check if the count is odd, because if it is odd that means one student of that letter doesn't have a pair, so I add that letter to the answer. At the end if the answer is empty I print fully paired, if not I print the answer.
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
My final approach is the same as my first plan. First I receive the input with input().strip() and make an empty dict called counts. Then I loop through each letter in the text and do counts[letter] = counts.get(letter, 0) + 1, so if the letter is not in the dict yet it starts at 0 and then adds 1. After that I make an empty string result and loop through counts.items(), and if count % 2 == 1 I add the letter to result. Because the dict keeps the order that the letters were first added, the letters in result already come out in the order they first appear from left to right. At the end if result is not empty I print it, and if it is empty I print fully paired
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
I use this test case to check whether the code works as intended or not
```

Input:

```text
zyxzxw
```

Expected output:

```text
yw
```

Actual output:

```text
yw
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
I use this test case to check whether the code works as intended or not
```

Input:

```text
aaaaabbbb
```

Expected output:

```text
a
```

Actual output:

```text
a
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
I use this test case to check whether the code works as intended or not
```

Input:

```text
mnnmoopp
```

Expected output:

```text
fully paired
```

Actual output:

```text
fully paired
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
