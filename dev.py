import os
# import openai

import os

import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def get_ai_response(conversation):
    print("Received a request by google to get AI response.")
    try:
        print(conversation)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(conversation)
        response_text = response.text
        print("AI response received.")
        return response_text
    except Exception as e:
        response_data = {
            'error': f'AI API error: {str(e)}'
        }
        print(f"AI API error: {str(e)}")
        return response_data


input = """
Introduction
Creating your first project
Hello world
Numeric data types
Text based data types
Converting string to numbers
Boolean data type
Operators
Remainder
Var keyword
Const keyword
Exercise - Storing user data
Exercise - Odd/Even checker
Console Input/Output
If statements
Switch statements
For loops
While loops
Conditional operator
Numeric formatting
TryParse function
Exercise - Times table
Exercise - Fizz buzz game
Verbatim string literal
String formatting
String interpolation
String concatenation
Empty string
String Equals function
String iteration looping
String IsNullOrEmpty function
Exercise - Print string in reverse
Exercise - Password checker
Arrays
Array sorting
Array reversal
Array clearing
Array IndexOf
Lists
Dictionary
Exercise - Odd/Even number split
Exercise - Array of multiples
Functions
Void functions
Return type functions
Function parameters
Optional parameters
Named parameters
Out parameters
Reference parameters
Exercise - Area of a Triangle
Exercise - Sum of int Array
Exception handling
Try…catch
Printing error messages
Exercise - Custom TryParse
Debugging
Local/auto window
Watch window
Exercise - Fix logic error
Structures
Classes
Class functions
Class fields
Class variable/function scope
Class properties
Class ToString function override
Outro
"""
last = """Explain every C# topic in more than 1000 words with code examples and output. Write content in such a way that you write the topic title as a heading first and then start the explanation."""

input = input.split("\n")
count = 1
it = int(len(input))
rem = len(input) % 3
val = ""
for i in range(0, len(input)):
    val = val+input[i]+"\n"
    if count % 3 == 0:
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
