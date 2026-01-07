from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("key2"))
client = genai.Client(api_key=os.getenv("key2"))
chat = client.chats.create(model="gemini-2.5-flash")

data = {
    "NETWORKING & CONTENT DELIVERY": [
        "59. Difference Between Security Groups and Network ACLs",
        "60. What is an Elastic IP Address",
        "61. What is DNS and How It Works",
        "62. What is Amazon Route 53 DNS Service",
    ],
    "IDENTITY & ACCESS MANAGEMENT (IAM)": [
        "63. What is Identity and Access Management (IAM)",
        "64. How Authentication and Authorization Work in AWS",
        "65. What is an IAM User",
        "66. What is an IAM Group",
        "67. What is an IAM Role",
        "68. What are IAM Policies and Permission Boundaries",
        "69. IAM Best Practices for Secure Access",
    ],
    "SECURITY SERVICES": [
        "70. What is Security in the AWS Cloud",
        "71. How AWS Secures Infrastructure",
        "72. What is AWS Shield for DDoS Protection",
        "73. What is AWS WAF Web Application Firewall",
        "74. What is Amazon GuardDuty Threat Detection",
        "75. What is Amazon Inspector Security Assessment",
        "76. What is AWS Key Management Service (KMS)",
        "77. How Data Encryption Works at Rest and In Transit",
    ],
    "MONITORING, LOGGING & GOVERNANCE": [
        "78. What is Monitoring and Observability in AWS",
        "79. What is Amazon CloudWatch",
        "80. How CloudWatch Metrics and Alarms Work",
        "81. How CloudWatch Logs Are Used",
        "82. What is AWS CloudTrail and API Auditing",
        "83. What is AWS Config and Resource Compliance",
    ],
    "APPLICATION INTEGRATION & MESSAGING": [
        "84. What is Application Integration in AWS",
        "85. What is Amazon SQS Message Queue Service",
        "86. What is Amazon SNS Notification Service",
        "87. Difference Between Messaging and Event-Driven Systems",
        "88. What is Amazon EventBridge",
    ],
    "ANALYTICS SERVICES": [
        "89. What is Analytics in AWS",
        "90. What is Amazon Athena Query Service",
        "91. What is AWS Glue Data Integration Service",
        "92. What is Amazon QuickSight BI Tool",
    ],
}

fileName = "AWS3.md"


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
        f.write("\n\n\n")
        f.close()
        print("AI response received.")
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