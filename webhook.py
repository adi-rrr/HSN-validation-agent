from flask import Flask, request, jsonify
import pandas as pd
import re

app = Flask(__name__)


df = pd.read_excel("HSN_SAC.xlsx")


df.columns = df.columns.str.strip()
df['HSNCode'] = df['HSNCode'].astype(str).str.strip()

def extract_hsn_codes(text):
    return re.findall(r'\b\d{2,8}\b', text)

def get_closest_match(code, df):
    for i in range(len(code) - 2, 1, -2):
        parent = code[:i]
        match = df[df['HSNCode'] == parent]
        if not match.empty:
            return match.iloc[0]['HSNCode'], match.iloc[0]['Description']
    return None, None


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    parameters = req.get("queryResult", {}).get("parameters", {})
    user_input = parameters.get("hsn_code", "")


    input_text = ""
    if isinstance(user_input, list):
        input_text = " ".join(map(str, user_input))
    else:
        input_text = str(user_input)


    codes = extract_hsn_codes(input_text)
    print(codes)
    response = []

    for code in codes:
        result = df[df['HSNCode'] == code]
        if not result.empty:
            desc = result.iloc[0]['Description']
            response.append(f"✅ HSN Code {code} is valid. Description: {desc}")
        else:
            closest_code, closest_desc = get_closest_match(code, df)
            if closest_code:
                response.append(
                    f"⚠️ HSN Code {code} not found. Closest match: {closest_code} - {closest_desc}"
                )
            else:
                response.append(f"❌ HSN Code {code} is invalid or not found.")

    return jsonify({"fulfillmentText": "\n".join(response)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
