import os
import requests
import json
from tqdm import tqdm

def fetch_detailed_data(record_id):
    endpoint = f"https://api.thiqah.sa/maroof/public/api/app/business/{record_id}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ar",
        "apikey": "c1qesecmag8GSbxTHGRjfnMFBzAH7UAN",
        "content-type": "Application/json",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }

    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve detailed data for record ID {record_id}. Status Code: {response.status_code}")
        return None

def main():
    # Assuming all files are in the current directory and have '.json' extension
    for filename in tqdm(os.listdir(), desc="Processing Files"):
        if filename.endswith(".json"):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Loop through records in the file and fetch detailed data
                detailed_records = []
                for record in tqdm(data, desc=f"Fetching Details for {filename}"):
                    record_id = record["id"]
                    detailed_data = fetch_detailed_data(record_id)
                    
                    if detailed_data:
                        detailed_records.append(detailed_data)

                # Save all detailed records to a single file
                detailed_filename = f"contacts_{filename}"
                with open(detailed_filename, 'w', encoding='utf-8') as detailed_file:
                    json.dump(detailed_records, detailed_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()

