from flask import Flask, render_template, request
# import subprocess
from heatmap import map
from flask_socketio import SocketIO
from model.model import CrowdDensityEstimator

app = Flask(__name__)


@app.route('/create_map', methods=['POST'])
def receive_data():
    data = request.get_json()
    mrt = data.get('mrt')   #mrt = {"City Hall": [1.293191026024169, 103.85165498556803],...}
    bus_stops = data.get('bus_stops') #bus_stops = {"Suntec City": [1.2923858977559841, 103.85182924546],...}
    aoi=data.get('aoi') #[long,lat]
    cameras_loc=data.get('cameras') #cameras_loc = {
                                        # "CAM1": {
                                        #     "Lattitude": 1.299810,
                                        #     "Longitude": 103.862298,
                                        #     "URL": http.....
                                        # },...}
    """RUN CV MODEL HERE USING camera_loc URL"""

    estimator = CrowdDensityEstimator(model_path='src/cmtl_shtechA_100.h5')
    for camera in cameras_loc:
        video_path = cameras_loc[camera]['URL']
        camera = camera
        estimator.analyse_stream(video_path,camera)



    # cameras={
    #     "CAM1": {
    #         "Lattitude": 1.299810,
    #         "Longitude": 103.862298,
    #         "Num_people": 240
    #     }...}

    ###GET THE NUM_PEOPLE FOR EACH CAMERA FROM CV,
    ### ABOVE SHOULD BE THE FORMAT BEFORE INPUTTING INTO MAP FUNCTION

    # Run the map.py script to generate the map
    map.create_map(aoi,mrt,bus_stops,cameras)

    # Render the map in an iframe in the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
