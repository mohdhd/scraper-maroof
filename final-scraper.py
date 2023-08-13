import requests
import json
from tqdm import tqdm

def fetch_data_from_maroof(businessTypeId, skip_count=0, max_result_count=10):
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
        "businessTypeId": businessTypeId,
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
        print(f"Failed to retrieve data for businessTypeId {businessTypeId}. Status Code: {response.status_code}")
        return None

def fetch_all_items_for_business_type(businessTypeId, max_result_count=10):
    all_items = []
    skip_count = 0

    # Fetch the first batch to determine the total count
    first_batch = fetch_data_from_maroof(businessTypeId, skip_count, max_result_count)
    if not first_batch:
        return all_items

    total_count = first_batch['totalCount']
    all_items.extend(first_batch['items'])
    skip_count += max_result_count

    for _ in tqdm(range(0, total_count, max_result_count), desc="Fetching Batches", leave=False):
        if len(all_items) >= total_count:
            break

        batch_data = fetch_data_from_maroof(businessTypeId, skip_count, max_result_count)
        if batch_data:
            all_items.extend(batch_data['items'])
            skip_count += max_result_count
        else:
            break

    return all_items



# Define the business types
business_types = [
  {
    "id": 45,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-13.png",
    "typeCategoryId": 15,
    "creationDate": "1900-01-01T00:00:00",
    "name": "أخرى",
    "key": "Other",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 47,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-14.png",
    "typeCategoryId": 10,
    "creationDate": "1900-01-01T00:00:00",
    "name": "السيارات",
    "key": "Cars",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 48,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-15.png",
    "typeCategoryId": 11,
    "creationDate": "1900-01-01T00:00:00",
    "name": "العقارات",
    "key": "RealEstate",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 54,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-5.png",
    "typeCategoryId": 6,
    "creationDate": "2023-02-07T12:40:07.077",
    "name": "الجمال والصحة",
    "key": "BeautyAndHealth",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 55,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-16.png",
    "typeCategoryId": 12,
    "creationDate": "2023-02-07T12:40:10.487",
    "name": "المنزل",
    "key": "Home",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 56,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-3.png",
    "typeCategoryId": 2,
    "creationDate": "2023-02-07T12:40:11.23",
    "name": "خدمات الأعمال",
    "key": "BusinessServices",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 57,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-9.png",
    "typeCategoryId": 8,
    "creationDate": "2023-02-07T12:40:19.107",
    "name": "حفلات",
    "key": "Occasions",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 58,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-1.png",
    "typeCategoryId": 1,
    "creationDate": "2023-02-07T12:40:19.89",
    "name": "أطعمة ومشروبات",
    "key": "FoodAndDrinks",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 59,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-211.png",
    "typeCategoryId": 13,
    "creationDate": "2023-02-07T12:40:22.643",
    "name": "هدايا",
    "key": "Gifts",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 60,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-4.png",
    "typeCategoryId": 4,
    "creationDate": "2023-02-07T12:40:23.58",
    "name": "التعليم",
    "key": "Education",
    "isActive": True,
    "nameEn": "null"
  },
  {
    "id": 61,
    "businessNum": 0,
    "icon": "/app/images/icons/cat-11.png",
    "typeCategoryId": 9,
    "creationDate": "2023-02-07T12:40:24.07",
    "name": "إلكترونيات",
    "key": "Electronics",
    "isActive": True,
    "nameEn": "null"
  }
]

# Fetch and save data for each business type
items_per_request = 150  # replace with the desired number of records per request

for business in business_types:
    print('*** Fetching data for business type: ' + business['name'] + ' ***')
    all_data = fetch_all_items_for_business_type(business['id'], items_per_request)
    
    filename = business['name'] + ".json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(all_data, file, ensure_ascii=False, indent=4)

    print('*** Done fetching data for business type: ' + business['name'] + ' ***')
    
