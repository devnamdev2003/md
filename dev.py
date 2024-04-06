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


input = """"""
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
