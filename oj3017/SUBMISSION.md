# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3017/Bill
```

OJ submission ID, if submitted:

```text
542171
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
From my understanding. First we recived total amount of food and drink price from customer. After that we need to add 10% service fees on top of it. The minimum is 50 baht and the maximum is 1,000 baht. And lastly calculate Vat 7% on top of it and print out the result.
```

---

## 3. My First Plan

```text
Step 1: Recived total amount of food and drink price from customer using input()

Step 2: Calculate 10% service fees and then check if it's lower than minimum or higher than maximum or not. If it's lower then set the fees to 50 baht. If it's higher then set the fees to 1,000 baht. And then we add it up to total amount of food and drink price from customer.

Step 3: Calculate price and service fees 7% vat by multiply it all by 1.07 and then print out the result
```

---

## 4. My Final Approach

```text
I use int(input()) to recived total amount of food and drink price from customer. And then I calculate the service fees by using total amount of food and drink price from customer multiply by 0.1. And then we compare that to minimum and miximum service fees. If it's lower then set the fees to 50 baht. If it's higher then set the fees to 1,000 baht. And then price and service fees up. Lastly multiply price and service fees 7% vat by 1.07. and then we print out the final result.
```

---

## 5. My Tests

### Test Case 1

Why I chose this case:

```text
To see if the minimum service fees is apply or not
```

Input:

```text
90
```

Expected output:

```text
149.80
```

Actual output:

```text
149.80
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
To see if the maximum service fees is apply or not
```

Input:

```text
100000
```

Expected output:

```text
108070.00
```

Actual output:

```text
108070.00
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
To see if my calculation is correct as the problem said or not
```

Input:

```text
4000
```

Expected output:

```text
4708.00
```

Actual output:

```text
4708.00
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
| I wrote this submission in my own words. |Yes |
| I understand my final code. |Yes |
| I recorded the real OJ status. |Yes |
| I did not copy AI-generated text directly into this file. |Yes |
| I did not copy code from another person. |Yes |
| If I received human help, I disclosed it in this file. |Yes |
| I submitted the final code to the OJ by myself. |Yes |
