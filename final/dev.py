import os

import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def get_ai_response_google(conversation):
    print("Received a request by google to get AI response.")
    try:
        print(conversation)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(conversation)
        response_text = response.text
        f = open("gt.md", "a")
        f.write(response_text)
        f.write("\n\n\n")
        f.close()
        print("AI response received.")
        return response_text
    except Exception as e:
        response_data = {
            'error': f'AI API error: {str(e)}'
        }
        print(f"AI API error: {str(e)}")
        return response_data


gt = [
    'Explain What is a Game',
    'Explain Game Design Schema',
    'Explain Game Design fundamentals',
    'Explain Engineering application of game theory',
    'Explain Design Process: Iterative design, Commissions',
    'Explain Design & Testing of the Board Game',
    'Explain Introduction to meaningful play',
    'Explain two kinds of meaningful play- discernable & integrated.'
    'Explain Introducing design, design & meaning',
    'Explain Semiotics: A brief overview',
    'Explain four semiotic Concepts',
    'Explain Context Shapes interpretations.',
    'Explain Introduction to Systems',
    'Explain elements of a System',
    'Explain Framing Systems',
    'Explain open & closed systems',
    'Explain Introduction to Interactivity',
    'Explain a multivalent model of interactivity',
    'Explain interaction & choice',
    'Explain choice molecules, anatomy of choice',
    'Explain space of possibility',
    'Expalin overview of digital games',
    'Expalin magic circle',
    'Expalin Primary Schemas: conceptual framework, rule, play, culture.',
    'Expalin Rules: defining rules, a deck of cards, quality of rules, rules in context, Rules on three',
    'Expalin levels: Operational, Constituative, Implicit, Identity of a Game, Specificity of Rules,',
    'Expalin Rules of Digital games.',
    'Expalin Case Studies: Tic Tac Toe, Deck of Cards.']


iot = ['Explain IoT definition, Characteristics',
       'Explain IoT conceptual and architectural framework',
       'Explain Components of IoT ecosystems',
       'Explain Physical and logical design of IoT',
       'Explain IoT enablers',
       'Explain Modern day IoT applications',
       'Explain M2M communications',
       'Explain IoT vs M2M',
       'Explain IoT vs WoT',
       'Explain IoT reference architecture',
       'Explain IoT Network configurations',
       'Explain IoT LAN',
       'Explain IoT WAN',
       'Explain IoT Node',
       'Explain IoT Gateway',
       'Explain IoT Proxy',
       'Explain Review of Basic Microcontrollers and interfacing',
       'Explain Define Sensor',
       'Explain Basic components and challenges of a sensor node',
       'Explain Sensor features',
       'Explain Sensor resolution',
       'Explain Sensor classes: Analog, Digital, Scalar, Vector Sensors;',
       'Explain Sensor Types',
       'Explain bias, drift, Hysteresis error, quantization error;',
       'Explain Actuator',
       'Explain Actuator types: Hydraulic, Pneumatic, electrical, thermal/magnetic, mechanical actuators, soft actuators',
       'Explain Basics of IoT Networking',
       'Explain IoT Components',
       'Explain Functional components of IoT',
       'Explain IoT service oriented architecture',
       'Explain IoT challenges',
       'Explain 6LowPAN',
       'Explain IEEE 802.15.4',
       'Explain ZigBee and its types',
       'Explain RFID, Features',
       'Explain RFID working principle and applications',
       'Explain NFC (Near Field communication)',
       'Explain Bluetooth, Wireless Sensor Networks and its Applications',
       'Explain MQTT',
       'Explain MQTT methods and components',
       'Explain MQTT communication, topics and applications',
       'Explain SMQTT',
       'Explain CoAP',
       'Explain CoAP message types',
       'Explain CoAP Request-Response model',
       'Explain XMPP',
       'Explain AMQP features and components',
       'Explain AMQP frame types',
       'Explain IoT Platforms, Arduino, Raspberry Pi Board, Other IoT Platforms',
       'Explain Data Analytics for IoT, Cloud for IoT, Cloud storage models & communication APIs',
       'Explain Attacks in IoT system',
       'Explain vulnerability analysis in IoT',
       'Explain IoT case studies: Smart Home, Smart framing etc.'
       ]

