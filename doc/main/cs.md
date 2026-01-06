<link rel="stylesheet" href="https://devnamdev2003.github.io/md/static/style.css">

# C# Programming Language

## C# Overview

C# (pronounced "see sharp") is a modern, object-oriented, high-level programming language developed by Microsoft as part of its .NET initiative. It is designed to be simple, safe, and efficient, and is widely used in software development, web applications, mobile apps, and games.

### Key Features of C#

- **Object-Oriented:** C# embraces object-oriented programming principles, allowing developers to create classes and objects that represent real-world entities.
- **Type-Safe:** C# enforces strong typing, which ensures that data is handled according to its declared type, preventing errors and unexpected behaviors.
- **Memory Management:** C# uses automatic memory management through garbage collection, freeing developers from manual memory allocation and deallocation tasks.
- **Exception Handling:** C# provides robust exception handling mechanisms to trap and handle errors gracefully, preventing program crashes and ensuring application stability.
- **Cross-Platform Support:** Through the .NET Core platform, C# applications can be deployed on multiple platforms including Windows, macOS, and Linux.

## Creating Your First C# Project

To create your first C# project, you will need a development environment like Visual Studio or a text editor, and the .NET SDK installed. Here's a step-by-step guide:

1. **Create a New Project:** Open your development environment and create a new C# console application project.
2. **Write the Code:** In the main method (`Main`) of your program, include the following code:

```csharp
Console.WriteLine("Hello, World!");
```

3. **Build and Run:** Build the project to compile the code. Then, run the program to see the output. You should see the text "Hello, World!" printed on the console.

## C# Topics in Detail

### Variables

Variables are used to store data in C#. They must be declared with a specific type, such as `int`, `string`, or `bool`, before they can be used.

```csharp
// Declare an integer variable named age
int age = 25;
```

### Data Types

C# offers a variety of data types to represent different types of data, including numeric, string, and boolean values.

- Numeric: **int**, **long**, **float**, **double**
- String: **string**
- Boolean: **bool**

### Operators

Operators are used to perform operations on variables. Common operators include:

- Arithmetic: +, -, *, /
- Comparison: ==, !=, >, <
- Logical: &&, ||, !

```csharp
// Add two numbers using the + operator
int sum = a + b;
```

### Control Flow

Control flow statements are used to control the order in which statements are executed.

- Conditional Statements: **if**, **else**, **switch**
- Looping Statements: **for**, **while**, **do-while**

```csharp
// Check if a number is even using an if-else statement
if (number % 2 == 0) {
  Console.WriteLine("Even");
} else {
  Console.WriteLine("Odd");
}
```

### Arrays

Arrays are used to store a collection of items of a specific type.

```csharp
// Create an array of integers
int[] numbers = new int[] { 1, 2, 3, 4, 5 };
```

### Functions

Functions are reusable blocks of code that perform a specific task. They can be defined with a return type or as void (without a return value).

```csharp
// Define a function to calculate the area of a circle
double CalculateArea(double radius) {
  return Math.PI * radius * radius;
}
```

### Classes and Objects

Classes are blueprints for creating objects. They define the properties and behaviors of the objects.

```csharp
// Define a class for a person
public class Person {
  public string Name { get; set; }
  public int Age { get; set; }
}

// Create an instance of the Person class
Person john = new Person() { Name = "John", Age = 25 };
```

### Inheritance

Inheritance allows classes to inherit properties and behaviors from parent classes.

```csharp
// Define a child class that inherits from the Person class
public class Employee : Person {
  public string Company { get; set; }
}
```

### Interfaces

Interfaces define a set of methods that classes can implement.

```csharp
// Define an interface for a shape
public interface IShape {
  double GetArea();
}

// Define a class that implements the IShape interface
public class Circle : IShape {
  public double Radius { get; set; }

  public double GetArea() {
    return Math.PI * Radius * Radius;
  }
}
```

### Delegates and Events

Delegates represent functions that can be passed as parameters or stored in fields. Events are a way to communicate between objects.

```csharp
// Define a delegate for a function that takes a string
public delegate void StringDelegate(string s);

// Define an event that takes a StringDelegate argument
public event StringDelegate OnMessageReceived;

// Subscribe to the event
OnMessageReceived += (s) => Console.WriteLine(s);
```

### Generics

Generics allow you to create classes and methods that work with different data types.

```csharp
// Define a generic class for a stack
public class Stack<T> {
  private T[] items = new T[0];

  public void Push(T item) {
    Array.Resize(ref items, items.Length + 1);
    items[items.Length - 1] = item;
  }

  public T Pop() {
    if (items.Length == 0) {
      throw new InvalidOperationException("Stack is empty");
    }

    T item = items[items.Length - 1];
    Array.Resize(ref items, items.Length - 1);
    return item;
  }
}
```

### Exception Handling

Exception handling allows you to handle errors and prevent program crashes.

```csharp
try {
  // Code that might throw an exception
} catch (Exception ex) {
  // Code to handle the exception
}
```

### Asynchronous Programming

Asynchronous programming allows you to perform tasks without blocking the main thread.

```csharp
async Task<int> SumAsync(int[] numbers) {
  int sum = 0;
  foreach (var number in numbers) {
    sum += await Task.Run(() => CalculateSum(number));
  }

  return sum;
}
```

### LINQ (Language Integrated Query)

LINQ provides a concise way to query and manipulate data.

```csharp
// Get all the even numbers from a list
var evenNumbers = numbers.Where(n => n % 2 == 0);
```

These are just a few of the many topics covered in C#. For more detailed information, refer to the official C# documentation or online tutorials.

---

## Numeric Data Types

### Overview

Numeric data types represent numeric values, including whole numbers (integers) and fractional numbers (floating-point numbers). C# provides a wide range of numeric data types to suit different data requirements and performance considerations.

### Integer Types

**byte:** Represents unsigned 8-bit integers, with a value range from 0 to 255.

**sbyte:** Represents signed 8-bit integers, with a value range from -128 to 127.

**short:** Represents signed 16-bit integers, with a value range from -32,768 to 32,767.

**ushort:** Represents unsigned 16-bit integers, with a value range from 0 to 65,535.

**int:** Represents signed 32-bit integers, with a value range from -2,147,483,648 to 2,147,483,647.

**uint:** Represents unsigned 32-bit integers, with a value range from 0 to 4,294,967,295.

**long:** Represents signed 64-bit integers, with a value range from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

**ulong:** Represents unsigned 64-bit integers, with a value range from 0 to 18,446,744,073,709,551,615.

### Floating-Point Types

**float:** Represents single-precision floating-point numbers, with a precision of approximately 7 decimal digits and a value range from approximately -3.4e38 to 1.7e38.

**double:** Represents double-precision floating-point numbers, with a precision of approximately 15 decimal digits and a value range from approximately -1.7e308 to 1.7e308.

### Decimal Type

**decimal:** Represents fixed-point numeric values with a high precision of 128 bits. Decimal values have a smaller value range than floating-point types but offer greater precision for financial and other applications.

### Examples with Output

