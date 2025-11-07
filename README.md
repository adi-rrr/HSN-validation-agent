HSN Code Validation Agent – Documentation & Run Instructions

(https://drive.google.com/file/d/17kL3vwDV3x7Hg92E--_Gd-zqdv59Zuz_/view?usp=drive_link) - Refer this video for Code walkthrough and overview


📌 Overview

This agent validates HSN (Harmonized System of Nomenclature) codes and provides official descriptions by referencing an Excel-based master dataset. It can handle:
•	Single or multiple HSN codes per query
•	Closest matches if the code is invalid
•	Hierarchical validation (e.g., checks parent codes like 01, 0101)
•	Live refresh capability (optional) without restarting the backend
⚙️ Setup Instructions
1. 🧩 Clone and Setup Virtual Environment
git clone <your-repo-url>
cd <project-root>
python -m venv .venv
source .venv/bin/activate     # Use .venv\\Scripts\\activate on Windows
pip install -r requirements.txt

2. 📦 Required Python Libraries
flask
pandas
openpyxl

If not using requirements.txt, just run:
pip install flask pandas openpyxl

________________________________________
🧠 Running the Flask App (Locally)
python main.py

This will start your webhook at:
<http://localhost:5000/webhook>

________________________________________
🌐 Expose Public Webhook with Ngrok Tunnel
#install ngrok if you have not installed
npm install -g ngrok
ngrok http PORT_NUMBER
#example ngrok http 5000

You’ll get a URL like:
<https://your-agent-name.ngrok-free.app>
________________________________________
Integrate Webhook in Dialogflow Essentials
1.	Go to Dialogflow Console → your agent → Fulfillment tab
2.	Enable Webhook and paste the Cloudflare URL (with /webhook path)
3.	<https://your-agent-name.ngrok-free.app/webhook>
4.	
5.	Save and test using a sample intent like:
“Check HSN code 1208 and 1234”
________________________________________
Format of Excel File (HSN_SAC.xlsx)
Make sure your Excel has exactly these columns:
HSNCode	Description
01	LIVE ANIMALS
01012100	PURE-BRED BREEDING ANIMALS
Testing Sample Inputs
✅ Valid HSN code
Input: “Check HSN code 1208”
Output: ✅ HSN Code 1208 is valid. Description: FLOURS AND MEALS...
❌ Invalid HSN code
Input: “Check HSN code 1234”
Output: ⚠️ HSN Code 1234 not found. Closest match: 12 - Oil seeds...
🔗 Multiple codes with mix
Input: “Check HSN for 01012100, 1234 and 0101”
Output: Combo of ✅, ❌, and ⚠️ responses







Using ADK only:
project files - https://drive.google.com/drive/folders/1X5u91ZaHogljlpH7Zk5ShhxauzrpVJSU
walkthrough - https://drive.google.com/file/d/1EUkjupzzS4OmdFF3z8KLZWh-gFUC74p4/view
