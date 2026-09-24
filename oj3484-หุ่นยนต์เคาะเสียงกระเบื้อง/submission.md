# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3484/หุ่นยนต์เคาะเสียงกระเบื้อง
```

OJ submission ID, if submitted:

```text
658530
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
A robot taps each tile at 5 spots, and for every tile in an N by N area I get a number from 0 to 5 telling how many spots sounded bad. The first line gives N and a fine P per bad spot, which can be a decimal. Then N lines follow, each with N numbers. I need to print a report. For each row, I print the row's own numbers, then how many tiles in that row have at least one bad spot, then the total bad spots in that row. After the rows, I print one line with the number of bad tiles in each column, and one line with the number of bad spots in each column. The last line has the total number of bad tiles, the total number of bad spots, and the total fine, which is total bad spots times P, shown with 2 decimal places.
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
At first I thought about making several separate loops, one for the row results, one for the column results and one for the totals, and reading the input again in each one. That felt wrong, because I can only read the input once. I also wasn't sure whether to count a tile as bad by its number or by adding up the spots, since those are two different things: a tile with 4 bad spots is still only one bad tile.
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
I read N and P from the first line, turning N into an integer and P into a float, because the fine can be a decimal. Then I read the whole grid once into a list of lists using a list comprehension, so I can loop over it as many times as I need. The main thing to keep straight is the difference between bad tiles and bad spots. A tile is bad when its value is more than 0, so it adds 1 to the tile count. The value itself is the number of bad spots, so it is added to the spot count. I go through the grid row by row. For each row I count the tiles with value more than 0, and I add up all the values. I add these to the running totals total_tiles and total_points. Then I print the row with two more numbers on the end, the tile count and the spot count, joined by spaces. After the rows, I make two lists of N zeros called column_tiles and column_points. I loop over the grid again, and for each value I add to the matching column, again counting 1 for a tile with value more than 0 and adding the value itself for the spots. I print each of those lists on its own line. For the last line, the fine is total_points times P. I print the total tiles, the total points and the fine with an f-string using :.2f, so it always shows exactly 2 decimal places, even when the fine is 0.
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
I use this test case to check whether my code works as intended or not
```

Input:

```text
2 10
5 5
5 5
```

Expected output:

```text
5 5 2 10
5 5 2 10
2 2
10 10
4 20 200.00
```

Actual output:

```text
5 5 2 10
5 5 2 10
2 2
10 10
4 20 200.00
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
3 1.5
0 0 0
0 4 0
0 0 0
```

Expected output:

```text
0 0 0 0 0
0 4 0 1 4
0 0 0 0 0
0 1 0
0 4 0
1 4 6.00
```

Actual output:

```text
0 0 0 0 0
0 4 0 1 4
0 0 0 0 0
0 1 0
0 4 0
1 4 6.00
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
I use this test case to check whether my code works as intended or not
```

Input:

```text
3 200
1 0 0
0 2 0
0 0 3
```

Expected output:

```text
1 0 0 1 1
0 2 0 1 2
0 0 3 1 3
1 1 1
1 2 3
3 6 1200.00
```

Actual output:

```text
1 0 0 1 1
0 2 0 1 2
0 0 3 1 3
1 1 1
1 2 3
3 6 1200.00
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
