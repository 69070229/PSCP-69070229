# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3477/PadThai
```

OJ submission ID, if submitted:

```text
658501
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
I play a cook making Pad Thai for a chef, and the chef has a fixed list of 11 allowed ingredients. I read ingredient names one per line until I see "Cook", and then I read flavors one per line until I see "End". The chef answers with one sentence depending on what I made. If I used any ingredient that is not on the list, the chef says "This is not Pad Thai!!!", and it does not matter whether the real ingredients are complete or what the flavors are. If every ingredient I used is allowed but some of the 11 are missing, the chef says "This is bad!" and ignores the flavors. If the ingredients are complete but the flavors are not exactly Sweet, Sour and Salty (one is missing, or there is an extra one like Bitter), the chef says "Not Bad...". If both the ingredients and the flavors are complete, the chef says "Delicious!". Repeated lines do not matter, as the second sample shows.
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
At first I thought about keeping the ingredients in a list and checking each of the 11 allowed ones with "in", then counting how many I found. For the not-Pad-Thai case I would loop over what I got and check every item against the allowed list. The problem is that repeated ingredients, like Tofu twice, would mess up my count, so I would have to handle duplicates by hand, and that felt messy.
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
I use sets for everything, because the order and the repeats do not matter, only which items appear. I make a set called allowed_ingredients with the 11 names and a set called required_flavors with Sweet, Sour and Salty. Then I read the ingredients into one set with a while True loop that stops at "Cook", and read the flavors into another set with a loop that stops at "End". Adding to a set ignores repeats, so I do not have to do anything extra about them. After that I check the cases in the order the problem wants, using if and elif. First, if the ingredient set is not a subset of allowed_ingredients, there is at least one outside ingredient, so I print "This is not Pad Thai!!!", and I check this first because it beats everything else. Second, if the ingredient set is not equal to allowed_ingredients, then everything is allowed but some are missing, so I print "This is bad!". Third, if the flavor set is not equal to required_flavors, I print "Not Bad...", and using equal instead of subset also catches an extra flavor like Bitter. Otherwise I print "Delicious!". Everything is an exact match, so the names are case sensitive and have to be typed exactly like in the problem.
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
Chicken
Cook
Sweet
Sour
Salty
End
```

Expected output:

```text
This is not Pad Thai!!!
```

Actual output:

```text
This is not Pad Thai!!!
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
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Peanuts
Cook
End
```

Expected output:

```text
Not Bad...
```

Actual output:

```text
Not Bad...
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
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Peanuts
Cook
Sweet
Sour
Salty
Spicy
Sweet
End
```

Expected output:

```text
Not Bad...
```

Actual output:

```text
Not Bad...
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
