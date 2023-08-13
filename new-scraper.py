import requests
import json

def fetch_data_from_maroof(skip_count=0, max_result_count=10):
    # Define the endpoint and headers
    endpoint = "https://api.thiqah.sa/maroof/public/api/app/business/search"
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
    
    # Define the parameters
    params = {
        "keyword": "",
        "businessTypeId": 48,
        "businessTypeSubCategoryId": "",
        "regionId": "",
        "cityId": "",
        "certificationType": "",
        "sortBy": 2,
        "sortDirection": 2,
        "sorting": "",
        "skipCount": skip_count,
        "maxResultCount": max_result_count
    }
    
    # Send the request
    response = requests.get(endpoint, headers=headers, params=params)
    
    # Ensure the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

def fetch_all_items(total_count, max_result_count=10):
    all_items = []
    skip_count = 0

    while len(all_items) < total_count:
        batch_data = fetch_data_from_maroof(skip_count, max_result_count)
        if batch_data:
            all_items.extend(batch_data['items'])
            skip_count += max_result_count
        else:
            break  # if there's an issue with fetching data, break out of the loop

    return all_items[:total_count]  # return only the desired total count of items

# Fetch desired amount of items
total_items_count = 706  # replace with the desired total number of items
items_per_request = 100  # replace with the desired number of records per request
all_data = fetch_all_items(total_items_count, items_per_request)

# Save to JSON file
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)

