import urllib.request
import json
import ssl

# आज का पंचांग API (Backup setup)
url = "https://aaj-ka-panchang-api.vercel.app/api/panchang"

try:
    # SSL Certificate Bypass & User Agent Header
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, context=context, timeout=10) as response:
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            panchang_data = {
                "tithi": data.get("tithi", "अष्टमी (कृष्ण पक्ष)"),
                "nakshatra": data.get("nakshatra", "रोहिणी"),
                "sunrise": data.get("sunrise", "05:55 AM"),
                "sunset": data.get("sunset", "06:20 PM")
            }
        else:
            raise Exception("API status not 200")
except Exception as e:
    print(f"API Error/Timeout, using fallback update: {e}")
    # अगर API रिस्पॉन्स न दे तो डिफ़ॉल्ट पंचांग डेटा फ़ाइल में लिख दें
    panchang_data = {
        "tithi": "आज का पंचांग",
        "nakshatra": "शुभ नक्षत्र",
        "sunrise": "06:00 AM",
        "sunset": "06:30 PM"
    }

# File Write
with open("today.json", "w", encoding="utf-8") as f:
    json.dump(panchang_data, f, ensure_ascii=False, indent=2)

print("Panchang updated successfully!")


    
