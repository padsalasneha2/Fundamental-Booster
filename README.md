# 🧑‍💻 Interactive Personal Data Collector

## 📌 Project Overview

**Interactive Personal Data Collector** is a beginner-friendly Python program that collects basic personal information from the user and displays the entered data along with its **data type** and **memory address**.

The program also calculates the user's **approximate birth year** based on the entered age.

This project is created for **learning and practicing Python fundamentals** such as:

* `input()`
* `print()`
* Variables
* Data Types
* Type Conversion
* `type()`
* `id()`
* Arithmetic Operators
* String formatting and output
* User interaction

---

## 🎯 Objective of the Project

The main objective of this project is to understand how Python can:

1. Take information from the user.
2. Store information in variables.
3. Convert input data into different data types.
4. Display the data entered by the user.
5. Find the data type of variables using `type()`.
6. Find the memory identity of objects using `id()`.
7. Perform calculations using arithmetic operators.
8. Create a simple interactive command-line application.

---

## ✨ Features

This program provides the following features:

### 1. 👤 Name Collection

The program asks the user to enter their name.

```python
name = input("please enter your name: ")
```

The name is stored as a **string (`str`)**.

---

### 2. 🎂 Age Collection

The program asks the user to enter their age.

```python
age = int(input("please enter your age: "))
```

The `input()` function normally returns data as a string, so `int()` is used to convert it into an integer.

Example:

```text
25
```

is converted from:

```text
"25"
```

to:

```text
25
```

---

### 3. 📏 Height Collection

The program collects the user's height in meters.

```python
height = float(input("please enter your height in meters: "))
```

The `float()` function converts the input into a decimal number.

Example:

```text
1.65
```

---

### 4. 🔢 Favorite Number

The program asks the user for their favorite number.

```python
favorite_number = int(input("please enter your favorite number: "))
```

The entered value is converted into an integer using `int()`.

---

## 🧠 Python Concepts Used

| Concept      | Used For                                                    |
| ------------ | ----------------------------------------------------------- |
| `print()`    | Displaying messages                                         |
| `input()`    | Taking input from the user                                  |
| `int()`      | Converting input into integer                               |
| `float()`    | Converting input into decimal number                        |
| `str`        | Storing text such as name                                   |
| `type()`     | Checking the data type                                      |
| `id()`       | Getting the identity/memory-related identifier of an object |
| Variables    | Storing user information                                    |
| `-` operator | Calculating birth year                                      |
| Comments     | Explaining code                                             |

---

# 🔍 Detailed Code Explanation

## Step 1: Welcome Message

```python
print("welcome to the intrective personal data collecter")
print()
```

### Explanation:

`print()` is used to display text on the screen.

The second:

```python
print()
```

prints a blank line to make the output easier to read.

---

## Step 2: Taking User's Name

```python
name = input("please enter your name: ")
```

### Explanation:

* `input()` takes information from the user.
* The entered name is stored in the variable `name`.
* By default, `input()` returns a **string**.

For example:

```text
please enter your name: Sneha
```

The value stored is:

```python
name = "Sneha"
```

---

## Step 3: Taking Age

```python
age = int(input("please enter your age: "))
```

### Explanation:

Here two functions are used:

```python
input()
```

takes input from the user.

Then:

```python
int()
```

converts the input into an integer.

For example:

```text
please enter your age: 20
```

The value becomes:

```python
age = 20
```

---

## Step 4: Taking Height

```python
height = float(input("please enter your height in meters: "))
```

### Explanation:

`float()` is used when we need to store decimal values.

Example:

```text
please enter your height in meters: 1.65
```

The value becomes:

```python
height = 1.65
```

Its data type is:

```python
float
```

---

## Step 5: Taking Favorite Number

```python
favorite_number = int(input("please enter your favorite number: "))
```

The favorite number is converted into an integer using `int()`.

Example:

```text
please enter your favorite number: 7
```

The value stored is:

```python
favorite_number = 7
```

---

# 📋 Displaying Collected Information

After collecting the information, the program displays a thank-you message.

```python
print("thank you for providing your information!")
```

Then it displays each variable.

---

## 🔤 Using `type()`

Example:

```python
type(name)
```

The `type()` function tells us what type of data is stored in a variable.

Examples:

```python
type(name)
```

Output:

```text
<class 'str'>
```

For age:

```python
type(age)
```

Output:

```text
<class 'int'>
```

For height:

```python
type(height)
```

Output:

```text
<class 'float'>
```

---

## 🧠 Using `id()`

Example:

```python
id(name)
```

The `id()` function returns the identity of the Python object.

Example:

```python
id(age)
```