```csharp
// Integer types
byte b = 255;
sbyte sb = -128;
short sh = 32767;
ushort ush = 65535;
int i = 2147483647;
uint ui = 4294967295;
long l = 9223372036854775807;
ulong ul = 18446744073709551615;

// Floating-point types
float f = 1.23456789f;
double d = 123456789.123456789;

// Decimal type
decimal dec = 123456789.123456789m;

// Print values
Console.WriteLine("Byte: " + b);
Console.WriteLine("SByte: " + sb);
Console.WriteLine("Short: " + sh);
Console.WriteLine("UShort: " + ush);
Console.WriteLine("Int: " + i);
Console.WriteLine("UInt: " + ui);
Console.WriteLine("Long: " + l);
Console.WriteLine("ULong: " + ul);
Console.WriteLine("Float: " + f);
Console.WriteLine("Double: " + d);
Console.WriteLine("Decimal: " + dec);
```

**Output:**

```
Byte: 255
SByte: -128
Short: 32767
UShort: 65535
Int: 2147483647
UInt: 4294967295
Long: 9223372036854775807
ULong: 18446744073709551615
Float: 1.2345679
Double: 123456789.12345678
Decimal: 123456789.123456789
```

## Text-Based Data Types

### Overview

Text-based data types in C# represent character data, strings, and other text-related information. They provide flexibility in storing, manipulating, and displaying textual content within a program.

### Character Type

**char:** Represents a single Unicode character. It can hold any character from the Unicode character set, including letters, numbers, symbols, and special characters.

### String Type

**string:** Represents a sequence of characters enclosed in double quotes (" ") or single quotes (' '). Strings are immutable, meaning that once created, they cannot be modified directly.

### StringBuilder Type

**StringBuilder:** Represents a mutable string builder that can be used to efficiently build and modify strings. Unlike strings, StringBuilders can be modified in place, allowing for more efficient concatenation and manipulation of text.

### Examples with Output

```csharp
// Character type
char ch = 'A';

// String type
string str = "Hello World";

// StringBuilder type
StringBuilder sb = new StringBuilder();
sb.Append("StringBuilder ");
sb.Append("example");

// Print values
Console.WriteLine("Character: " + ch);
Console.WriteLine("String: " + str);
Console.WriteLine("StringBuilder: " + sb);
```

**Output:**

```
Character: A
String: Hello World
StringBuilder: StringBuilder example
```

---

## Converting String to Numbers

Converting a string to a number in C# can be achieved using various methods, depending on the desired numeric data type. Here are the commonly used methods:

### int.Parse Method

The `int.Parse` method converts a string representation of an integer to its corresponding integer value. It takes a string as an argument and returns an `int`.

```csharp
string numberString = "123";
int number = int.Parse(numberString);
Console.WriteLine(number); // Output: 123
```

### double.Parse Method

Similarly, the `double.Parse` method converts a string representation of a double-precision floating-point number to its corresponding double value.

```csharp
string decimalString = "3.14";
double decimalNumber = double.Parse(decimalString);
Console.WriteLine(decimalNumber); // Output: 3.14
```

### Convert.ToInt32 Method

The `Convert.ToInt32` method is a more generic way to convert a string to an integer. It takes a string and a base (defaulting to 10) as arguments and returns an `int`.

```csharp
string hexString = "FF";
int hexNumber = Convert.ToInt32(hexString, 16);
Console.WriteLine(hexNumber); // Output: 255
```

### Convert.ToDouble Method

Likewise, the `Convert.ToDouble` method converts a string to a double.

```csharp
string scientificString = "1.23e-5";
double scientificNumber = Convert.ToDouble(scientificString);
Console.WriteLine(scientificNumber); // Output: 0.0000123
```

## Boolean Data Type

In C#, the Boolean data type represents logical values: `true` or `false`. It is useful for representing binary choices or conditions.

### Declaring Boolean Variables

Boolean variables can be declared using the `bool` keyword.

```csharp
bool isLoggedIn = true;
bool isNight = false;
```

### Boolean Literals

Boolean literals are used to assign `true` or `false` values directly.

```csharp
bool isTrue = true;
bool isFalse = false;
```

### Boolean Operators

Boolean operators allow us to perform logical operations on Boolean values. Here are the common operators:

* **Logical AND (`&&`)**: Returns `true` if both operands are `true`, otherwise `false`.
* **Logical OR (`||`)**: Returns `true` if either operand is `true`, otherwise `false`.
* **Logical NOT (`!`)**: Negates the operand, returning `true` if it is `false`, and vice versa.
* **Conditional AND (`?`)**: Returns the left operand if it is `true`, otherwise returns the right operand.
* **Conditional OR (`??`)**: Returns the left operand if it is `true`, otherwise returns the right operand, which is evaluated lazily.

### Example:

```csharp
bool a = true, b = false;

Console.WriteLine(a && b); // Output: false
Console.WriteLine(a || b); // Output: true
Console.WriteLine(!a); // Output: false
Console.WriteLine(a ? "Yes" : "No"); // Output: "Yes"
Console.WriteLine(b ?? "Default"); // Output: "Default"
```

## Operators

Operators in C# are symbols that perform specific operations on variables and values. They can be classified into several types based on their functionality.

### Arithmetic Operators

Arithmetic operators perform mathematical operations on numeric values. Here are the common operators:

* `+`: Addition
* `-`: Subtraction
* `*`: Multiplication
* `/`: Division
* `%`: Modulus

### Example:

```csharp
int num1 = 10, num2 = 5;

Console.WriteLine(num1 + num2); // Output: 15
Console.WriteLine(num1 - num2); // Output: 5
Console.WriteLine(num1 * num2); // Output: 50
Console.WriteLine(num1 / num2); // Output: 2
Console.WriteLine(num1 % num2); // Output: 0
```

### Assignment Operators

Assignment operators assign values to variables. The most common operator is `=`. Additionally, there are compound assignment operators that combine an assignment with an operation.

* `=`: Assignment
* `+=`: Addition assignment
* `-=`: Subtraction assignment
* `*=`: Multiplication assignment
* `/=`: Division assignment
* `%=`: Modulus assignment

### Example:

```csharp
int num = 10;

num += 5; // Equivalent to num = num + 5
Console.WriteLine(num); // Output: 15
```

### Comparison Operators

Comparison operators compare two values and return a Boolean value (`true` or `false`). Here are the common operators:

* `==`: Equality
* `!=`: Inequality
* `<`: Less than
* `<=`: Less than or equal
* `>`: Greater than
* `>=`: Greater than or equal

### Example:

```csharp
int num1 = 10, num2 = 5;

Console.WriteLine(num1 == num2); // Output: false
Console.WriteLine(num1 != num2); // Output: true
Console.WriteLine(num1 < num2); // Output: false
Console.WriteLine(num1 <= num2); // Output: false
Console.WriteLine(num1 > num2); // Output: true
Console.WriteLine(num1 >= num2); // Output: true
```

### Logical Operators

Logical operators perform logical operations on Boolean values. Here are the common operators:

* `&&`: Logical AND
* `||`: Logical OR
* `!`: Logical NOT

### Example:

```csharp
bool isLoggedIn = true, isAdmin = false;

Console.WriteLine(isLoggedIn && isAdmin); // Output: false
Console.WriteLine(isLoggedIn || isAdmin); // Output: true
Console.WriteLine(!isLoggedIn); // Output: false
```

---

## Remainder

The remainder operator (%) returns the remainder of dividing two numbers. The syntax is:

```
a % b
```

where `a` and `b` are integers.

For example, the remainder of 7 divided by 3 is 1, because 7 divided by 3 is 2 with a remainder of 1.

```
Console.WriteLine(7 % 3); // Output: 1
```

