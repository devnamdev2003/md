import os
import openai


def get_ai_response(user_input):
    print(user_input)
    openai.api_key = os.getenv('OPENAI_KEY')
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for writing a contetn in more than 1000 words"},
            {"role": "user", "content":  user_input}
        ]
    )
    response_text = completion.choices[0].message.content
    print(response_text)
    return response_text


input = """- Introduction about c++
- Your First C++ Program
- Comments
- Errors and Warnings
- Statements and Functions
- Data input and output
- C++ Program Execution Model
- C++ core language Vs Standard library Vs STL
- Variables and data types Introduction
- Number Systems
- Integer types : Decimals and Integers
- Integer Modifiers
- Fractional Numbers
- Booleans
- Characters And Text
- Auto
- Assignments
- Variables and data types summary
- Introduction on Data operations
- Basic Operations
- Precedence and Associativity
- Prefix/Postfix Increment & Decrement
- Compound Assignment Operators
- Relational Operators
- Logical Operators
- Output formatting
- Numeric Limits
- Math Functions
- Weird Integral Types
- Data Operations Summary
- Flow Control Introduction
- If Statements
- Else If
- Switch
- Ternary Operators
- Flow Control Summary
- Loops Introduction
- For Loop
- While Loop
- Do While Loop
- Introduction to Arrays
- Declaring and using arrays
- Size of an array
- Arrays of characters
- Array Bounds
- Introduction to Pointers
- Declaring and using pointers
- Pointer to char
- Program Memory Map Revisited
- Dynamic Memory Allocation
- Dangling Pointers
- When new Fails
- Null Pointer Safety
- Memory Leaks
- Dynamically allocated arrays
- Introduction to References
- Declaring and using references
- Comparing pointers and references
- References and const
- Introduction to Strings
- Character Manipulation
- C-string manipulation
- C-String concatenation and copy
- Introducing std::string
- Declaring and using std::string
- The One Definition Rule
- First Hand on C++ Functions
- Function Declaration and Function Definitions
- Multiple Files - Compilation Model Revisited
- Pass by value
- Pass by pointer
- Pass by reference
- Introduction to getting things out of functions
- Input and output parameters
- Returning from functions by value
- Function Overloading Introduction
- Overloading with different parameters
- Intro to Lambda Functions
- Declaring and using lambda functions
- Capture lists
- Capture all in context
- Summary
- Intro to function templates
- Trying out function templates
- Template type deduction and explicit arguments
- Template parameters by reference
- Template specialization
- Intro to C++20 Concepts
- Using C++20 Concepts
- Building your own C++20 Concepts
- Zooming in on the requires clause
- Combining C++20 Concepts
- C++20 Concepts and auto
- Intro to classes
- Your First Class
- C++ Constructors
- Defaulted constructors
- Setters and Getters
- Class Across Multiple Files
- Arrow pointer call notation
- Destructors
- Order of Constructor Destructor Calls
- The this Pointer
- struct
- Size of objects
- Introduction to Inheritance
- First try on Inheritance
- Protected members
- Base class access specifiers : Zooming in
- Closing in on Private Inheritance
- Resurrecting Members Back in Context
- Default Constructors with Inheritance
- Custom Constructors With Inheritance
- Copy Constructors with Inheritance
- Inheriting Base Constructors
- Inheritance and Destructors
- Reused Symbols in Inheritance
- Introduction to Polymorphism
- Static Binding with Inheritance
- Dynamic binding with virtual functions
- Size of polymorphic objects and slicing
- Polymorphic objects stored in collections (array)
- Override
- Overloading, overriding and function hiding
- Inheritance and Polymorphism at different levels
- Inheritance and polymorphism with static members
- Final
- Virtual functions with default arguments
- Virtual Destructors
- Dynamic casts
- Polymorphic Functions and Destructors
- Pure virtual functions and abstract classes
- Abstract Classes as Interfaces"""
last = """Explain every C++ topic in more than 1000 words with code examples and output. Write content in such a way that you write the topic title as a heading first and then start the explanation."""

input = input.split("\n")
count = 1
it = int(len(input)/5)*5
rem = len(input) % 5
val = ""
for i in range(0, len(input)):
    val = val+input[i]+"\n"
    if count % 5 == 0:
        text = val+last
        with open("cpp_ans.md", "a") as file:
            ans = get_ai_response(text)
            file.write(f"\n\n---\n\n{ans}")
            file.close()
        print("-------------")
        val = ""
    count += 1

if (rem > 0):
    val = ""
    for i in range(it, len(input)):
        val = val+input[i]+"\n"
    with open("cpp_ans.md", "a") as file:
        ans = get_ai_response(val)
        file.write(f"\n\n---\n\n{ans}")
        file.close()
    print("-------------")
