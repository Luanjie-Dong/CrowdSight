import axios from "axios";
import React from "react";

async function Camera(){
    const endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/find"
    const apikey = import.meta.env.VITE_MONGODB_API_KEY;
    var camera_data = null;

    console.log(endpoint);

    const data = JSON.stringify({
        "dataSource":"ESGeePeeTee",
        "database" : "crowdsight",
        "collection" : "cctv",
        "filter" : {},
    })

    const config = {
        method: 'post',
        url: endpoint,
        headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apikey}`,
        },
        data: data,
    };

    axios(config)
        .then((response) => {
            // Access the array of documents directly from response.data
            if (response.data.documents !== null) {
                // console.log('successful');
                camera_data = response.data.documents;
                const all_cameras = []

                for (const c in camera_data) {
                    all_cameras.push({
                        name: camera_data[c].name,
                        longitude: camera_data[c].longitude,
                        latitude: camera_data[c].latitude,
                        url: camera_data[c].url,
                    })
                }
                console.log(all_cameras);
            } else {
              alert("CCTV data not retrieved");
            }
        })


    const submit = () => {
        event.preventDefault();
    }

    // var object = "";

    return(
        <>
           <body id="add">
                   <div id="content">
                           <form action="#">
                           <div id="text">
                   
                    <h1 class="headers">Add Camera</h1>
                    <input type="text" id='cam_name' class="container textvalue" placeholder="Name"/>
                    <input type="text" id='cam_long' class="container textvalue" placeholder="Longitude"/>
                    <input type="text" id='cam_lat'class="container textvalue" placeholder="Latitude"/>
                    <input type="text" id='cam_uri'class="container textvalue" placeholder="URI"/>
                           </div>
                           <button class="container generate" onClick={submit}>Add Camera</button>
                           </form>
                       </div>
                   
                       <div class="sidebar">
                           <i id="icons" class="fa-solid fa-map"></i>
                           <a href="#sitemap">Sitemap</a>
                           <img src="crowdsight/src/assets/cctv.png" />
                           <a href="#camera">Cameras</a>
                           <i id="icons"class="fa-solid fa-location-dot"></i>
                           <a href="#Marker">Markers</a>
                           <img id="logo"src="crowdsight/src/assets/Nomura A1 (1).png" />
                       </div>

                       <div class="existing">
                        <table>
                            object
                        </table>
                       </div>


           </body>
        </>
    )
}
export default Camera