The remainder operator can be used to check if a number is even or odd. A number is even if the remainder of dividing it by 2 is 0.

```
bool isEven = (number % 2 == 0);
```

The remainder operator can also be used to find the last digit of a number. The last digit of a number is the remainder of dividing the number by 10.

```
int lastDigit = number % 10;
```

## Var Keyword

The `var` keyword can be used to declare a variable without specifying its type. The type of the variable is inferred from the initializer. For example, the following code declares a variable named `x` of type `int`:

```
var x = 5;
```

The `var` keyword can be used to declare variables of any type. However, it is best to use the `var` keyword only when the type of the variable is obvious from the initializer. For example, the following code should not use the `var` keyword:

```
var x = new List<int>();
```

The type of the variable `x` is not obvious from the initializer, so it is better to declare the variable explicitly:

```
List<int> x = new List<int>();
```

## Const Keyword

The `const` keyword can be used to declare a constant. A constant is a value that cannot be changed. The syntax is:

```
const type name = value;
```

where `type` is the type of the constant, `name` is the name of the constant, and `value` is the value of the constant.

For example, the following code declares a constant named `PI` of type `double`:

```
const double PI = 3.14;
```

The value of the constant `PI` cannot be changed.

Constants are often used to represent values that should not change during the execution of a program. For example, the value of `PI` should not change, so it is declared as a constant.

Constants can also be used to improve the readability of code. For example, the following code is more readable than the previous code:

```
const double PI = 3.14;

double radius = 5;

double circumference = 2 * PI * radius;
```

The code is more readable because the value of `PI` is declared as a constant, so it is clear that the value of `PI` will not change.

---

{'error': 'AI API error: The `response.text` quick accessor only works when the response contains a valid `Part`, but none was returned. Check the `candidate.safety_ratings` to see if the response was blocked.'}

---

{'error': 'AI API error: The `response.text` quick accessor only works when the response contains a valid `Part`, but none was returned. Check the `candidate.safety_ratings` to see if the response was blocked.'}

---

**While Loops**

A while loop is a control flow statement that executes a block of code as long as a given condition is true. The syntax of a while loop is as follows:

```
while (condition)
{
    // Code to be executed
}
```

The condition can be any Boolean expression. If the condition is true, the code block will be executed. If the condition is false, the loop will terminate and execution will continue with the next statement after the loop.

Here is an example of a while loop that prints the numbers from 1 to 10:

```
int i = 1;

while (i <= 10)
{
    Console.WriteLine(i);
    i++;
}
```

Output:

```
1
2
3
4
5
6
7
8
9
10
```

**Conditional Operator**

The conditional operator is a shorthand way of writing an if-else statement. The syntax of the conditional operator is as follows:

```
condition ? trueValue : falseValue
```

If the condition is true, the expression will evaluate to trueValue. If the condition is false, the expression will evaluate to falseValue.

Here is an example of a conditional operator that returns the string "Yes" if the condition is true, and "No" if the condition is false:

```
bool condition = true;

string result = condition ? "Yes" : "No";
```

The value of result will be "Yes" because the condition is true.

**Numeric Formatting**

Numeric formatting is the process of converting a number to a string in a specific format. The .NET Framework provides a number of methods for formatting numeric values, including:

* ToString()
* ToString(string)
* ToString(IFormatProvider)

The ToString() method converts a numeric value to a string in the current culture's format. The ToString(string) method converts a numeric value to a string in the specified format. The ToString(IFormatProvider) method converts a numeric value to a string in the specified format provider's format.

Here are some examples of how to use the numeric formatting methods:

```
int number = 123456789;

// Convert the number to a string in the current culture's format
string result = number.ToString();

// Convert the number to a string in the "C" format
string result = number.ToString("C");

// Convert the number to a string in the "N" format
string result = number.ToString("N");
```

The output of the above code is as follows:

```
123,456,789
$123,456,789.00
123,456,789.00
```

As you can see, the output of the ToString() method is a string in the current culture's format. The output of the ToString("C") method is a string in the "C" format, which is a currency format. The output of the ToString("N") method is a string in the "N" format, which is a number format.

---

{'error': 'AI API error: The `response.text` quick accessor only works when the response contains a valid `Part`, but none was returned. Check the `candidate.safety_ratings` to see if the response was blocked.'}

---

## Verbatim String Literals

Verbatim string literals are a way to represent strings in C# without having to escape special characters. This can be useful when working with strings that contain characters that would otherwise have special meaning, such as quotes or backslashes.

To create a verbatim string literal, simply prefix the string with an `@` character. For example:

```csharp
string myString = @"This is a verbatim string literal.";
```

The following characters are interpreted literally in verbatim string literals:

* `"` (double quote)
* `'}` (single quote)
* `\n` (newline)
* `\r` (carriage return)
* `\t` (tab)
* `\b` (backspace)
* `\f` (form feed)
* `\v` (vertical tab)

All other characters are interpreted as their literal value.

Here are some examples of verbatim string literals:

```csharp
string myString1 = @"This is a verbatim string literal with a double quote: "".";
string myString2 = @"This is a verbatim string literal with a single quote: '.";
string myString3 = @"This is a verbatim string literal with a newline:

.";
```

## String Formatting

String formatting is a way to insert values into a string using placeholders. This can be useful for creating strings that are dynamically generated, such as error messages or user-friendly prompts.

To format a string, you use the `string.Format` method. The first argument to `string.Format` is the format string, which contains placeholders for the values to be inserted. The remaining arguments to `string.Format` are the values to be inserted.

The placeholder in a format string is a curly-braced expression that specifies the index of the value to be inserted. For example, the following format string inserts the value of the first argument into the string:

```csharp
string myString = string.Format("The value is {0}.", 123);
```

You can also specify the format of the inserted value using a format specifier. A format specifier is a suffix that is appended to the curly-braced expression. For example, the following format string inserts the value of the first argument as a currency value:

```csharp
string myString = string.Format("The value is {0:C}.", 123);
```

Here are some of the most common format specifiers:

* `C`: Currency
* `D`: Decimal
* `E`: Exponential
* `F`: Fixed-point
* `G`: General
* `N`: Number
* `P`: Percent
* `X`: Hexadecimal