It may return a number such as:

```text
140712345678912
```

### Important:

The value returned by `id()` can be different each time the program runs.

It is mainly useful for understanding **object identity and memory-related concepts in Python**.

---

# 🎂 Calculating Birth Year

The program uses:

```python
birth_year = 2026 - age
```

This calculates an **approximate birth year** based only on the entered age.

For example:

```text
Age = 20
```

Calculation:

```text
2026 - 20 = 2006
```

Therefore:

```text
Your birth year is approximately: 2006
```

### ⚠️ Note

This is only an approximate calculation because the exact birth year depends on whether the user's birthday has already occurred in 2026.

---

# 🖥️ Sample Output

```text
welcome to the intrective personal data collecter

please enter your name: Sneha
please enter your age: 20
please enter your height in meters: 1.65
please enter your favorite number: 7

thank you for providing your information!

name:  Sneha (type:  <class 'str'> , memory address:  140712345678912 )
age:  20 (type:  <class 'int'> , memory address:  140712345679232 )
height:  1.65 (type:  <class 'float'> , memory address:  140712345679360 )
favorite number:  7 (type:  <class 'int'> , memory address:  140712345679488 )

Your birth year is approximately: 2006 (based on your age of 20 )

Thank you for using the Personal Data Collector. Goodbye!
```

> **Note:** The `id()` values in the output are examples. They can change when the program runs.

---

# 🗂️ Data Types Used

The program demonstrates three important Python data types:

## 1. String (`str`)

Used for the user's name.

```python
name = "Sneha"
```

---

## 2. Integer (`int`)

Used for age and favorite number.

```python
age = 20
favorite_number = 7
```

---

## 3. Float (`float`)

Used for height.

```python
height = 1.65
```

---

# 🔄 Type Conversion

The program demonstrates type conversion using:

### `int()`

Converts a value into an integer.

```python
age = int(input())
```

### `float()`

Converts a value into a floating-point number.

```python
height = float(input())
```

This is important because values received from `input()` are initially strings.

---

# 📚 Learning Outcomes

After completing this project, a beginner can understand:

* How to create variables in Python.
* How to take user input.
* How `input()` works.
* How to convert strings into integers.
* How to convert strings into floating-point numbers.
* Difference between `str`, `int`, and `float`.
* How to use `type()`.
* How to use `id()`.
* How arithmetic operations work.
* How to create an interactive command-line program.
* How Python stores information in variables.

---

# ▶️ How to Run the Project

## Step 1: Install Python

Make sure Python is installed on your computer.

Check Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Open the Project Folder

Open the folder containing your Python file.

For example:

```text
Personal-Data-Collector
```

---

## Step 3: Open Terminal

Open Command Prompt or PowerShell inside the project folder.

---

## Step 4: Run the Program

If your Python file is named:

```text
personal_data.py
```

run:

```bash
python personal_data.py
```

---

# 📁 Project Structure

```text
Personal-Data-Collector/
│
├── personal_data.py
│
└── README.md
```

### `personal_data.py`

Contains the main Python program.

### `README.md`

Contains project information, features, explanation, instructions, and learning outcomes.

---

# 🛠️ Technologies Used

* **Programming Language:** Python
* **Application Type:** Command-Line Application
* **Level:** Beginner
* **Purpose:** Learning / Practice

---

# 🎓 Project Level

**Beginner Python Project**

This project is suitable for students who are learning Python fundamentals and want to practice:

```text
Input → Variables → Data Types → Type Conversion → Output → Calculation
```

---

# 🚀 Possible Future Improvements

This project can be extended with more features, such as:

* Email collection
* Phone number collection
* Gender selection
* Address collection
* Exact date of birth
* BMI calculation
* Age calculation from date of birth
* Input validation
* Error handling using `try-except`
* Saving user information into a file
* Creating a graphical user interface using Tkinter
* Storing information in a database

---

# 👩‍💻 Author

**Sneha Padsala**

### Project Purpose

This project is created for **educational and learning purposes** to practice Python programming fundamentals.

---

## ⭐ Conclusion

The **Interactive Personal Data Collector** is a simple Python project that demonstrates how Python can interact with users, collect information, work with different data types, perform type conversion, inspect object identity, and perform basic calculations.

It provides a strong foundation for beginners before moving on to more advanced Python concepts such as:

```text
Conditional Statements
        ↓
Loops
        ↓
Functions
        ↓
Lists & Tuples
        ↓
Dictionaries & Sets
        ↓
File Handling
        ↓
Object-Oriented Programming
        ↓
Pandas & NumPy
        ↓
Data Analysis & Machine Learning
```
