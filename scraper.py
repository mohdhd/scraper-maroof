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

def fetch_all_data(total_items, items_per_request):
    all_data = []
    for skip in range(0, total_items, items_per_request):
        data = fetch_data_from_maroof(skip_count=skip, max_result_count=items_per_request)
        if data:
            all_data.append(data)
    return all_data

# Define how many total items you want and how many items per request
TOTAL_ITEMS = 706  # Example value, modify as needed
ITEMS_PER_REQUEST = 100

# Fetch all the data
all_data = fetch_all_data(TOTAL_ITEMS, ITEMS_PER_REQUEST)

# Save to JSON file
with open('data.json', 'w') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)

print(f"Data has been saved to data.json")

