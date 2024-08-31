import requests
import json

endpoint_url = " https://ap-southeast-1.aws.data.mongodb-api.com/app/data-fevcdnd/endpoint/data/v1/action" #edit your endpoint
API_KEY = 'KdrhLZMfd335dURL2AUB2Tbtav6SCdtCBdbyrBRX1OwFHzd2H4rEtG1YKzgtD8o9'

get_url = f'{endpoint_url}/find'


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
            site_map = aoi_response_data[0]["sitemap_file"]
            with open("./heatmap/data/sitemap.json", "wb") as f:
                f.write(site_map)
            print("AOI data saved successfully")
        
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




if __name__ == "__main__":
    # Example company data to update or store
    aoi , cctv , bus , mrt = map_data()
    print(aoi)
    print(cctv)
    print(bus)
    print(mrt)
