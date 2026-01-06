from google import genai

client = genai.Client(api_key="AIzaSyD40Ph78rlz0g-9VHgX5lpodaAwSTsqztU")
chat = client.chats.create(model="gemini-2.5-flash")

data = {
    "CLOUD COMPUTING FUNDAMENTALS": [
        "1. What is Cloud Computing and How It Works",
        "2. Problems with Traditional On-Premises Infrastructure",
        "3. Benefits of Using Cloud Computing",
        "4. Real-World Examples of Cloud Usage",
        "5. Types of Cloud Computing (Public, Private, Hybrid, Multi-Cloud)",
        "6. Cloud Deployment Models Explained",
        "7. Cloud Service Models Explained (IaaS, PaaS, SaaS)",
    ],
    "AWS OVERVIEW & BASICS": [
        "8. What is Amazon Web Services (AWS)",
        "9. Why AWS is the Leading Cloud Provider",
        "10. Overview of AWS Services and Categories",
    ],
    "AWS GLOBAL INFRASTRUCTURE": [
        "11. What is AWS Global Infrastructure",
        "12. What is an AWS Region and Why It Matters",
        "13. What is an AWS Availability Zone",
        "14. How Availability Zones Provide High Availability",
        "15. What are AWS Edge Locations and CDN Concept",
    ],
    "AWS SHARED RESPONSIBILITY MODEL": [
        "16. What is the AWS Shared Responsibility Model",
        "17. AWS Responsibilities vs Customer Responsibilities",
        "18. Shared Responsibility Model for Compute Services",
        "19. Shared Responsibility Model for Storage Services",
        "20. Shared Responsibility Model for Database Services",
    ],
    "ACCESSING & MANAGING AWS": [
        "21. How to Access AWS (AWS Management Console, CLI, SDK)",
        "22. What is the AWS Management Console",
        "23. What is the AWS Command Line Interface (CLI)",
        "24. What are AWS SDKs and When to Use Them",
    ],
    "COMPUTE SERVICES (SERVERS)": [
        "25. What is Compute in Cloud Computing",
        "26. What is an Amazon EC2 Virtual Server",
        "27. Types of EC2 Instances and Their Use Cases",
        "28. What is an Amazon Machine Image (AMI)",
        "29. How EC2 Key Pairs Work for Secure Access",
        "30. What are Security Groups and How They Protect EC2",
        "31. What is Elastic Load Balancing and Why It Is Needed",
        "32. Types of AWS Load Balancers Explained",
        "33. What is Auto Scaling and How It Works",
        "34. How High Availability and Fault Tolerance Are Achieved",
    ],
    "STORAGE SERVICES": [
        "35. What is Cloud Storage",
        "36. What is Amazon S3 Object Storage",
        "37. How S3 Buckets and Objects Work",
        "38. S3 Storage Classes and Cost Optimization",
        "39. What is S3 Versioning and Lifecycle Management",
        "40. How Security and Access Control Work in S3",
        "41. What is Amazon EBS Block Storage",
        "42. What is Amazon EFS File Storage",
        "43. Difference Between S3, EBS, and EFS",
    ],
    "DATABASE SERVICES": [
        "44. What is a Database and Why Applications Need It",
        "45. Difference Between Relational and Non-Relational Databases",
        "46. What is Amazon RDS Managed Relational Database",
        "47. Supported Database Engines in Amazon RDS",
        "48. What is Amazon Aurora and Why It Is Faster",
        "49. What is Amazon DynamoDB NoSQL Database",
        "50. When to Use DynamoDB vs RDS",
        "51. What is Amazon Redshift Data Warehouse",
        "52. How Backup, Restore, and Disaster Recovery Work",
    ],
    "NETWORKING & CONTENT DELIVERY": [
        "53. What is Networking in Cloud Computing",
        "54. What is an Amazon Virtual Private Cloud (VPC)",
        "55. What are Subnets and Why Public and Private Subnets Are Used",
        "56. What is an Internet Gateway",
        "57. What is a NAT Gateway and Why It Is Required",
        "58. How Route Tables Control Network Traffic",
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
    "AI & MACHINE LEARNING SERVICES": [
        "93. What is Artificial Intelligence and Machine Learning in AWS",
        "94. What is Amazon Rekognition Image and Video Analysis",
        "95. What is Amazon Comprehend Natural Language Processing",
        "96. What is Amazon Lex Chatbot Service",
        "97. What is Amazon Polly Text-to-Speech Service",
    ],
    "INFRASTRUCTURE AS CODE & MANAGEMENT": [
        "98. What is Infrastructure as Code",
        "99. What is AWS CloudFormation and Why It Is Used",
        "100. What is AWS Elastic Beanstalk Application Deployment",
        "101. What is AWS Systems Manager",
    ],
    "DEVOPS & CI/CD": [
        "102. What is DevOps in AWS",
        "103. What is CI/CD Pipeline",
        "104. What is AWS CodeCommit",
        "105. What is AWS CodeBuild",
        "106. What is AWS CodeDeploy",
        "107. What is AWS CodePipeline",
    ],
    "PRICING, BILLING & COST MANAGEMENT": [
        "108. How AWS Pricing Works",
        "109. What is the AWS Free Tier and Its Limits",
        "110. What is On-Demand Pricing",
        "111. What are Reserved Instances",
        "112. What are Savings Plans",
        "113. What are Spot Instances",
        "114. How to Monitor Costs Using AWS Cost Explorer",
        "115. How to Control Costs Using AWS Budgets",
    ],
    "RELIABILITY & ARCHITECTURE BEST PRACTICES": [
        "116. What is Reliability in Cloud Architecture",
        "117. What is the AWS Well-Architected Framework",
        "118. The Five Pillars of the Well-Architected Framework",
        "119. High Availability Design Principles",
        "120. Disaster Recovery Strategies in AWS",
    ],
    "MIGRATION & SUPPORT": [
        "121. What is Cloud Migration",
        "122. Common Cloud Migration Strategies",
        "123. AWS Migration Tools Overview",
        "124. What are AWS Support Plans",
        "125. How to Use AWS Documentation and Whitepapers",
        "126. What is the AWS Cloud Practitioner Certification",
        "127. AWS Cloud Practitioner Exam Structure",
        "128. Real-World AWS Architecture at Beginner Level",
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

            Instructions:
            - Explain EACH topic separately and in simple way with examples.
            - Use an H2 heading for each topic.
            - Do not merge the topics.
            """
            get_ai_chat_response_google(text)


def test_ai():
    print("Testing...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents="How does AI work?"
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


test_ai()
