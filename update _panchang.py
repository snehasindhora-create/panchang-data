import urllib.request
import json

url = "https://aaj-ka-panchang-api.vercel.app/api/panchang"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            
            panchang_data = {
                "tithi": data.get("tithi", "अष्टमी (कृष्ण पक्ष)"),
                "nakshatra": data.get("nakshatra", "रोहिणी"),
                "sunrise": data.get("sunrise", "05:55 AM"),
                "sunset": data.get("sunset", "06:20 PM")
            }
            
            with open("today.json", "w", encoding="utf-8") as f:
                json.dump(panchang_data, f, ensure_ascii=False, indent=2)
            print("Panchang updated successfully!")
except Exception as e:
    print(f"Error updating panchang: {e}")

