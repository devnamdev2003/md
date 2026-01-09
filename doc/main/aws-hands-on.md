<link rel="stylesheet" href="https://devnamdev2003.github.io/md/static/style.css">

# 🧭 COMPLETE AWS EC2 HANDS-ON ROADMAP

## 🧪 EC2 HANDS-ON – LAB 1

### 👉 Launch Your First EC2 Instance (Free Tier – SAFE)

### 🎯 Objective

You will:

* Launch a **Free Tier EC2 instance**
* Understand **AMI, instance type, key pair, security group**
* Get a **public IP**

---

### 🧠 Before You Start (Very Important)

* Login to **Amazon Web Services Management Console**
* Make sure you are in **ONE region** (example: `ap-south-1 (Mumbai)`)

👉 **Region matters** because:

* EC2 runs inside a region
* Free tier limits are per region

---

### 🔹 STEP 1: Go to EC2 Dashboard

1. Login to AWS Console
2. In the **search bar**, type: `EC2`
3. Click **EC2**

📌 You are now inside the EC2 service

---

### 🔹 STEP 2: Click “Launch Instance”

1. Click **Launch Instance**
2. You will see a **Launch Instance** page

---

### 🔹 STEP 3: Name Your Instance

* Instance name:

  ```
  ec2-hands-on-1
  ```

📌 This is just a **label** to identify your server

---

### 🔹 STEP 4: Choose AMI (Operating System)

Select:

* **Amazon Linux 2023 AMI**

📌 Why?

* Free tier eligible
* Optimized for AWS
* Secure and lightweight

✅ Do **NOT** choose Ubuntu for now

---

### 🔹 STEP 5: Choose Instance Type

Select:

* **t2.micro**

📌 Why?

* 1 vCPU
* 1 GB RAM
* **FREE TIER ELIGIBLE**

⚠️ Anything else = billing risk

---

### 🔹 STEP 6: Create Key Pair (VERY IMPORTANT)

Key pair = **login password for your server**

1. Click **Create new key pair**
2. Key pair name:

   ```
   ec2-key-hands-on
   ```
3. Key pair type: **RSA**
4. Private key format: **.pem**
5. Click **Create key pair**

📌 A `.pem` file will download
⚠️ **DO NOT DELETE IT**
Without this, you **cannot login**

---

### 🔹 STEP 7: Configure Network Settings (Security Group)

Click **Edit** under Network settings

### Inbound rules (ALLOW ACCESS):

| Type | Port | Source   |
| ---- | ---- | -------- |
| SSH  | 22   | My IP    |
| HTTP | 80   | Anywhere |

📌 Explanation:

* **SSH (22)** → Login to EC2
* **HTTP (80)** → Web server access
* **My IP** → Secure (only your system)
* **Anywhere** → Public website access

---

### 🔹 STEP 8: Storage (Leave Default)

* 8 GiB (gp3) → Leave as it is

📌 Free tier allows up to **30 GB**

---

### 🔹 STEP 9: Launch Instance

1. Review everything
2. Click **Launch Instance**
3. Click **View all instances**

---

### 🔹 STEP 10: Verify Instance Status

Your instance state should be:

* 🟡 Initializing
* 🟢 **Running**

Click your instance and check:

* **Instance State** → Running
* **Public IPv4 address** → COPY IT

📌 This IP is your **server on the internet**

---

### ✅ TASK FOR YOU (DO THIS NOW)

✔ Launch EC2 instance
✔ Instance state = **Running**
✔ You can see **Public IPv4 address**

---


Excellent 👍
**LAB 1 completed successfully** ✅
Now we move to the **next hands-on**, exactly as promised.

---

## 🧪 EC2 HANDS-ON – LAB 2

### 👉 Connect to EC2 using SSH 