For a complete list of format specifiers, see the [String.Format documentation](https://docs.microsoft.com/en-us/dotnet/standard/base-types/string-format-method).

## String Interpolation

String interpolation is a newer way to format strings in C# 6.0 and later. It uses curly braces to embed expressions directly into strings.

For example, the following code uses string interpolation to insert the value of the `name` variable into the string:

```csharp
string name = "John Doe";
string myString = $"Hello, {name}!";
```

String interpolation is more concise and easier to read than using the `string.Format` method. It is also more flexible, as you can use any valid C# expression in a string interpolation expression.

Here are some of the benefits of using string interpolation:

* It is more concise and easier to read than using the `string.Format` method.
* It is more flexible, as you can use any valid C# expression in a string interpolation expression.
* It is supported in all versions of C# 6.0 and later.

Here are some examples of string interpolation:

```csharp
// Insert the value of the name variable into the string
string name = "John Doe";
string myString = $"Hello, {name}!";

// Insert the result of the expression into the string
int age = 30;
string myString = $"I am {age} years old.";

// Insert the value of the property into the string
public class Person
{
    public string Name { get; set; }
}

Person person = new Person() { Name = "John Doe" };
string myString = $"Hello, {person.Name}!";
```

---

**String Concatenation**

String concatenation is the process of joining two or more strings together to form a new string. In C#, the plus sign (+) operator is used to concatenate strings. For example:

```csharp
string firstName = "John";
string lastName = "Doe";
string fullName = firstName + " " + lastName;
Console.WriteLine(fullName); // Output: John Doe
```

The above code creates three strings: `firstName`, `lastName`, and `fullName`. The `firstName` and `lastName` strings are concatenated using the plus sign operator to form the `fullName` string. The `fullName` string is then printed to the console.

**Empty String**

The empty string is a string that contains no characters. It is represented by the `""` string literal. For example:

```csharp
string emptyString = "";
Console.WriteLine(emptyString); // Output:
```

The above code creates an empty string called `emptyString`. The `emptyString` string is then printed to the console.

**String Equals Function**

The `Equals` function compares two strings to determine if they are equal. The `Equals` function takes two string arguments and returns a boolean value indicating whether the two strings are equal. For example:

```csharp
string firstName = "John";
string lastName = "Doe";
bool areEqual = firstName.Equals(lastName);
Console.WriteLine(areEqual); // Output: False
```

The above code creates three strings: `firstName`, `lastName`, and `areEqual`. The `firstName` and `lastName` strings are compared using the `Equals` function to determine if they are equal. The `areEqual` variable is then assigned the result of the comparison. The `areEqual` variable is then printed to the console.

In the above example, the `firstName` and `lastName` strings are not equal, so the `areEqual` variable is assigned the value `False`.

**Additional Information**

* The `+` operator can also be used to concatenate strings and other types of data. For example:

```csharp
string firstName = "John";
int age = 30;
string fullName = firstName + " is " + age + " years old.";
Console.WriteLine(fullName); // Output: John is 30 years old.
```

* The `String.IsNullOrEmpty` method can be used to check if a string is null or empty. For example:

```csharp
string firstName = null;
if (String.IsNullOrEmpty(firstName))
{
    Console.WriteLine("The firstName variable is null or empty.");
}
```

* The `String.Compare` method can be used to compare two strings to determine their relative order. The `String.Compare` method takes two string arguments and returns an integer value indicating the relative order of the two strings. The following table shows the possible return values of the `String.Compare` method:

| Return Value | Description                                         |
| ------------ | --------------------------------------------------- |
| -1           | The first string is less than the second string.    |
| 0            | The first string is equal to the second string.     |
| 1            | The first string is greater than the second string. |

---

**String iteration looping**

String iteration looping is a technique used to iterate over the characters of a string. This can be done using a for loop, a foreach loop, or a while loop.

**For loop**

The for loop is the most common way to iterate over the characters of a string. The syntax is as follows:

```
for (int i = 0; i < str.Length; i++)
{
    // Do something with the character at index i
}
```

The following code example shows how to use a for loop to iterate over the characters of a string and print each character to the console:

```
string str = "Hello world";

for (int i = 0; i < str.Length; i++)
{
    Console.WriteLine(str[i]);
}
```

**Output:**

```
H
e
l
l
o
 
w
o
r
l
d
```

**Foreach loop**

The foreach loop is a more concise way to iterate over the characters of a string. The syntax is as follows:

```
foreach (char c in str)
{
    // Do something with the character c
}
```

The following code example shows how to use a foreach loop to iterate over the characters of a string and print each character to the console:

```
string str = "Hello world";

foreach (char c in str)
{
    Console.WriteLine(c);
}
```

**Output:**

```
H
e
l
l
o
 
w
o
r
l
d
```

**While loop**

The while loop can also be used to iterate over the characters of a string. However, it is not as common as the for loop or the foreach loop. The syntax is as follows:

```
int i = 0;
while (i < str.Length)
{
    // Do something with the character at index i
    i++;
}
```

The following code example shows how to use a while loop to iterate over the characters of a string and print each character to the console:

```
string str = "Hello world";

int i = 0;
while (i < str.Length)
{
    Console.WriteLine(str[i]);
    i++;
}
```

**Output:**

```
H
e
l
l
o
 
w
o
r
l
d
```

**String IsNullOrEmpty function**

The IsNullOrEmpty function is a static method of the String class that returns a boolean value indicating whether the string is null or empty. The syntax is as follows:

```
public static bool IsNullOrEmpty(string str);
```

The following code example shows how to use the IsNullOrEmpty function to check if a string is null or empty:

```
string str = null;

if (string.IsNullOrEmpty(str))
{
    Console.WriteLine("The string is null or empty.");
}
else
{
    Console.WriteLine("The string is not null or empty.");
}
```

**Output:**

```
The string is null or empty.
```

The IsNullOrEmpty function can be useful for checking if a string is valid before using it in other operations. For example, you could use the IsNullOrEmpty function to check if a string is null or empty before trying to convert it to an integer.

**Exercise - Print string in reverse**

Write a program that prints a string in reverse.

**Solution:**

The following code example shows how to write a program that prints a string in reverse:

```
string str = "Hello world";

for (int i = str.Length - 1; i >= 0; i--)
{
    Console.WriteLine(str[i]);
}
```

**Output:**

```
d
l
r
o
w
 
l
l
e
H
```

The program uses a for loop to iterate over the characters of the string in reverse order. The loop starts at the last index of the string and decrements the index by one each time through the loop. This causes the loop to iterate over the characters of the string in reverse order.

---

## Arrays

### Definition

An array is a data structure that stores a fixed-size sequential collection of elements of the same type. An array is used to store a collection of data, but it is often more useful to think of an array as a collection of variables of the same type instead.

### Declaration

An array is declared by specifying the type of its elements followed by the name of the array and its size enclosed in square brackets. For example, the following declaration creates an array of 10 integers named `numbers`:

```c#
int[] numbers = new int[10];
```

### Accessing Elements

Individual elements of an array are accessed using their index, which is a zero-based number. The following statement assigns the value 10 to the first element of the `numbers` array:

```c#
numbers[0] = 10;
```

### Iterating Over Elements

The `foreach` statement can be used to iterate over the elements of an array. The following statement iterates over the `numbers` array and prints the value of each element:

```c#
foreach (int number in numbers)
{
    Console.WriteLine(number);
}
```

### Multidimensional Arrays

Multidimensional arrays can be used to store data in a more organized way. A multidimensional array is declared by specifying the number of dimensions followed by the type of its elements, the name of the array, and the size of each dimension. For example, the following declaration creates a two-dimensional array of integers named `matrix`:

```c#
int[,] matrix = new int[3, 4];
```

### Jagged Arrays

Jagged arrays are arrays of arrays. They are declared by specifying the type of their elements, the name of the array, and the number of dimensions. For example, the following declaration creates a jagged array of integers named `jaggedArray`:

```c#
int[][] jaggedArray = new int[3][];
```

## Array Sorting

### Introduction

Array sorting is the process of arranging the elements of an array in a specific order. Sorting can be performed on arrays of any type, but it is most commonly used on arrays of numbers or strings.

### Built-in Sorting Methods

The `Array` class provides several built-in sorting methods, including:

* `Sort()`: Sorts the elements of an array in ascending order.
* `Sort(IComparer)`: Sorts the elements of an array using a specified comparer.
* `Reverse()`: Reverses the order of the elements in an array.

### Custom Sorting

You can also create your own custom sorting methods. To do this, you need to implement the `IComparer` interface and provide a comparison method that compares two elements of the array. For example, the following custom sorting method sorts the elements of an array of strings in descending order:

```c#
public class StringComparer : IComparer
{
    public int Compare(object x, object y)
    {
        string s1 = (string)x;
        string s2 = (string)y;

        return -s1.CompareTo(s2);
    }
}
```

## Code Examples

### Sorting an Array of Numbers

The following code example shows how to sort an array of numbers using the `Sort()` method:

```c#
int[] numbers = { 5, 1, 3, 2, 4 };

Array.Sort(numbers);

foreach (int number in numbers)
{
    Console.WriteLine(number);
}
```

Output:

```
1
2
3
4
5
```

### Sorting an Array of Strings

The following code example shows how to sort an array of strings using the `Sort()` method and a custom comparer:

```c#
string[] strings = { "banana", "apple", "cherry", "dog", "cat" };

StringComparer comparer = new StringComparer();

Array.Sort(strings, comparer);

foreach (string s in strings)
{
    Console.WriteLine(s);
}
```

Output:

```
apple
banana
cat
cherry
dog
```

---

## Array Reversal

An array is a data structure that stores a fixed-size sequential collection of elements of the same type. An array is used to store a collection of data, but it is often more useful to be able to access the elements of the array in reverse order.

To reverse an array, you can use the `Array.Reverse()` method. This method takes an array as an argument and reverses the order of the elements in the array.

For example, the following code reverses the order of the elements in the `numbers` array:

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
Array.Reverse(numbers);
```

After the `Array.Reverse()` method is called, the `numbers` array will contain the following elements:

```csharp
{ 5, 4, 3, 2, 1 }
```

You can also reverse an array manually by using a `for` loop to iterate through the array and swap the elements at each index.

For example, the following code reverses the order of the elements in the `numbers` array using a `for` loop:

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
for (int i = 0; i < numbers.Length / 2; i++)
{
    int temp = numbers[i];
    numbers[i] = numbers[numbers.Length - 1 - i];
    numbers[numbers.Length - 1 - i] = temp;
}
```

After the `for` loop is finished, the `numbers` array will contain the following elements:

```csharp
{ 5, 4, 3, 2, 1 }
```

## Array Clearing

An array is a data structure that stores a fixed-size sequential collection of elements of the same type. An array is used to store a collection of data, but it is often useful to be able to clear the array and remove all of the elements.

To clear an array, you can use the `Array.Clear()` method. This method takes an array as an argument and sets all of the elements in the array to the default value for the array's element type.

For example, the following code clears the `numbers` array:

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
Array.Clear(numbers, 0, numbers.Length);
```

After the `Array.Clear()` method is called, the `numbers` array will contain the following elements:

```csharp
{ 0, 0, 0, 0, 0 }
```

You can also clear an array manually by using a `for` loop to iterate through the array and set each element to the default value for the array's element type.

For example, the following code clears the `numbers` array using a `for` loop:

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
for (int i = 0; i < numbers.Length; i++)
{
    numbers[i] = 0;
}
```

After the `for` loop is finished, the `numbers` array will contain the following elements:

```csharp
{ 0, 0, 0, 0, 0 }
```

## Array IndexOf

An array is a data structure that stores a fixed-size sequential collection of elements of the same type. An array is used to store a collection of data, but it is often useful to be able to find the index of a specific element in the array.

To find the index of an element in an array, you can use the `Array.IndexOf()` method. This method takes an array and a value as arguments and returns the index of the first occurrence of the value in the array.

For example, the following code finds the index of the value `3` in the `numbers` array:

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
int index = Array.IndexOf(numbers, 3);
```

The `index` variable will be assigned the value `2`, which is the index of the first occurrence of the value `3` in the `numbers` array.

You can also find the index of an element in an array manually by using a `for` loop to iterate through the array and compare each element to the value you are searching for.

For example, the following code finds the index of the value `3` in the `numbers` array using a `for` loop:

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
int index = -1;
for (int i = 0; i < numbers.Length; i++)
{
    if (numbers[i] == 3)
    {
        index = i;
        break;
    }
}
```

The `index` variable will be assigned the value `2`, which is the index of the first occurrence of the value `3` in the `numbers` array.

---

## Lists
A list is a mutable, ordered sequence of elements. It allows duplicate elements, and the order of the elements is preserved. Lists are created using square brackets ([]), and the elements are separated by commas. For example, the following code creates a list of numbers:

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
```

Lists can be accessed using the index of the element. The first element has an index of 0, the second element has an index of 1, and so on. The following code accesses the first element of the numbers list:

```csharp
int firstNumber = numbers[0]; // 1
```

Lists can be modified by adding or removing elements. The Add() method adds an element to the end of the list, and the Remove() method removes an element from the list. The following code adds the number 6 to the end of the numbers list:

```csharp
numbers.Add(6);
```

The following code removes the first element from the numbers list:

```csharp
numbers.RemoveAt(0);
```

Lists can be iterated over using a foreach loop. The following code iterates over the numbers list and prints each element to the console:

```csharp
foreach (int number in numbers)
{
    Console.WriteLine(number);
}
```

Output:

```
1
2
3
4
5
6
```

## Dictionary
A dictionary is a mutable, unordered collection of key-value pairs. The keys are unique, and the values can be of any type. Dictionaries are created using curly braces ({}), and the key-value pairs are separated by colons (:). For example, the following code creates a dictionary of names and ages:

```csharp
Dictionary<string, int> namesAndAges = new Dictionary<string, int>
{
    { "Alice", 25 },
    { "Bob", 30 },
    { "Charlie", 35 }
};
```

Dictionaries can be accessed using the key of the key-value pair. The following code accesses the age of Alice from the namesAndAges dictionary:

```csharp
int aliceAge = namesAndAges["Alice"]; // 25
```

Dictionaries can be modified by adding or removing key-value pairs. The Add() method adds a key-value pair to the dictionary, and the Remove() method removes a key-value pair from the dictionary. The following code adds the key-value pair "Dave" and 40 to the namesAndAges dictionary:

```csharp
namesAndAges.Add("Dave", 40);
```

The following code removes the key-value pair "Charlie" from the namesAndAges dictionary:

```csharp
namesAndAges.Remove("Charlie");
```

Dictionaries can be iterated over using a foreach loop. The following code iterates over the namesAndAges dictionary and prints each key-value pair to the console:

```csharp
foreach (KeyValuePair<string, int> pair in namesAndAges)
{
    Console.WriteLine($"{pair.Key}: {pair.Value}");
}
```

Output:

```
Alice: 25
Bob: 30
Dave: 40
```

## Exercise - Odd/Even number split
Write a C# program that takes a list of integers and splits it into two lists: one list for odd numbers and one list for even numbers.

```csharp
using System;
using System.Collections.Generic;

namespace OddEvenSplit
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a list of integers
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            // Create two lists to store the odd and even numbers
            List<int> oddNumbers = new List<int>();
            List<int> evenNumbers = new List<int>();

            // Iterate over the numbers list and add each number to the appropriate list
            foreach (int number in numbers)
            {
                if (number % 2 == 0)
                {
                    evenNumbers.Add(number);
                }
                else
                {
                    oddNumbers.Add(number);
                }
            }

            // Print the odd and even numbers lists
            Console.WriteLine("Odd numbers:");
            foreach (int number in oddNumbers)
            {
                Console.WriteLine(number);
            }

            Console.WriteLine("Even numbers:");
            foreach (int number in evenNumbers)
            {
                Console.WriteLine(number);
            }
        }
    }
}
```

Output:

```
Odd numbers:
1
3
5
7
9
Even numbers:
2
4
6
8
10
```

---

## Array of multiples

An array of multiples is an array that contains the multiples of a given number. For example, an array of multiples of 5 would contain the numbers 5, 10, 15, 20, and so on.

Arrays of multiples can be created using a for loop. The following code creates an array of multiples of 5 up to 100:

```
int[] multiples = new int[20];

