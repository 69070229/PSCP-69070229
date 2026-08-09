# Problem Solving Submission
## 1. OJ Information

OJ problem number/title:

```text
2996/สลับตัวอักษร
```

OJ submission ID, if submitted:

```text
542044
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
0-15 minutes
```

---

## 2. My Understanding

```text
From my understanding. First you recived a string with 5 character length. And then you need to print out the string you recived backword and lowercase.
```

---

## 3. My First Plan

```text
Step 1: First I start with reciving the input from the problem by using 
text = input() to recived the string value.

Step 2: Then I start to print the output as the problem said "backword and lowercase" using print(text[::-1].lower()) the [::-1] behind the text make the print function ran from the back to front and the .lower() in the end make all of the string lowercase.
```

---

## 4. My Final Approach

```text
As I explain in the topic 3. I use the Index slicing method to make the text backword by steping backword by -1 and .lower() to make it all lowercase
```

---

## 5. My Tests

### Test Case 1

Why I chose this case:

```text
To test if index is actually calling the string from the back to the front.
```

Input:

```text
thank
```

Expected output:

```text
knaht
```

Actual output:

```text
knaht
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
To test if .lower() actually making the string lowercase.
```

Input:

```text
Thank
```

Expected output:

```text
knahT
```

Actual output:

```text
knahT
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
To test if index is calling the string from the back to the front and make all the string lowercase.
```

Input:

```text
ThAnK
```

Expected output:

```text
KnAhT
```

Actual output:

```text
KnAhT
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

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

---

## 8. Student Declaration

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. |Yes|
| I understand my final code. |Yes |
| I recorded the real OJ status. |Yes |
| I did not copy AI-generated text directly into this file. |Yes |
| I did not copy code from another person. |Yes |
| If I received human help, I disclosed it in this file. |Yes |
| I submitted the final code to the OJ by myself. |Yes |
