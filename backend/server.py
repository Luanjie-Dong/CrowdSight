from flask import Flask, render_template, request
from heatmap import map
from model.model import CrowdDensityEstimator
from data import map_data , update
from flask_cors import CORS 



app = Flask(__name__)
CORS(app)


@app.route('/create_map', methods=['GET'])
def receive_map():
    
    aoi , cctv , bus , mrt = map_data()

    try:
        """CV MODEL IS HEREEE"""
        model_path = 'model/src/cmtl_shtechA_100.h5'
        estimator = CrowdDensityEstimator(model_path)
        cameras = {}
        for camera in cctv:
            print(f"HOLD UPPPP Analysing {camera} ")
            video_path = cctv[camera]['URL']
            long = cctv[camera]['Longitude']
            lat = cctv[camera]['Lattitude']
            crowd = estimator.analyse_stream(video_path,camera)
            cameras[camera] = {"Longitude":long,"Lattitude":lat,"Num_people":crowd[1]}

        

        print("Crowd Density analysis done :)))))))))))")

        ###GET THE NUM_PEOPLE FOR EACH CAMERA FROM CV,
        ### ABOVE SHOULD BE THE FORMAT BEFORE INPUTTING INTO MAP FUNCTION

        # Run the map.py script to generate the map
        map.create_map(aoi,mrt,bus,cameras)
        
        # # Render the map in an iframe in the HTML template
        return render_template('map.html')
    
    except Exception as e:
        mistake = f"An error occurred: {e}"
        return mistake

    


    
@app.route('/hello', methods=['GET'])
def hello():
    message = "the server is saying hello"
    return message



    

if __name__ == '__main__':
    app.run(debug=True)