for (int i = 0; i < 20; i++)
{
    multiples[i] = 5 * i;
}
```

Once an array of multiples has been created, it can be used like any other array. The following code prints the array of multiples of 5 to the console:

```
for (int i = 0; i < 20; i++)
{
    Console.WriteLine(multiples[i]);
}
```

Output:

```
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
```

Arrays of multiples can be useful for a variety of tasks, such as:

* Generating test data
* Populating drop-down lists
* Creating sequences of numbers

## Code examples

The following code examples demonstrate how to use arrays of multiples in C#:

**Example 1: Create an array of multiples of 5**

```
int[] multiples = new int[20];

for (int i = 0; i < 20; i++)
{
    multiples[i] = 5 * i;
}
```

**Example 2: Print an array of multiples of 5 to the console**

```
for (int i = 0; i < 20; i++)
{
    Console.WriteLine(multiples[i]);
}
```

**Example 3: Use an array of multiples to populate a drop-down list**

The following code example demonstrates how to use an array of multiples to populate a drop-down list:

```
// Create an array of multiples of 5
int[] multiples = new int[20];

for (int i = 0; i < 20; i++)
{
    multiples[i] = 5 * i;
}

// Create a drop-down list and add the multiples to it
DropDownList dropDownList = new DropDownList();

foreach (int multiple in multiples)
{
    dropDownList.Items.Add(new ListItem(multiple.ToString()));
}
```

**Example 4: Use an array of multiples to create a sequence of numbers**

The following code example demonstrates how to use an array of multiples to create a sequence of numbers:

```
// Create an array of multiples of 5
int[] multiples = new int[20];