![Image](https://miro.medium.com/1%2AB6_U18PU0UYWOgbsDQbzxg.png)

![Image](https://cloudonaut.io/images/2022/02/ec2-ssh-ic-ssm.png)


---

### 🎯 Objective of This Lab

You will:

* Connect to your EC2 instance **from your Windows laptop**
* Understand **SSH**, **key pair**, **user**, **IP**
* Login **successfully** without fear or confusion

---

### 🧠 Important Concepts

Before doing steps, understand this:

### 🔹 What is SSH?

**SSH (Secure Shell)** is a secure way to:

* Connect your laptop → EC2 server
* Run commands on the server

Think like this:

> SSH = Remote control of your EC2 using text commands

---

### 🔹 What do we need for SSH?

We need **4 things**:

1. **Public IP** → Address of your EC2
2. **Key pair (.pem file)** → Password (but more secure)
3. **Username** → Depends on OS
4. **SSH command**

---

### 🔹 STEP 1: Open PowerShell (Windows)

1. Press **Windows key**
2. Type: `PowerShell`
3. Open **Windows PowerShell**

📌 Do **NOT** open CMD
PowerShell supports SSH by default

---

### 🔹 STEP 2: Go to Folder Where `.pem` File Exists

Your key file name:

```
ec2-key-hands-on.pem
```

Usually it is in **Downloads** folder.

### Run this command:

```powershell
cd Downloads
```

📌 Explanation:

* `cd` = change directory
* `Downloads` = folder name

To confirm file exists, run:

```powershell
ls
```

📌 `ls` shows list of files
You should see:

```
ec2-key-hands-on.pem
```

---

### 🔹 STEP 3: Copy Your EC2 Public IP

1. Go to EC2 Console
2. Click your instance
3. Copy **Public IPv4 address**

Example:

```
13.235.xxx.xxx
```

---

### 🔹 STEP 4: Understand the SSH Command (IMPORTANT)

### SSH command format:

```powershell
ssh -i keyfile.pem username@public-ip
```

Now replace values 👇

| Part      | Value                  |
| --------- | ---------------------- |
| keyfile   | `ec2-key-hands-on.pem` |
| username  | `ec2-user`             |
| public-ip | your EC2 IP            |

📌 **Why `ec2-user`?**
Because you selected **Amazon Linux AMI**

---

### 🔹 STEP 5: Connect to EC2 (RUN THIS)

```powershell
ssh -i ec2-key-hands-on.pem ec2-user@YOUR_PUBLIC_IP
```

Example:

```powershell
ssh -i ec2-key-hands-on.pem ec2-user@13.235.xxx.xxx
```

---

### 🔹 STEP 6: Type “yes” (First Time Only)

You will see:

```
Are you sure you want to continue connecting (yes/no)?
```

Type:

```
yes
```

Press **Enter**

📌 This happens only once
It means: “I trust this server”

---

### 🎉 SUCCESS CHECK (VERY IMPORTANT)

If you see something like:

```
[ec2-user@ip-172-31-xx-xx ~]$
```

✅ **YOU ARE INSIDE EC2 SERVER**

This means:

* Your laptop → connected to AWS server
* SSH is working
* Key pair is correct

---

### 🔍 Verify You Are Really Inside EC2

Run:

```bash
whoami
```

Output should be:

```
ec2-user
```

Run:

```bash
pwd
```

Output:

```
/home/ec2-user
```

---


### ✅ TASK FOR YOU (LAB 2)

✔ Open PowerShell

✔ SSH into EC2

✔ See `[ec2-user@...]$` prompt

✔ Run `whoami`

---



## 🔑 What is a Key Pair in EC2? 

A **Key Pair** is like a **lock and key** 🔐

* **Public key** → Stored inside the EC2 instance (AWS keeps it)
* **Private key** → Downloaded by **you** (file like `.pem` or `.ppk`)

This key pair is used to **log in securely** to your EC2 instance.

👉 **Without a key pair, you CANNOT login to EC2**

---

### 🧭 When You Create a Key Pair – What Options You See

When you click **Create new key pair**, AWS shows **2 main options**:

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20230309161715/IMG_20230309_161526-768.png)

---

### 1️⃣ Key Pair Type

You will see **two options**:

### 🔹 RSA (Most common ✅)

* Old but very stable
* Supported everywhere
* Default choice

👉 **Use this if you are a beginner**

### 🔹 ED25519

* Newer & more secure
* Faster
* Not supported by some old systems

👉 Use this **only if you clearly know you need it**

✅ **Recommended for you:** `RSA`

---

### 2️⃣ Private Key File Format (MOST IMPORTANT)

This is where people get confused 👇

You will see **two options**:

---

### 🔹 `.pem` file (Linux / Mac / Git Bash)

**Use this when:**

* EC2 OS is **Amazon Linux / Ubuntu**
* You connect using:

  * Git Bash
  * MobaXterm
  * Mac Terminal
  * Linux Terminal


---

### 🔹 `.ppk` file (Windows – PuTTY)

**Use this when:**

* You use **PuTTY** on Windows
* You don’t want to convert `.pem` to `.ppk`

Used directly in **PuTTY → Auth → Private key file**

---

### 🧠 Very Important Rule (Remember This)

| Your Tool            | Choose This |
| -------------------- | ----------- |
| Git Bash / MobaXterm | `.pem`      |
| Mac / Linux Terminal | `.pem`      |
| PuTTY (Windows)      | `.ppk`      |

👉 If confused → **Always choose `.pem`**
You can later convert `.pem → .ppk`, but not easily the other way.

---

### ❗ IMPORTANT WARNINGS (Real-life mistakes)

⚠️ **Download key only ONCE**

* AWS will **never show it again**
* If you lose it → You lose access

⚠️ **Do NOT share your private key**

* Anyone with this file can access your server

⚠️ **Do NOT upload key to GitHub**

* This is a serious security risk

---

### 🧠 Short Memory Trick

> **Linux server = `.pem`**
> **PuTTY user = `.ppk`**

---



## 🔐 What “Key Pair” Means Internally (Big Picture)

An EC2 key pair uses **asymmetric encryption**.

That means:

* 🔑 **Public Key** → stored on the EC2 server
* 🗝️ **Private Key** → stored ONLY with you
* They work **together**, not separately

Think of it like:

> **Public key = Lock**
> **Private key = Only key that can open that lock**

---

### 🧠 Step-by-Step: What Happens Internally


![Image](https://comodosslstore.com/blog/wp-content/uploads/2018/04/public-key-vs-private-key.png)



### When EC2 instance is launched:

* The **public key** is copied into the server file:

```text
~/.ssh/authorized_keys
```

This file lives **inside the EC2 instance**.

👉 This file decides **who is allowed to log in**.

---

### 🟢 You try to connect (SSH)

You run:

```bash
ssh -i mykey.pem ec2-user@<public-ip>
```

What happens internally:

1. You say: *“Hey server, I want to login”*
2. Server says: *“Prove you are authorized”*

---

### 🟢 Server sends a challenge 🔒

The EC2 server:

* Creates a **random encrypted message**
* Encrypts it using the **public key**
* Sends it to your system

⚠️ Important:

* **Only the matching private key can decrypt it**

---

### 🟢 Step 5: Your private key responds 🔓

Your computer:

* Uses your **private key**
* Decrypts the message
* Sends the correct response back

---

### 🟢 Step 6: Server verifies and allows login ✅

Server checks:

* “Does this response match what I expected?”

If **YES**:

* Login allowed 🎉

If **NO**:

* ❌ Permission denied

---

### 🔄 Internal Flow (Very Simple)

```
You (Private Key)
        ↓
Decrypt challenge
        ↓
Send proof
        ↓
EC2 checks using Public Key
        ↓
Login allowed
```

---

### 🔐 Why Password Is NOT Used

EC2 does **NOT** use passwords by default because:

❌ Passwords can be:

* Brute-forced
* Stolen
* Guessed

✅ Keys are:

* Very long
* Mathematically linked
* Impossible to guess

---

### 🔥 What If Someone Gets Public Key?

Nothing happens.

✔️ Public key:

* Can be shared
* Is useless without private key

❌ Private key:

* MUST be protected
* Gives full access

---

### 🧨 What If You Lose the Private Key?

Internally:

* Server has the public key
* You don’t have the private key
* Authentication fails forever ❌

Result:

* You cannot login
* You must:

  * Detach root volume
  * Attach to another EC2
  * Add a new public key manually


---

### 🧠 One-Line Summary (Interview Ready)

> **EC2 uses SSH key-based authentication where the public key is stored on the server and the private key proves the client’s identity without ever being sent over the network.**

---

### 🧪 Real-World Analogy

* Public key → Lock on your house
* Private key → Actual key in your pocket
* SSH login → Trying to open the door

---

## 🧪 EC2 HANDS-ON – LAB 3

### 👉 Install Apache Web Server & Host Your First Website

![Image](https://miro.medium.com/1%2AUdXC594q9XxYneb4yqze_A.png)

---

### 🎯 Objective of This Lab

You will:

* Install **Apache (httpd)** on EC2
* Start the web server
* Host a simple web page
* Access it using **browser + public IP**

---

### 🧠 Important Concept (Simple Words)

### 🔹 What is Apache?

**Apache (httpd)** is a **web server**.

Meaning:

* It listens on **port 80**
* When someone opens your IP in browser
* Apache sends a **web page**

---

### 🔹 STEP 1: Update Your EC2 Server

Run this command:

```bash
sudo dnf update -y
```

📌 Explanation:

* `sudo` → run command as admin (root)
* `dnf` → package manager (like Play Store)
* `update` → update system packages
* `-y` → auto-approve (no questions)

---

### 🔹 STEP 2: Install Apache (httpd)

Run:

```bash
sudo dnf install httpd -y
```

📌 Explanation:

* `install` → install software
* `httpd` → Apache web server package

---

### 🔹 STEP 3: Start Apache Server

```bash
sudo systemctl start httpd
```

📌 Explanation:

* `systemctl` → service manager
* `start` → start service
* `httpd` → Apache service

---

### 🔹 STEP 4: Enable Apache on Boot (VERY IMPORTANT)

```bash
sudo systemctl enable httpd
```

📌 Why?

* If EC2 restarts
* Apache starts automatically

---

### 🔹 STEP 5: Check Apache Status

```bash
sudo systemctl status httpd
```

You should see:

```
Active: active (running)
```

Press:

```
q
```

to exit status screen

---

### 🔹 STEP 6: Test in Browser (BIG MOMENT 🎉)

1. Copy your **EC2 Public IP**
2. Open browser
3. Paste:

```
http://YOUR_PUBLIC_IP
```

### Expected Result:

🟢 **Apache Test Page**

✅ This means:

* EC2 is running
* Apache is working
* Security group allows HTTP (port 80)

---

### 🔹 STEP 7: Create Your Own Web Page

Apache default folder:

```
/var/www/html
```

### Go to folder:

```bash
cd /var/www/html
```

---

### 🔹 STEP 8: Create HTML File

```bash
sudo nano index.html
```

📌 `nano` = simple text editor

Paste this:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First EC2 Website</title>
</head>
<body>
  <h1>Hello from EC2 🚀</h1>
  <p>Apache Web Server is working!</p>
</body>
</html>
```

### Save & Exit:

* Press **CTRL + X**
* Press **Y**
* Press **Enter**

---

### 🔹 STEP 9: Refresh Browser

Open again:

```
http://YOUR_PUBLIC_IP
```

🎉 You should see **your own website**

---

### 🛑 COMMON ISSUE CHECK

If page does not open:

* Check **Security Group → HTTP (80) allowed**
* Instance state = **Running**
* Apache status = **active**

---

### ✅ TASK FOR YOU (LAB 3)

✔ Apache installed
✔ Apache running
✔ Custom HTML page created
✔ Website opens using public IP

---

## 🧪 EC2 HANDS-ON – LAB 4

### 👉 Elastic IP (Static Public IP) – No More IP Changes

![Image](https://www.turnkeylinux.org/files/images/01_Elastic_IP_addresses_EC2_Console.png)

---

### 🎯 Objective of This Lab

You will:

* Understand **why public IP changes**
* Create an **Elastic IP (EIP)**
* Attach it to your EC2 instance
* Access your website using a **fixed IP**

---

### 🧠 Why Public IP Changes? (Simple Explanation)

>Because the public IP is temporary unless you reserve it.

- AWS gives you a temporary public IP by default.

- When the instance stops and restarts, that IP is taken back by AWS.

❌ Bad for:

* Websites
* APIs
* Domain mapping
 
### 🚨 IMPORTANT RULE (Remember This)

|Action	| Public IP|
|---	|---|
|Reboot EC2 |	❌ Does NOT change|
|Stop EC2 |	✅ Changes|
|Terminate EC2 |	❌ Instance gone|
|Start EC2 |	✅ New IP|

---

💰 Cost:
👉 ~$0.005 per hour per Elastic IP

### 🧠 What is Elastic IP?

**Elastic IP (EIP)** is:

* A **static public IPv4 address**
* Belongs to **your AWS account**
* You can attach/detach to EC2

Think like:

> Elastic IP = Permanent phone number 📱
> Public IP = Temporary number

---

### ⚠️ Cost Warning (IMPORTANT)

* **Free** when attached to **running EC2**
* **Charged** if:

  * Not attached
  * Instance stopped

👉 We will keep it **attached**

---

### 🔹 STEP 1: Go to Elastic IPs

1. Open **EC2 Console**
2. Left menu → **Elastic IPs**
3. Click **Allocate Elastic IP address**

---

### 🔹 STEP 2: Allocate Elastic IP

* Network border group → **Leave default**
* Click **Allocate**

You will now see a new **Elastic IP**

---

### 🔹 STEP 3: Associate Elastic IP to EC2

1. Select Elastic IP
2. Click **Actions → Associate Elastic IP**
3. Resource type → **Instance**
4. Instance → select `ec2-hands-on-1`
5. Click **Associate**

---

### 🔹 STEP 4: Verify Association

* Elastic IP shows:

  * Instance ID
  * Private IP

Your EC2 now has:

* **Static public IP**

---

### 🔹 STEP 5: Test Website Using Elastic IP

Open browser:

```
http://ELASTIC_IP
```

🟢 Your website should load

---

### 🔹 STEP 6: Confirm IP Stability (Understanding)

If you:

* Restart EC2 ❌ (DON’T DO NOW)
* Elastic IP **will NOT change**

---

### 🛑 IMPORTANT RULE

If you ever:

* **Terminate EC2**
  👉 First **release Elastic IP**
  Otherwise AWS will charge

---

### ✅ TASK FOR YOU (LAB 4)

✔ Elastic IP allocated
✔ Elastic IP associated to EC2
✔ Website opens using Elastic IP

---

## 🧪 EC2 HANDS-ON – LAB 5

### 👉 Attach a Domain to EC2 using Route 53 (Real-World Hosting)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/1%2ArusHUrFBnPFcD6esjWZB1Q.png)

---

### 🎯 Objective of This Lab

You will:

* Understand **DNS & Domain flow**
* Create a **Hosted Zone** in Route 53
* Map your **Elastic IP → Domain**
* Open your website using a **domain name** 🎉

---

### 🧠 First: Understand the Flow (VERY IMPORTANT)

When someone types:

```
www.example.com
```

What happens?

1. Browser asks **DNS**
2. DNS replies → **Elastic IP**
3. Elastic IP points → **EC2**
4. Apache sends the website

👉 **Route 53 = DNS service**

---

### 🧠 What is Route 53?

**Amazon Route 53** is:

* AWS DNS service
* Converts **domain → IP address**
* Highly available & fast

---

### ⚠️ IMPORTANT NOTE (READ CAREFULLY)

There are **TWO CASES**:

#### ✅ Case 1: You already bought a domain

(from GoDaddy / Namecheap / Route 53)

→ Continue with this lab

#### ❌ Case 2: You don’t have a domain yet

→ You can still **practice** using a fake domain name
(no website will open publicly, but concept is same)

I’ll explain **both safely**.

---

### 🔹 STEP 1: Open Route 53

1. AWS Console → search **Route 53**
2. Open **Route 53**
3. Click **Hosted zones**
4. Click **Create hosted zone**

---

### 🔹 STEP 2: Create Hosted Zone

#### Fill details:

* **Domain name**
  Example:

  ```
  devcloudpractice.com
  ```

* **Type**
  → **Public Hosted Zone**

Click **Create hosted zone**

📌 Hosted Zone = DNS control panel for your domain

---

### 🔹 STEP 3: Understand Name Servers (CRITICAL)

After creation, you’ll see **4 NS records**, like:

```
ns-123.awsdns-45.com
ns-678.awsdns-90.net
...
```

📌 These are **AWS DNS servers**

---

### 🔹 STEP 4: Update Name Servers (Only if Domain Bought Outside AWS)

If your domain is from:

* GoDaddy
* Namecheap
* Hostinger

#### Go to domain provider:

1. Open DNS / Nameserver settings
2. Replace existing name servers
3. Paste **Route 53 name servers**
4. Save

⏳ DNS propagation: **5–30 minutes (sometimes 24 hrs)**

⚠️ If domain bought from Route 53 → **skip this step**

---

### 🔹 STEP 5: Create A Record (Domain → EC2)

Inside Hosted Zone:

1. Click **Create record**
2. Record type → **A**
3. Record name:

   * Leave empty → root domain
     (`example.com`)
4. Value:

   * Paste **Elastic IP**
5. TTL → default
6. Click **Create records**

📌 A record = maps domain → IP

---

### 🔹 STEP 6: (Optional) Create www Record

Create another record:

* Record name:

  ```
  www
  ```
* Type → A
* Value → Elastic IP

This enables:

```
www.example.com
```

---

### 🔹 STEP 7: Test Your Domain 🎉

Open browser:

```
http://yourdomain.com
```

or

```
http://www.yourdomain.com
```

🟢 Your EC2 website should load

---

### 🧠 Real-World Knowledge (Interview Ready)

✔ Route 53 does **not host websites**
✔ It only does **DNS resolution**
✔ EC2 + Apache hosts the website
✔ Elastic IP ensures static mapping

---

### 🛑 Common Issues Checklist

| Issue            | Fix                      |
| ---------------- | ------------------------ |
| Site not opening | Wait DNS propagation     |
| IP wrong         | Check Elastic IP         |
| Apache down      | `systemctl status httpd` |
| HTTP blocked     | Security Group port 80   |

---

### ✅ TASK FOR YOU (LAB 5)

✔ Hosted Zone created
✔ A record added
✔ Domain mapped to Elastic IP

---

## 🔐 EC2 Security Group – SSH, Ports, and IP Access 

---

### 1️⃣ What is a Security Group in EC2?

* A **Security Group** is a **virtual firewall**
* It controls:

  * **Who can reach your EC2 instance**
  * **On which port**
* It works at **network level (before login)**

👉 If traffic is **not allowed** by Security Group → EC2 never receives it.

---

### 2️⃣ What does `0.0.0.0/0` mean?

```
0.0.0.0/0 = ANY IP address on the internet
```

⚠️ This means **publicly open to the world**.

---

### 3️⃣ What does “My IP” mean?

When you select **My IP**, AWS:

* Detects your **current public internet IP**
* Sets the rule as:

```
x.x.x.x/32
```

`/32` means:

* Only **ONE exact IP**
* Only **your current network**

👉 This is **secure and recommended**.

---

### 4️⃣ Understanding the 3 Important Ports

#### 🔐 Port 22 – SSH

**Used for:**

* Remote login to EC2
* Full server control (admin access)

**What SSH gives:**

* File access
* Command execution
* Full OS control

👉 **This is the most sensitive port**

---

#### 🌐 Port 80 – HTTP

**Used for:**

* Website access via browser
* Public web traffic

**What HTTP gives:**

* Only what your application exposes
* No OS access
* No command execution

👉 **Designed to be public**

---

#### ⚙️ Port 8080 – Application Port

**Used for:**

* Spring Boot
* Node.js
* Test applications

**Access level:**

* Application only
* Not OS-level

👉 Safe for testing, risky if admin APIs are exposed

---

### 5️⃣ Why ONLY SSH is dangerous when open to `0.0.0.0/0`

#### Key reason:

> **SSH provides full administrative access to the server**

Comparison:

| Port      | Access Type      | Risk        |
| --------- | ---------------- | ----------- |
| 22 (SSH)  | Full OS control  | 🔥 Very High |
| 80 (HTTP) | Web content only | 🟢 Low       |
| 8080      | App-level access | 🟡 Medium    |

👉 **Admin access should never be public**

---

### 6️⃣ What happens if SSH is set to `0.0.0.0/0`

#### Important clarification:

❌ Anyone **CANNOT login without `.pem` key**

✅ Anyone **CAN try to connect**

#### What attackers can do:

* Scan your public IP
* Detect open port 22
* Attempt:

  * Usernames
  * Stolen keys
  * Brute-force attacks

Even if they fail:

* Continuous attack attempts
* Log flooding
* Resource usage
* High security risk

---

### 7️⃣ Two Levels of EC2 Security (Very Important)

#### Level 1️⃣: Security Group (Network Gate)

* Controls **who can reach the port**

#### Level 2️⃣: SSH Authentication (Login Lock)

* Requires:

  * Correct username
  * Correct private key (`.pem`)

👉 `0.0.0.0/0` opens the **gate**, not the **lock**

---

### 8️⃣ Why `.pem` key is still required

* EC2 uses **key-based authentication**
* Password login is disabled by default
* Private key is never sent over the network

So:

* ❌ No `.pem` → No login
* ❌ Even AWS can’t login without it

---

### 9️⃣ Recommended Safe Configuration

| Port      | Source                | Status           |
| --------- | --------------------- | ---------------- |
| 22 (SSH)  | My IP                 | ✅ Secure         |
| 80 (HTTP) | 0.0.0.0/0             | ✅ Required       |
| 8080      | 0.0.0.0/0 (temporary) | ⚠️ OK for testing |

---

### 🔐 Golden Security Rule (Must Remember)

> **Never expose administrative access (SSH) to the public internet.**

* SSH → restrict to your IP
* HTTP/HTTPS → public
* App ports → open only if needed


---

### 🎯 Interview-Ready One-Line Answer

> **Opening SSH to 0.0.0.0/0 allows anyone on the internet to attempt connections, increasing attack risk. SSH must be restricted to trusted IPs, while HTTP is designed for public access.**

---

## 🧪 EC2 HANDS-ON – LAB 6

### 👉 Security Groups (Inbound & Outbound Rules – Deep Hands-On)

![Image](https://docs.aws.amazon.com/images/vpc/latest/userguide/images/security-group-referencing.png)


---

### 🎯 Objective of LAB 6

By the end of this lab, you will:

* **Create & modify Security Group rules**
* Understand **Inbound vs Outbound**
* Prove that **Security Groups are STATEFUL**
* Be able to **explain this confidently in interviews**

---

### 🧠 FIRST: What is a Security Group? (Very Simple)

A **Security Group (SG)** is:

* A **virtual firewall**
* Controls **who can access your EC2**
* Works at **instance level**

Think like this:

> Security Group = Security guard at the door 🚪
> Only allowed people can enter

---

### 🧠 IMPORTANT RULE (MEMORIZE)

❗ Security Groups:

* ✅ Allow rules only
* ❌ No deny rules
* ✅ Are **STATEFUL**

We will **prove this practically**.

---

### 🔹 STEP 1: Open Your EC2 Security Group

1. AWS Console → **EC2**
2. Click **Instances**
3. Select your instance `ec2-hands-on-1`
4. Go to **Security** tab
5. Click the **Security group name**

You are now inside **Security Group settings**

---

### 🔹 STEP 2: Understand Existing Inbound Rules

You should already see something like:

| Type | Port | Source   |
| ---- | ---- | -------- |
| SSH  | 22   | My IP    |
| HTTP | 80   | Anywhere |

#### What this means:

* SSH → You can connect from your laptop
* HTTP → Anyone can open your website

---

### 🔹 STEP 3: TEST 1 – Remove HTTP Access (Hands-On Proof)

#### ❌ Remove HTTP Rule

1. Click **Edit inbound rules**
2. ❌ Delete **HTTP (port 80)**
3. Click **Save rules**

---

#### 🔍 TEST IN BROWSER

Open:

```
http://ELASTIC_IP
```

#### Expected Result:

❌ Website **WILL NOT OPEN**

✅ This proves:

* Security Group **controls traffic**
* Port 80 is required for web access

---

### 🔹 STEP 4: Add HTTP Rule Back

1. **Edit inbound rules**
2. Add rule:

| Setting | Value                |
| ------- | -------------------- |
| Type    | HTTP                 |
| Port    | 80                   |
| Source  | Anywhere (0.0.0.0/0) |

3. **Save rules**

🔁 Refresh browser

#### Result:

🟢 Website opens again

---

### 🔹 STEP 5: TEST 2 – Change SSH Source (IMPORTANT)

#### ❌ Break SSH Access (on purpose)

1. Edit inbound rules
2. Change **SSH source** from:

```
My IP
```

to:

```
0.0.0.0/0
```

3. Save

📌 Meaning:

* Anyone on internet can try SSH (❌ unsafe)

⚠️ We will fix it later

---

### 🔹 STEP 6: Understand INBOUND vs OUTBOUND

#### Inbound Rules

👉 Who can **come IN** to EC2
Examples:

* SSH (22)
* HTTP (80)

---

#### Outbound Rules

👉 Where EC2 can **go OUT**

Default outbound rule:

```
All traffic → 0.0.0.0/0
```

📌 Means:

* EC2 can access internet
* Install updates
* Download packages

---

### 🔹 STEP 7: STATEFUL PROOF (VERY IMPORTANT)

Security Groups are **STATEFUL**.

#### What does that mean?

If:

* Inbound request is allowed
  Then:
* Response is **automatically allowed**
  (No outbound rule needed)

📌 Example:

* Browser → EC2 (HTTP allowed)
* EC2 → Browser (response allowed automatically)

💡 This is **interview GOLD**

---

### 🔹 STEP 8: FIX SECURITY (BEST PRACTICE)

Now make SSH secure again 👇

1. Edit inbound rules
2. Change SSH source back to:

```
My IP
```

3. Save

✅ Your EC2 is secure again

---

### 🧠 INTERVIEW-READY ANSWER (MEMORIZE)

> **Security Group** is a stateful virtual firewall that controls inbound and outbound traffic at the EC2 instance level. It supports only allow rules, and responses to allowed inbound traffic are automatically permitted.

---

### ✅ LAB 6 TASK CHECKLIST

✔ Removed HTTP and tested
✔ Added HTTP and tested
✔ Understood inbound vs outbound
✔ Proved **STATEFUL behavior**
✔ Secured SSH again

---

## 🧪 EC2 HANDS-ON – LAB 7

### 👉 Network ACL (NACL) vs Security Group (Hands-On + Deep Clarity)

![Image](https://docs.aws.amazon.com/images/vpc/latest/userguide/images/network-acl.png)

---

### 🎯 Objective of LAB 7

By the end of this lab, you will:

* Create & modify a **Network ACL**
* See how it works at **subnet level**
* **PROVE** it is **STATELESS**
* Understand **NACL vs Security Group** (interview-ready)

---

### 🧠 FIRST: What is a Network ACL? (Simple Words)

A **Network ACL (NACL)** is:

* A **firewall for a subnet**
* Works **before traffic reaches EC2**
* Applies to **ALL instances** in that subnet

Think like:

> NACL = Security gate at society entrance 🏢
> Security Group = Guard at each flat 🚪

---

### 🧠 VERY IMPORTANT RULES (MEMORIZE)

| Feature | NACL                    |
| ------- | ----------------------- |
| Level   | Subnet                  |
| Rules   | **Allow + Deny**        |
| Nature  | **STATELESS**           |
| Order   | Rule number (100, 110…) |
| Default | Allow all               |

---

### 🔹 STEP 1: Open Network ACLs

1. AWS Console → **VPC**
2. Left menu → **Network ACLs**
3. You will see a **default NACL**

---

### 🔹 STEP 2: Identify Your Subnet

1. Go to **EC2 → Instances**
2. Click your instance
3. Note **Subnet ID**

📌 We will apply NACL to **this subnet**

---

### 🔹 STEP 3: Create Custom NACL

1. VPC → Network ACLs
2. Click **Create network ACL**
3. Name:

   ```
   ec2-hands-on-nacl
   ```
4. Select your **VPC**
5. Click **Create**

---

### 🔹 STEP 4: Associate NACL with Subnet

1. Select your new NACL
2. Go to **Subnet associations**
3. Click **Edit subnet associations**
4. Select your EC2 subnet
5. Save

⚠️ This NACL now controls traffic for your EC2

---

### 🔹 STEP 5: BLOCK HTTP Using NACL (Hands-On Proof)

> Inbound Rule – DENY HTTP

1. Select **Inbound rules**
2. Click **Edit inbound rules**
3. Add rule:

| Rule # | Type | Port | Source    | Action   |
| ------ | ---- | ---- | --------- | -------- |
| 100    | HTTP | 80   | 0.0.0.0/0 | **DENY** |

4. Save

---

> 🔍 TEST IN BROWSER

Open:

```
http://ELASTIC_IP
```

❌ Website **WILL NOT OPEN**

📌 Even though:

* Security Group allows HTTP
* NACL denies it

👉 **NACL blocks first**

---

### 🔹 STEP 6: ALLOW HTTP Again

Add **ALLOW rule** with higher priority:

| Rule # | Type | Port | Source    | Action    |
| ------ | ---- | ---- | --------- | --------- |
| 90     | HTTP | 80   | 0.0.0.0/0 | **ALLOW** |

📌 Rule **90 runs before 100**

🔁 Refresh browser → 🟢 Works

---

### 🔹 STEP 7: PROVE STATELESS BEHAVIOR (IMPORTANT)

> ❌ Remove Outbound Rule

1. Go to **Outbound rules**
2. Delete rule:

```
ALLOW ALL (0.0.0.0/0)
```

3. Save

---

> 🔍 Test Website Again

❌ Website **WILL NOT LOAD**

📌 Why?

* Inbound allowed
* Outbound response blocked

👉 This **PROVES NACL is STATELESS**

---

### 🔹 STEP 8: FIX OUTBOUND RULE (IMPORTANT)

Add outbound rule:

| Rule # | Type | Port | Destination | Action |
| ------ | ---- | ---- | ----------- | ------ |
| 100    | HTTP | 80   | 0.0.0.0/0   | ALLOW  |

Also add:

| Rule # | Type  | Port | Destination | Action |
| ------ | ----- | ---- | ----------- | ------ |
| 110    | HTTPS | 443  | 0.0.0.0/0   | ALLOW  |

Save

---

### 🔹 STEP 9: FINAL COMPARISON (INTERVIEW TABLE)

| Feature    | Security Group | NACL          |
| ---------- | -------------- | ------------- |
| Level      | Instance       | Subnet        |
| Rules      | Allow only     | Allow + Deny  |
| Nature     | **Stateful**   | **Stateless** |
| Rule Order | No order       | Number based  |
| Scope      | Specific EC2   | All in subnet |

---

### 🧠 INTERVIEW-READY ANSWER

> Security Groups act as a stateful firewall at the instance level allowing only permitted traffic, whereas Network ACLs operate at the subnet level, are stateless, and support both allow and deny rules evaluated in order.

---

### ⚠️ CLEANUP (VERY IMPORTANT)

To avoid confusion later:

* Either **restore default NACL**
* Or keep both inbound & outbound properly allowed

---

### ✅ LAB 7 TASK CHECKLIST

✔ Created custom NACL
✔ Associated subnet
✔ Denied & allowed HTTP
✔ Proved stateless behavior
✔ Understood SG vs NACL clearly

---

## 🧪 EC2 HANDS-ON – LAB 8

### 👉 EC2 Key Pairs (Create, Use, Delete & Recover Access)

![Image](https://docs.aws.amazon.com/images/AWSEC2/latest/UserGuide/images/ec2-key-pair.png)

---

### 🎯 Objective of LAB 8

You will:

* Understand **what a key pair really is**
* Create & attach **new key pairs**
* Know **what happens if key is deleted**
* Learn **key recovery concept** (very important)

---

### 🧠 FIRST: What is an EC2 Key Pair?

A **Key Pair** has:

* **Public key** → Stored in EC2
* **Private key (.pem)** → Stored on your laptop

Think like:

> Lock (public key) is on server 🔒
> Key (private key) is with you 🔑

AWS **never stores private key**.

---

### 🔹 STEP 1: View Existing Key Pair

1. EC2 Console → **Key Pairs**
2. You will see:

```
ec2-key-hands-on
```

📌 AWS only shows **key name**, not the file

---

### 🔹 STEP 2: Create a SECOND Key Pair

1. Click **Create key pair**
2. Name:

```
ec2-key-backup
```

3. Type: **RSA**
4. Format: **.pem**
5. Create & download

📌 This is for **learning purpose**

---

### 🔹 STEP 3: Understand a CRITICAL RULE

❗ You **cannot** directly change key pair of:

* Running instance
* Stopped instance

Key pair is:

* Injected **at launch time**

---

### 🔹 STEP 4: What Happens If Key is Deleted? (Concept)

> Scenario:

* `.pem` file deleted from laptop ❌
* EC2 still running

> Result:

❌ You are **LOCKED OUT**

AWS **cannot recover it**

---

### 🔹 STEP 5: HOW TO RECOVER ACCESS (IMPORTANT CONCEPT)

There are **3 real-world recovery methods**:

---

> 🟢 Method 1: EC2 Instance Connect (AWS Linux only)

* Works only if:

  * Instance supports it
  * Port 22 allowed
* Temporary access

---

> 🟢 Method 2: Detach Root Volume (MOST COMMON)

Steps (conceptual):

1. Stop instance
2. Detach root EBS
3. Attach it to another EC2
4. Add new public key to:

```
~/.ssh/authorized_keys
```

5. Reattach volume
6. Start instance

📌 **Very important interview topic**

---

> 🟢 Method 3: Session Manager (BEST PRACTICE)

* Uses **IAM Role**
* No SSH, no key pair
* Secure & auditable

We’ll do this **hands-on later**

---

### 🔹 STEP 6: BEST PRACTICES (MEMORIZE)

✔ Always keep backup key
✔ Use **IAM Roles + Session Manager**
✔ Never share `.pem`
✔ Restrict SSH source
✔ Rotate keys in production

---

### 🧠 INTERVIEW-READY ANSWER

> An EC2 key pair consists of a public key stored on the instance and a private key held by the user. AWS does not store the private key, and if it is lost, access must be recovered through volume attachment or Session Manager.

---

### 🛑 DO NOT TRY KEY RECOVERY NOW

We will do it safely in **advanced labs**.

---

### ✅ LAB 8 TASK CHECKLIST

✔ Understood key pair concept
✔ Created backup key
✔ Learned recovery methods
✔ Understood best practices

---

## 🧪 EC2 HANDS-ON – LAB 9

### 👉 EC2 User Data (Automatic Setup at Launch)

![Image](https://cloudkatha.com/wp-content/uploads/2021/09/How-to-use-EC2-User-Data-Script-to-Install-Apache-Web-Server.png)


---

### 🎯 Objective of LAB 9

By the end of this lab, you will:

* Understand **what User Data is**
* Use User Data to **auto-install Apache**
* Deploy a website **WITHOUT SSH**
* Learn **cloud-init concept** (interview topic)

---

### 🧠 FIRST: What is EC2 User Data? (Very Simple)

**User Data** is:

* A **script** that runs **only once**
* Runs **when EC2 starts for the first time**
* Used for **automation**

Think like:

> User Data = Auto-setup instructions for EC2 🧠

Example:

* Install Apache
* Start service
* Create website
* Configure app

---

### 🧠 VERY IMPORTANT RULES (MEMORIZE)

❗ User Data:

* Runs **only at first launch**
* Runs as **root user**
* Uses **cloud-init**
* Best for **bootstrapping**

---

### 🔹 WHAT WE WILL DO (PLAN)

We will:

1. Launch **NEW EC2 instance**
2. Add **User Data script**
3. Apache installs automatically
4. Website works **without SSH**

---

### 🔹 STEP 1: Launch a NEW EC2 Instance

Go to:
**EC2 → Instances → Launch instance**

> Instance name:

```
ec2-userdata-demo
```

---

### 🔹 STEP 2: Choose AMI & Instance Type

* AMI → **Amazon Linux 2023**
* Instance type → **t2.micro (Free tier)**

---

### 🔹 STEP 3: Select Key Pair

Choose:

```
ec2-key-hands-on
```

(We won’t SSH, but AWS requires it)

---

### 🔹 STEP 4: Network & Security Group

Inbound rules:

| Type | Port | Source   |
| ---- | ---- | -------- |
| HTTP | 80   | Anywhere |
| SSH  | 22   | My IP    |

---

### 🔹 STEP 5: ADD USER DATA (MOST IMPORTANT)

Scroll down → **Advanced details**

Find:

> 👉 User data

Paste **EXACTLY** this:

```bash
#!/bin/bash
dnf update -y
dnf install httpd -y
systemctl start httpd
systemctl enable httpd

echo "<h1>Hello from EC2 User Data 🚀</h1>" > /var/www/html/index.html
```

---

### 🧠 EXPLAIN SCRIPT LINE BY LINE (IMPORTANT)

```bash
#!/bin/bash
```

➡ Tells EC2: “This is a Linux shell script”

```bash
dnf update -y
```

➡ Updates system packages

```bash
dnf install httpd -y
```

➡ Installs Apache web server

```bash
systemctl start httpd
```

➡ Starts Apache

```bash
systemctl enable httpd
```

➡ Starts Apache on reboot

```bash
echo "<h1>Hello from EC2 User Data 🚀</h1>" > /var/www/html/index.html
```

➡ Creates website homepage automatically

---

### 🔹 STEP 6: Launch Instance

Click **Launch instance**

Wait until:
🟢 Instance state → **Running**

---

### 🔹 STEP 7: Test WITHOUT SSH (BIG MOMENT 🎉)

1. Copy **Public IP**
2. Open browser:

```
http://PUBLIC_IP
```

> Expected Output:

```
Hello from EC2 User Data 🚀
```

✅ Apache installed
✅ Website deployed
✅ **No manual work**

---

### 🔹 STEP 8: Verify User Data Ran (Optional SSH)

If you want to check logs:

```bash
sudo cat /var/log/cloud-init-output.log
```

📌 Shows user data execution logs

---

### 🧠 INTERVIEW-READY ANSWER

> EC2 User Data is a cloud-init based mechanism that allows running scripts at instance launch to automate configuration such as installing software and starting services. It runs only once at first boot.

---

### ⚠️ COMMON MISTAKES (VERY IMPORTANT)

❌ Forget `#!/bin/bash`
❌ Wrong indentation
❌ Expecting script to run again after reboot
❌ Missing HTTP rule in SG

---

### ✅ LAB 9 TASK CHECKLIST

- ✔ New EC2 launched
- ✔ User Data added
- ✔ Apache auto-installed
- ✔ Website works without SSH
- ✔ Understood automation concept

---

## 🧪 EC2 HANDS-ON – LAB 10

### 👉 EC2 Instance Lifecycle (Start, Stop, Reboot, Terminate)

![Image](https://miro.medium.com/v2/resize%3Afit%3A752/1%2Ag5rz-jln6QgHrIy-xSv7YQ.png)

---

### 🎯 Objective of LAB 10

You will:

* Perform **Start / Stop / Reboot / Terminate**
* Understand **what happens to IP, storage, billing**
* Learn **when to use each action**
* Be **interview-ready**

---

### 🧠 FIRST: EC2 Lifecycle States (Simple)

An EC2 instance can be in:

| State      | Meaning         |
| ---------- | --------------- |
| Pending    | Starting        |
| Running    | Active          |
| Stopped    | Powered off     |
| Terminated | Deleted forever |

---

### 🔹 STEP 1: Identify Two Instances

You should have:

1. `ec2-hands-on-1` (Elastic IP attached)
2. `ec2-userdata-demo`

We will **safely test lifecycle** on `ec2-userdata-demo`

---

### 🔹 STEP 2: STOP the Instance

1. EC2 → Instances
2. Select `ec2-userdata-demo`
3. **Instance state → Stop**
4. Confirm

---

> 🔍 What Happens When STOP?

| Item       | Result            |
| ---------- | ----------------- |
| Instance   | OFF               |
| Billing    | ❌ No compute cost |
| EBS root   | ✅ Preserved       |
| Public IP  | ❌ Released        |
| Elastic IP | ❌ Not attached    |

---

### 🔹 STEP 3: START the Instance Again

1. Select instance
2. **Instance state → Start**

Wait → Running

---

> 🔍 Check Public IP

* Public IP will be **NEW**
* Website still works (Apache already installed)

📌 This proves:

* Data remains
* Public IP changes

---

### 🔹 STEP 4: REBOOT the Instance

1. Select instance
2. **Instance state → Reboot**

---

> 🔍 What Happens When REBOOT?

| Item      | Result      |
| --------- | ----------- |
| OS        | Restarts    |
| Public IP | ✅ Same      |
| Data      | ✅ Safe      |
| Billing   | ✅ Continues |

📌 Reboot = Restart laptop

---

### 🔹 STEP 5: TERMINATE the Instance (IMPORTANT)

⚠️ **THIS IS DESTRUCTIVE**

1. Select `ec2-userdata-demo`
2. **Instance state → Terminate**
3. Confirm

---

> 🔍 What Happens When TERMINATE?

| Item      | Result       |
| --------- | ------------ |
| Instance  | ❌ Deleted    |
| EBS root  | ❌ Deleted    |
| Public IP | ❌ Gone       |
| Recovery  | ❌ Impossible |

📌 Terminate = Delete forever

---

### 🧠 VERY IMPORTANT INTERVIEW POINTS

- Stop → Save money
- Start → New public IP
- Reboot → Same IP
- Terminate → Data lost

---

### 🧠 INTERVIEW-READY ANSWER

> Stopping an EC2 instance halts compute billing while preserving EBS volumes, whereas terminating an instance permanently deletes the instance and associated root volume, making recovery impossible.

---

### ⚠️ COST BEST PRACTICES

- Stop unused instances
- Use Elastic IP for static access
- Terminate unused test EC2s
- Monitor free tier usage

---

### ✅ LAB 10 TASK CHECKLIST

- Stopped instance
- Started instance
- Rebooted instance
- Terminated test instance
- Understood lifecycle fully

---