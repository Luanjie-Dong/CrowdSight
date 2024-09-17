import requests
import json

endpoint_url = "" #edit your endpoint
API_KEY = "" #edit your mongodb key

get_url = f'{endpoint_url}/find'
update_url = f'{endpoint_url}/updateOne'
get_one_url = f'{endpoint_url}/fineOne'


def map_data():

    headers = {
        'Content-Type': 'application/json',
        'api-key': API_KEY
    }

    get_aoi = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "aoi",
        "filter": {}
    }

    get_cctv = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "cctv",
        "filter": {}
    }

    get_marker = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "marker",
        "filter": {}
    }

    aoi = []
    cctv_array = []
    bus_array = []
    mrt_array = []

    try:
        # Get AOI
        aoi_response = requests.post(get_url, headers=headers, json=get_aoi)
        if aoi_response.status_code == 200:
            print("AOI data accessed")
            aoi_response_data = aoi_response.json()['documents']
            # print(aoi_response_data)
            aoi_lat = aoi_response_data[0]["latitude"]
            aoi_lot = aoi_response_data[0]["longitude"]
            aoi = [aoi_lat,aoi_lot]
            
        
        #Get CCTV
        cctv_response = requests.post(get_url, headers=headers, json=get_cctv)
        if cctv_response.status_code == 200:
            print("CCTV data accessed")
            cctv_response_data = cctv_response.json()['documents']
            # print(cctv_response_data)
            cctv_array = {}
            for cctv in cctv_response_data:
                cctv_name = cctv["name"]
                cctv_lat = cctv["latitude"]
                cctv_lot = cctv["longitude"]
                cctv_url = cctv["url"]
                cctv_array[cctv_name] = {"Lattitude":cctv_lat,"Longitude":cctv_lot,"URL":cctv_url}

        #Get marker
        marker_response = requests.post(get_url, headers=headers, json=get_marker)
        if marker_response.status_code == 200:
            print("Marker data accessed")
            marker_response_data = marker_response.json()['documents']
            # print(marker_response_data)
            bus_array = {}
            mrt_array = {}
            for marker in marker_response_data:
                marker_name = marker["label"]
                marker_lat = marker["latitude"]
                marker_lon = marker["longitude"]
                marker_type = marker["type"]
                if marker_type == 'bus_stop':
                    bus_array[marker_name] = [marker_lat,marker_lon]
                else:
                    mrt_array[marker_name] = [marker_lat,marker_lon]
    except Exception as e:
        print(f"An error occurred: {e}")


    return aoi , cctv_array , bus_array , mrt_array


def update(url_links, check_mode=False):
    headers = {
        'Content-Type': 'application/json',
        'api-key': API_KEY
    }

    # Define the base structure for querying CCTV data
    base_query = {
        "dataSource": "ESGeePeeTee",
        "database": "crowdsight",
        "collection": "cctv",
    }

    for camera_name, camera_url in url_links.items():
        # Define the specific filter for the current camera
        find_query = {**base_query, "filter": {"name": camera_name}}

        # Define the update operation
        update_query = {
            **base_query,
            "filter": {"name": camera_name},
            "update": {"$set": {"url": camera_url}}
        }

        try:
            if check_mode:
                # Checking mode - Fetch CCTV data without updating
                cctv_response = requests.post(get_url, headers=headers, json=find_query)
                if cctv_response.status_code == 200:
                    print(f"Fetched CCTV data for {camera_name}")
                    cctv_data = cctv_response.json().get('documents', [])
                    print(cctv_data)
                else:
                    print(f"Failed to fetch data for {camera_name}: {cctv_response.status_code} - {cctv_response.text}")
            else:
                # Update mode - Perform the update
                cctv_response = requests.post(get_url, headers=headers, json=find_query)
                if cctv_response.status_code == 200:
                    update_response = requests.post(update_url, headers=headers, json=update_query)
                    if update_response.status_code == 200:
                        print(f"Successfully updated URL for {camera_name}")
                    else:
                        print(f"Failed to update URL for {camera_name}: {update_response.status_code} - {update_response.text}")
                else:
                    print(f"Failed to find camera {camera_name}: {cctv_response.status_code} - {cctv_response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    
   





if __name__ == "__main__":
    # Example company data to update or store
    # aoi , cctv , bus , mrt = map_data()
    # print(aoi)
    # print(cctv)
    # print(bus)
    # print(mrt)

    url_links = {'Gate 1':'https://hd-auth.skylinewebcams.com/live.m3u8?a=v4s81gppcdsbpaca89ei5jl1k0',
                 'Gate 2':'https://hd-auth.skylinewebcams.com/live.m3u8?a=v4s81gppcdsbpaca89ei5jl1k0',
                 'Gate 3A':'https://hd-auth.skylinewebcams.com/live.m3u8?a=v4s81gppcdsbpaca89ei5jl1k0',
                 'Gate 3B':'https://hd-auth.skylinewebcams.com/live.m3u8?a=v4s81gppcdsbpaca89ei5jl1k0'}
    check_type = ['checking',None]
    update(url_links,check_type[1])