for (int i = 0; i < 20; i++)
{
    multiples[i] = 5 * i;
}

// Create a sequence of numbers using the multiples
IEnumerable<int> sequence = multiples.Select(x => x * x);

// Print the sequence to the console
foreach (int number in sequence)
{
    Console.WriteLine(number);
}
```

---

## Return Type Functions

A function's return type specifies the data type of the value that the function returns. The return type is declared after the function's name and parameters, as shown in the following example:

```
int Sum(int a, int b)
{
    return a + b;
}
```

In this example, the `Sum` function takes two integer parameters (`a` and `b`) and returns an integer value.

The return type of a function can be any valid C# data type, including primitive types (such as `int`, `double`, and `bool`), reference types (such as `string` and `object`), and custom types (such as classes and structs).

If a function does not return a value, its return type must be declared as `void`. For example:

```
void PrintMessage(string message)
{
    Console.WriteLine(message);
}
```

The `PrintMessage` function takes a string parameter (`message`) and prints it to the console. It does not return a value, so its return type is declared as `void`.

## Function Parameters

Function parameters are used to pass data into a function. Parameters are declared within the parentheses after the function's name, as shown in the following example:

```
int Sum(int a, int b)
{
    return a + b;
}
```

In this example, the `Sum` function has two parameters: `a` and `b`. Both parameters are of type `int`.

Parameters can be of any valid C# data type, including primitive types, reference types, and custom types.

Parameters can also be declared as optional, which means that they do not have to be specified when the function is called. Optional parameters are declared using the `default` keyword, as shown in the following example:

```
int Sum(int a, int b = 0)
{
    return a + b;
}
```

In this example, the `Sum` function has two parameters: `a` and `b`. The `b` parameter is optional, with a default value of 0. This means that the `Sum` function can be called with one or two arguments.

## Optional Parameters

Optional parameters allow you to specify default values for function parameters. This can make your code more flexible and easier to use.

To declare an optional parameter, you use the `default` keyword. The default value can be any valid C# expression. For example:

```
int Sum(int a, int b = 0)
{
    return a + b;
}
```

In this example, the `b` parameter is optional, with a default value of 0. This means that the `Sum` function can be called with one or two arguments.

If you do not specify a default value for an optional parameter, its default value will be `null`.

Optional parameters can be used to make your code more flexible and easier to use. For example, the following function takes a variable number of arguments and returns their sum:

```
int Sum(params int[] numbers)
{
    int sum = 0;
    foreach (int number in numbers)
    {
        sum += number;
    }
    return sum;
}
```

This function can be called with any number of arguments. If no arguments are specified, the function will return 0.

Optional parameters can be a powerful tool for making your code more flexible and easier to use.

---

## Named Parameters

Named parameters allow you to specify the name of the parameter when you pass it to a method. This can make your code more readable and easier to maintain, especially when you have methods with many parameters.

To use named parameters, you simply specify the parameter name followed by a colon and the value of the parameter. For example, the following code calls the `PrintPerson` method and passes the `name` and `age` parameters by name:

```csharp
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

public static void PrintPerson(string name, int age)
{
    Console.WriteLine($"Name: {name}, Age: {age}");
}

public static void Main()
{
    PrintPerson(name: "John", age: 30);
}
```

Output:

```
Name: John, Age: 30
```

You can also use named parameters to pass optional parameters to a method. To do this, you simply specify the default value of the parameter after the colon. For example, the following code calls the `PrintPerson` method and passes the `name` parameter by name and the `age` parameter with the default value of 0:

```csharp
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

public static void PrintPerson(string name, int age = 0)
{
    Console.WriteLine($"Name: {name}, Age: {age}");
}

public static void Main()
{
    PrintPerson(name: "John");
}
```

Output:

```
Name: John, Age: 0
```

## Out Parameters

Out parameters allow you to pass a reference to a variable to a method. This allows the method to modify the value of the variable.

To use out parameters, you simply specify the `out` keyword followed by the type of the parameter. For example, the following code calls the `GetPerson` method and passes an out parameter for the `person` variable:

```csharp
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

public static void GetPerson(out Person person)
{
    person = new Person() { Name = "John", Age = 30 };
}

public static void Main()
{
    Person person;
    GetPerson(out person);
    Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
}
```

Output:

```
Name: John, Age: 30
```

In this example, the `GetPerson` method creates a new `Person` object and assigns it to the `person` out parameter. The `Main` method then uses the `person` variable to print the person's name and age.

## Reference Parameters

Reference parameters allow you to pass a reference to a variable to a method. This allows the method to modify the value of the variable.

To use reference parameters, you simply specify the `ref` keyword followed by the type of the parameter. For example, the following code calls the `Swap` method and passes reference parameters for the `a` and `b` variables:

```csharp
public static void Swap(ref int a, ref int b)
{
    int temp = a;
    a = b;
    b = temp;
}

public static void Main()
{
    int a = 1;
    int b = 2;
    Swap(ref a, ref b);
    Console.WriteLine($"a: {a}, b: {b}");
}
```

Output:

```
a: 2, b: 1
```

In this example, the `Swap` method swaps the values of the `a` and `b` variables. The `Main` method then uses the `a` and `b` variables to print the values of the variables after they have been swapped.

---

**Area of a Triangle**

The area of a triangle can be calculated using the formula:  
```
Area = (1/2) * base * height
```

where base is the length of the base of the triangle and height is the length of the height of the triangle.

Here is a C# program that calculates the area of a triangle:

```C#
using System;

