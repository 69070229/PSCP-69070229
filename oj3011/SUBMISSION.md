# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3011/Colors
```

OJ submission ID, if submitted:

```text
542082
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
15-30 minutes
```
---

## 2. My Understanding

```text
From my understanding. You recived two input as a primary color Red, Yellow and Blue. When you mix red with yellow you'll recived orange color. When you mix red with blue you'll recived violet color. And lastly when you mix yellow with blue you'll recived green. If the color you recived is wrong or cannot be mix you need to return "Error" or if you mix the same color in primary color you'll recived the same color as you mix.
```

---

## 3. My First Plan

```text
Step 1: First you need to recived 2 color as the problem said so I use input() to recived the color

Step 2: After that I create a list of primary color and a list of the color I recived in Step 1.

Step 3: Then we check the color by check if color1 is in the primary color or not if not print out Error same as color 2.

Step 4: If the color is in the primary color then we check if color1 and color2 is the same color if yes then print out color1. It doesn't matter if you print out color1 or color2 by this point the color is the same.

Step 5: If there is no red in color list that's mean the only color left is yellow and blue. Which mean we get the color Green. same repeat for other conditions.
```

---

## 4. My Final Approach

```text
I use input() to recived both color. And create a list of primary color. And a color list that I recived. And then I use condition to compare if color1 is in primary color list or not, or if color2 is in primary color or not. If not then we print out Error. If the color is in primary color list we pass on to the next condition. If color1 and color2 is the same we print out color1. Else if the color red is not in the color list that's mean the only color left is yellow and blue. Which mean we get the color Green. Else if the color yellow is not in the color list that's mean the only color left is red and blue. Which mean we get the color Violet. Else if the color blue is not in the color list that's mean the only color left is red and yellow. Which mean we get the color Orange. 
```

---

## 5. My Tests

### Test Case 1

Why I chose this case:

```text
To check if the color condition is working correctly or not
```

Input:

```text
Red
Blue
```

Expected output:

```text
Violet
```

Actual output:

```text
Violet
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
To check if the output gonna be Error or not cause by color not in primary color
```

Input:

```text
Black
Red
```

Expected output:

```text
Error
```

Actual output:

```text
Error
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
To check if color1 and color2 is the same the result will be the same as given color
```

Input:

```text
Red
Red
```

Expected output:

```text
Red
```

Actual output:

```text
Red
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
