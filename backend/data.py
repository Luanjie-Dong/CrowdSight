import requests
import json

endpoint_url = " https://ap-southeast-1.aws.data.mongodb-api.com/app/data-fevcdnd/endpoint/data/v1/action" #edit your endpoint
API_KEY = 'KdrhLZMfd335dURL2AUB2Tbtav6SCdtCBdbyrBRX1OwFHzd2H4rEtG1YKzgtD8o9'

get_url = f'{endpoint_url}/find'


def map_data(map_information):
    headers = {
        'Content-Type': 'application/json',
        'api-key': API_KEY
    }

    get_aoi = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "aoi",
        "filter": {"company": company_data['company']}
    }

    get_cctv = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "cctv",
        "filter": {"company": company_data['company']}
    }

    get_marker = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "marker",
        "filter": {"company": company_data['company']}
    }

    

    try:
        # Get AOI
        response = requests.post(get_url, headers=headers, json=get_aoi)
        if response.status_code == 200:
            response_data = response.json()
            aoi_lat = response_data[0]["lattitude"]
            aoi_lot = response_data[0]["longitude"]
        
        #Get CCTV
        response = requests.post(get_url, headers=headers, json=get_cctv)
        if response.status_code == 200:
            response_data = response.json()
            aoi_lat = response_data[0]["lattitude"]
            aoi_lot = response_data[0]["longitude"]

        #Get marker
        response = requests.post(get_url, headers=headers, json=get_marker)
        if response.status_code == 200:
            response_data = response.json()
            aoi_lat = response_data[0]["lattitude"]
            aoi_lot = response_data[0]["longitude"]
        

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example company data to update or store
    company_data = {'company': 'Boeing', 
                    'industry': 'AIR', 
                    'total_score': 22, 
                    'environmental': {'score': 8, 'dimension_total': 35}, 
                    'social': {'score': 8, 'dimension_total': 37}, 
                    'governance': {'score': 6, 'dimension_total': 28}, 
                    'timestamp': '2024-07-22'}

    store_or_update_esg_scores(company_data)