namespace AreaOfTriangle
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get the base and height of the triangle from the user.
            Console.WriteLine("Enter the base of the triangle:");
            double @base = double.Parse(Console.ReadLine());

            Console.WriteLine("Enter the height of the triangle:");
            double height = double.Parse(Console.ReadLine());

            // Calculate the area of the triangle.
            double area = (0.5) * @base * height;

            // Display the area of the triangle.
            Console.WriteLine("The area of the triangle is: {0}", area);
        }
    }
}
```

Output:

```
Enter the base of the triangle:
10
Enter the height of the triangle:
5
The area of the triangle is: 25
```

**Sum of int Array**

The sum of an array of integers can be calculated by iterating over the array and adding each element to a running total.

Here is a C# program that calculates the sum of an array of integers:

```C#
using System;

namespace SumOfIntArray
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create an array of integers.
            int[] numbers = { 1, 2, 3, 4, 5 };

            // Calculate the sum of the array.
            int sum = 0;
            for (int i = 0; i < numbers.Length; i++)
            {
                sum += numbers[i];
            }

            // Display the sum of the array.
            Console.WriteLine("The sum of the array is: {0}", sum);
        }
    }
}
```

Output:

```
The sum of the array is: 15
```

**Exception Handling**

Exception handling is a way of handling errors that occur during the execution of a program. In C#, exceptions are represented by objects that inherit from the `System.Exception` class.

There are two main types of exceptions:  
1. **Checked exceptions** are exceptions that are detected by the compiler. They must be handled or declared as being thrown by the method.
2. **Unchecked exceptions** are exceptions that are not detected by the compiler. They do not need to be handled or declared as being thrown by the method.

Here is an example of how to handle exceptions in C#:

```C#
using System;

