from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("key2"))
client = genai.Client(api_key=os.getenv("key4"))
chat = client.chats.create(model="gemini-2.5-flash")

data = {
    "AI & MACHINE LEARNING SERVICES": [
        "97. What is Amazon Polly Text-to-Speech Service",
    ],
}

fileName = "AWS.md"


def get_ai_response_google(conversation):
    print("Received a request by google to get AI response.")
    try:
        print(conversation)
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=conversation
        )
        response_text = response.text
        f = open("AWS.md", "a")
        f.write(response_text)
        f.write("\n\n\n")
        f.close()
        print("AI response received.")
        return response_text
    except Exception as e:
        response_data = {"error": f"AI API error: {str(e)}"}
        print(f"AI API error: {str(e)}")
        return response_data


def get_ai_chat_response_google(conversation):
    print("Received a request by google to get AI response.")
    try:
        print(conversation)
        response = chat.send_message(conversation)
        response_text = response.text
        f = open(fileName, "a")
        f.write(response_text)
        f.write("\n\n")
        f.close()
        print("✅ AI response received.")
        return response_text
    except Exception as e:
        response_data = {"error": f"AI API error: {str(e)}"}
        print(f"AI API error: {str(e)}")
        return response_data


def createData():
    for heading, topics in data.items():
        print(f"\n{heading}")
        for i in range(0, len(topics), 2):
            print(topics[i])
            second_topic = ""
            if i + 1 < len(topics):
                print(topics[i + 1])
                second_topic = topics[i + 1]
            text = f"""
Subject: {heading}
Topics:
1. {topics[i]}
2. {second_topic}

Explain these topic in MORE THAN 1000 WORDS, explain EACH topic separately and in simple way with examples Include real-world examples and interview ready answer for every major concept. Include AWS-specific terminology correctly. 

Formatting rules: 
- Each topic MUST be written under an H2 heading (##). 
- Use H3 headings (###) for sub-sections when needed. 
- Use bullet points, numbered lists, flow diagram, and tables. 
- Do NOT repeat the topic list in the answer. 
- Do NOT include introductions or conclusions unless required by the topic.

Output rules: 
- Output ONLY the explanation content. 
- Do NOT add meta commentary. 
- Do NOT say "Sure" or "Here is the explanation".
            """
            input("press enter...")
            get_ai_chat_response_google(text)


def test_ai():
    print("Testing...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents="hi"
        )
        print(response.text)
    except Exception as e:
        print(f"AI API error: {str(e)}")

    # chat
    # chat = client.chats.create(model="gemini-2.5-flash")
    # response = chat.send_message("I have 2 dogs in my house.")
    # print(response.text)
    # response = chat.send_message("How many paws are in my house?")
    # print(response.text)


createData()
# test_ai()