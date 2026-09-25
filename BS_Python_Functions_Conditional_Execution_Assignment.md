# Assignment: Functions and Conditional Execution in Python

**Course:** Introduction to Programming with Python\
**Level:** BS (Undergraduate)\
**Duration:** 40--50 Minutes\
**Marks:** 20

## Instructions

1.  Attempt all questions.
2.  Write clean and properly indented Python code.
3.  Use functions wherever required.
4.  Use conditional execution (`if`, `elif`, `else`) appropriately.
5.  Do not use AI-generated or copied code without understanding it.

## Question 1 --- Basic Function (4 Marks)

Create a function named `check_even_odd()` that:

-   takes one integer as input,
-   returns `"Even"` if the number is even,
-   otherwise returns `"Odd"`.

### Sample Input

``` python
7
```

### Expected Output

``` text
Odd
```

## Question 2 --- Grade Calculator Using Functions (6 Marks)

Write a function named `calculate_grade()` that:

-   accepts marks (0--100),
-   returns grade according to the following conditions:

  Marks          Grade
  -------------- -------
  80 and above   A
  70--79         B
  60--69         C
  50--59         D
  Below 50       Fail

### Requirements

-   Use `if-elif-else`.
-   Call the function using user input.
-   Display the returned grade.

## Question 3 --- Temperature Decision System (5 Marks)

Create a function named `weather_advice()` that:

-   accepts temperature as input,
-   gives advice according to the following rules:

  Temperature   Message
  ------------- ---------------------
  Above 35      Stay hydrated
  25--35        Weather is pleasant
  Below 25      It may feel cold

### Example

``` text
Input: 38
Output: Stay hydrated
```

## Question 4 --- Debugging Question (5 Marks)

The following program contains logical and syntax mistakes. Identify and
correct the errors.

``` python
def compare(a,b)
    if a > b:
    print("A is greater")
    else
        print("B is greater")

compare(10,5)
```

### Requirements

1.  Rewrite the corrected code.
2.  Briefly explain the mistakes.

## Bonus Challenge (Optional)

Create a function named `login_system()` that:

-   asks for username and password,
-   prints `"Login Successful"` if:
    -   username = `"admin"`
    -   password = `"python123"`
-   otherwise prints `"Invalid Credentials"`.

## Submission Guidelines

-   Submit a `.py` file.
-   File name format:

``` text
YourName_Functions_Assignment.py
```

-   Late submissions may receive deduction in marks.