namespace ExceptionHandling
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Code that might throw an exception.
                int x = int.Parse("abc");
            }
            catch (FormatException e)
            {
                // Code to handle the exception.
                Console.WriteLine("The input string is not a valid number.");
            }
            finally
            {
                // Code that will always be executed, regardless of whether an exception is thrown.
                Console.WriteLine("This code will always be executed.");
            }
        }
    }
}
```

Output:

```
The input string is not a valid number.
This code will always be executed.
```

---

## Try...catch

The `try...catch` statement is used to handle exceptions that may occur during the execution of a block of code. The `try` block contains the code that may throw an exception, and the `catch` block contains the code that will handle the exception if it occurs.

### Syntax

```c#
try
{
    // Code that may throw an exception
}
catch (Exception ex)
{
    // Code to handle the exception
}
```

### Example

The following code demonstrates how to use the `try...catch` statement to handle an exception:

```c#
try
{
    int[] numbers = new int[] { 1, 2, 3, 4, 5 };
    int index = 5;
    Console.WriteLine(numbers[index]);
}
catch (IndexOutOfRangeException ex)
{
    Console.WriteLine("Error: Index out of range.");
}
```

Output:

```
Error: Index out of range.
```

### Printing Error Messages

When an exception occurs, the `Exception` object contains a `Message` property that can be used to retrieve a description of the error. The following code demonstrates how to print the error message:

```c#
try
{
    int[] numbers = new int[] { 1, 2, 3, 4, 5 };
    int index = 5;
    Console.WriteLine(numbers[index]);
}
catch (Exception ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

Output:

```
Error: Index was outside the bounds of the array.
```

## Custom TryParse

The `TryParse` method is a static method that attempts to convert a string to a specified type. If the conversion is successful, the `TryParse` method returns a `true` value and the converted value is stored in the `out` parameter. If the conversion is unsuccessful, the `TryParse` method returns a `false` value and the `out` parameter is not modified.

### Syntax

```c#
public static bool TryParse(string s, out T result);
```

where:

* `s` is the string to convert.
* `T` is the type to convert the string to.
* `result` is the converted value.

### Example

The following code demonstrates how to use the `TryParse` method to convert a string to an integer:

```c#
string s = "123";
int result;
if (int.TryParse(s, out result))
{
    Console.WriteLine("The converted value is: " + result);
}
else
{
    Console.WriteLine("The string could not be converted to an integer.");
}
```

Output:

```
The converted value is: 123
```

### Creating a Custom TryParse Method

You can also create your own custom `TryParse` method for a specific type. The following code demonstrates how to create a custom `TryParse` method for a `Date` type:

```c#
public static bool TryParse(string s, out Date result)
{
    // Parse the string into a Date object
    try
    {
        result = new Date(s);
        return true;
    }
    catch
    {
        result = null;
        return false;
    }
}
```

Once you have created a custom `TryParse` method, you can use it to convert a string to the specified type. The following code demonstrates how to use the custom `TryParse` method to convert a string to a `Date` object:

```c#
string s = "2020-12-31";
Date result;
if (Date.TryParse(s, out result))
{
    Console.WriteLine("The converted value is: " + result);
}
else
{
    Console.WriteLine("The string could not be converted to a Date object.");
}
```

Output:

```
The converted value is: 2020-12-31
```

---

**Local/Auto Window**

The Local/Auto window displays the values of local and auto variables in the current scope. It is helpful for debugging and understanding the flow of your program.

To open the Local/Auto window, go to **Debug > Windows > Locals** or press **Ctrl + Alt + V**.

**How to use the Local/Auto window:**

1. **Select a stack frame**. If your program is paused at a breakpoint, you can select a stack frame in the Call Stack window. This will show the local variables for the selected stack frame.
2. **Inspect variable values**. The Local/Auto window displays the name, type, and value of each local variable. You can expand the value to see more details, such as the contents of an array or object.
3. **Set variable values**. You can edit the value of a local variable by double-clicking on it and entering a new value. This is helpful for testing different values and debugging your program.

**Example:**

The following code snippet demonstrates how to use the Local/Auto window to debug a simple program:

```c#
int x = 10;
int y = 20;

Console.WriteLine("x = {0}", x);
Console.WriteLine("y = {0}", y);

// Set a breakpoint here
int z = x + y;

Console.WriteLine("z = {0}", z);
```

To debug this program, you can set a breakpoint on the line where `z` is assigned a value. Then, you can open the Local/Auto window and inspect the values of `x`, `y`, and `z`. You can also edit the value of `x` and `y` to see how it affects the value of `z`.

**Watch Window**

The Watch window allows you to monitor the values of variables throughout the execution of your program. It is helpful for debugging and understanding the state of your program at specific points in time.

To open the Watch window, go to **Debug > Windows > Watch** or press **Ctrl + Alt + W**.

**How to use the Watch window:**

1. **Add variables to the watch list**. To add a variable to the watch list, select it in the Local/Auto window and drag it to the Watch window. You can also type the name of the variable into the Watch window.
2. **Inspect variable values**. The Watch window displays the name, type, and value of each variable in the watch list. You can expand the value to see more details, such as the contents of an array or object.
3. **Evaluate expressions**. You can also evaluate expressions in the Watch window. To do this, enter the expression into the Expression field and press Enter. The Watch window will display the result of the evaluation.

**Example:**

The following code snippet demonstrates how to use the Watch window to debug a simple program:

```c#
int x = 10;
int y = 20;

Console.WriteLine("x = {0}", x);
Console.WriteLine("y = {0}", y);

// Add x and y to the watch list
int z = x + y;

Console.WriteLine("z = {0}", z);
```

To debug this program, you can add `x` and `y` to the Watch window. Then, you can step through the program and watch how the values of `x`, `y`, and `z` change. You can also evaluate expressions in the Watch window, such as `x + y` or `z * 2`, to see how they are affected by the execution of your program.

---

## Structures

A structure is a value type that can contain multiple fields of different types. Unlike classes, structures do not support inheritance or polymorphism. Structures are typically used to represent small, lightweight objects that do not require the full functionality of a class.

### Defining a Structure

To define a structure, use the `struct` keyword followed by the name of the structure:

```c#
struct Point
{
    public int X;
    public int Y;
}
```

The above code defines a structure named `Point` with two public fields, `X` and `Y`.

### Creating a Structure

To create an instance of a structure, use the `new` keyword followed by the name of the structure:

```c#
Point point = new Point();
```

The above code creates an instance of the `Point` structure and initializes the `X` and `Y` fields to their default values (0).

### Accessing Structure Members

To access the members of a structure, use the dot operator:

```c#
Console.WriteLine($"X: {point.X}, Y: {point.Y}");
```

The above code prints the values of the `X` and `Y` fields of the `point` structure.

### Example

The following example demonstrates the use of structures:

```c#
struct Point
{
    public int X;
    public int Y;
}

class Program
{
    static void Main(string[] args)
    {
        // Create a Point structure
        Point point = new Point();

        // Set the X and Y fields
        point.X = 10;
        point.Y = 20;

        // Print the X and Y fields
        Console.WriteLine($"X: {point.X}, Y: {point.Y}");
    }
}
```

Output:

```
X: 10, Y: 20
```

## Classes

A class is a blueprint for creating objects. A class defines the properties and methods that an object can have.

### Defining a Class

To define a class, use the `class` keyword followed by the name of the class:

```c#
class Person
{
    public string Name;
    public int Age;
}
```

The above code defines a class named `Person` with two public fields, `Name` and `Age`.

### Creating an Object

To create an instance of a class, use the `new` keyword followed by the name of the class:

```c#
Person person = new Person();
```

The above code creates an instance of the `Person` class and initializes the `Name` and `Age` fields to their default values (null and 0, respectively).

### Accessing Class Members

To access the members of a class, use the dot operator:

```c#
Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
```

The above code prints the values of the `Name` and `Age` fields of the `person` object.

### Example

The following example demonstrates the use of classes:

```c#
class Person
{
    public string Name;
    public int Age;
}

class Program
{
    static void Main(string[] args)
    {
        // Create a Person object
        Person person = new Person();

        // Set the Name and Age properties
        person.Name = "John Doe";
        person.Age = 30;

        // Print the Name and Age properties
        Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
    }
}
```

Output:

```
Name: John Doe, Age: 30
```

---

## Class Functions

Class functions, also known as member functions, are functions that are associated with a particular class. They are used to encapsulate behavior that is specific to that class. Class functions can be accessed through instances of the class.

### Example

The following example defines a class called `Person` with a function called `GetName()`:

```csharp
public class Person
{
    private string name;

    public Person(string name)
    {
        this.name = name;
    }

    public string GetName()
    {
        return name;
    }
}
```

You can use the `GetName()` function by creating an instance of the `Person` class:

```csharp
Person person = new Person("John Doe");
string name = person.GetName();
Console.WriteLine(name); // Output: John Doe
```

## Class Fields

Class fields, also known as member variables, are variables that are associated with a particular class. They are used to store data that is specific to that class. Class fields can be accessed through instances of the class.

### Example

The following example defines a class called `Car` with a field called `make`:

```csharp
public class Car
{
    private string make;

    public Car(string make)
    {
        this.make = make;
    }

    public string GetMake()
    {
        return make;
    }
}
```

You can use the `make` field by creating an instance of the `Car` class:

```csharp
Car car = new Car("Toyota");
string make = car.GetMake();
Console.WriteLine(make); // Output: Toyota
```

## Class Variable/Function Scope

The scope of a class variable or function determines where it can be accessed. There are three types of scope in C#:

* **Instance scope:** Variables and functions that are declared within an instance of a class can only be accessed by that instance.
* **Class scope:** Variables and functions that are declared within a class but outside of an instance can be accessed by all instances of that class.
* **Global scope:** Variables and functions that are declared outside of any class can be accessed by all code in the program.

### Example

The following example demonstrates the different scopes of class variables and functions:

```csharp
public class ScopeTest
{
    public int instanceVariable; // Instance scope

    public static int classVariable; // Class scope

    public void InstanceMethod()
    {
        int localVariable; // Instance scope
    }

    public static void ClassMethod()
    {
        int localVariable; // Class scope
    }
}

public class MainClass
{
    public static void Main(string[] args)
    {
        ScopeTest instance = new ScopeTest();

        instance.instanceVariable = 1; // Instance scope
        ScopeTest.classVariable = 2; // Class scope

        instance.InstanceMethod(); // Instance scope
        ScopeTest.ClassMethod(); // Class scope

        int globalVariable = 3; // Global scope
    }
}
```

### Output

```
1
2
```

---

## Class Properties

Class properties are a concise syntax for defining public fields and methods with full access control. They are declared using the `prop` keyword, followed by the data type and the property name.

```csharp
public class Person
{
    private string _name;

    public string Name
    {
        get { return _name; }
        set { _name = value; }
    }
}
```

The above code defines a class property named `Name`. The property has a private backing field named `_name`. The `get` and `set` accessors provide a means to read and write the property value.

Class properties can be used to enforce business rules and ensure data integrity. For example, the following property validates the `Age` property value before assigning it:

```csharp
public class Person
{
    private int _age;

    public int Age
    {
        get { return _age; }
        set
        {
            if (value < 0 || value > 120)
            {
                throw new ArgumentOutOfRangeException("Age must be between 0 and 120.");
            }

            _age = value;
        }
    }
}
```

Class properties can also be used to provide computed values. For example, the following property calculates the BMI (Body Mass Index) based on the `Height` and `Weight` properties:

```csharp
public class Person
{
    private double _height;
    private double _weight;

    public double Height
    {
        get { return _height; }
        set { _height = value; }
    }

    public double Weight
    {
        get { return _weight; }
        set { _weight = value; }
    }

    public double BMI
    {
        get { return _weight / (_height * _height); }
    }
}
```

## Class ToString Function Override

The `ToString` method is a built-in method that returns a string representation of an object. By default, the `ToString` method returns the fully qualified name of the object's type. However, you can override the `ToString` method to provide a custom string representation.

The following code overrides the `ToString` method to return a comma-separated list of the `Name`, `Age`, and `BMI` properties:

```csharp
public class Person
{
    private string _name;
    private int _age;
    private double _bmi;

    public string Name
    {
        get { return _name; }
        set { _name = value; }
    }

    public int Age
    {
        get { return _age; }
        set { _age = value; }
    }

    public double BMI
    {
        get { return _bmi; }
        set { _bmi = value; }
    }

    public override string ToString()
    {
        return $"{_name}, {_age}, {_bmi}";
    }
}
```

You can use the `ToString` method to display object information in debug logs, user interfaces, and other scenarios where a string representation is required.

## Outro

Class properties and the `ToString` function override are essential features of C# that allow you to create and manipulate objects in a concise and efficient manner. By understanding these concepts, you can write more effective and maintainable C# code.

---