cc = [
    ' explain Service Oriented Architecture',
    ' explain Web Services',
    ' explain Basic Web Services Architecture',
    ' explain SOAP',
    ' explain WSDL and UDDI',
    ' explain REST ful services and its Characteristics, Components, Types',
    ' Explain Software as a Service',
    ' Explain Plat form as a Service',
    ' Explain Organizational scenarios of clouds',
    ' Explain Administering & Monitoring cloud services and its benefits and limitations',
    ' Explain Study of a Hypervisor.',
    ' Explain Utility Computing',
    ' Explain Elastic Computing',
    ' Explain Ajax: asynchronous ‘rich’ interfaces',
    ' Explain Mashups:  User interface',
    ' Explain Services Virtualization Technology: Virtualization applications in  enterprises',
    ' Explain Pitfalls of virtualization Multitenant software: Multi-entity support, Multischema approach',
    ' Explain Multi-tenancy using cloud data stores.',
    ' Explain Data in the cloud: Relational databases',
    ' Explain Cloud file systems: GFS and HDFS and its features and comparisons among GFS, HDFS etc',
    ' Explain Big Table',
    ' Explain H Base and Dynamo. Map-Reduce and extensions: Parallel computing',
    ' Explain The Map-Reduce model: Parallel efficiencyofMapReduce, Relationaloperations, Enterprisebatchprocessing',
    ' Explain Example/Application of MapReduce',
    ' Explain Cloud security fundamentals',
    ' Explain Vulnerability assessment tool for cloud',
    ' Explain Privacy and Security in cloud: Cloud computing security architecture, General Issues',
    ' Explain Trusted Cloud computing',
    ' Security challenges: Virtualization security management-virtual threats',
    ' VM Security Recommendations',
    ' VM-Specific Security techniques',
    ' Secure Execution Environments and Communications in cloud',
    ' Explain Issues in cloud computing; implementing real time application',
    ' Explain QOS Issues in Cloud, Dependability',
    ' Explain data migration',
    ' Explain streaming in Cloud. Cloud Middleware. Mobile Cloud Computing. Inter Cloud issues. Agrid of clouds',
    ' Explain Sky computing',
    ' Explain load balancing',
    ' Explain Resource optimization',
    ' Explain Resource dynamic reconfiguration',
    ' Explain Monitoring in Cloud',
    ' Installing cloud platforms and performance evaluation',
    ' Features and functions of cloud computing platforms. ']
print(len(iot))
# Custom increment of 2
for i in range(0, len(iot), 2):
    text=f"""
    Subject: internet of things
    Topics:
        1. {iot[i]}
        2. {iot[i+1]}

    Explain each topic in more than 1000 words. and wrtie in a way so each topic in h2 heading
    """
    get_ai_response_google(text)
    print(i)

print(len(cc))
# Custom increment of 2
for i in range(0, len(cc), 2):
    text=f"""
    Subject: Cloud computing
    Topics:
        1. {cc[i]}
        2. {cc[i+1]}

    Explain each topic in more than 1000 words. and wrtie in a way so each topic in h2 heading
    """
    get_ai_response_google(text)
    print(i)

print(len(gt))
# Custom increment of 2
for i in range(0, len(gt), 2):
    text=f"""
    Subject: Game Theory with Engineering applications
    Topics:
        1. {gt[i]}
        2. {gt[i+1]}

    Explain each topic in more than 1000 words. and wrtie in a way so each topic in h2 heading
    """
    get_ai_response_google(text)
    print(i)


# text=f"""
#     Subject: Game Theory with Engineering applications
#     Topics:
#         1. Expalin Case Studies: Tic Tac Toe, Deck of Cards.

#     Explain each topic in more than 1000 words. and wrtie in a way so each topic in h2 heading
#     """
# get_ai_response_google(text)
