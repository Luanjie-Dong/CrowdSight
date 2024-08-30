import axios from "axios";
import React from "react";
import { Link } from 'react-router-dom';
function Heatmap(){
    const backend_endpoint = import.meta.env.VITE_BACKEND_ENDPOINT + "/create_map";
    var map_html = null;

    const config = {
        method: 'get',
        url: backend_endpoint,
        headers: {
            'Content-Type': 'application/json',
        },
    }

    axios(config)
    .then((response) => {
        if (response.data !== null) {
            console.log("heatmap successfully retrieved");
            map_html = response.data;
        } else {
            alert("failed to retrieve heatmap");
        }
    })


    return(
        <>
            <iframe srcDoc={map_html} />

            <body id="home">
                <div class="sidebar">
                    <i id="icons" class="fa-solid fa-map"></i>
                    <Link to={`/heatmap`}>
                        Sitemap
                    </Link>
                    <img src="crowdsight/src/assets/cctv.png" />
                    <Link to={`/camera`}>
                        Cameras
                    </Link>
                    <i id="icons"class="fa-solid fa-location-dot"></i>
                    <Link to={`/marker`}>
                        Markers
                    </Link>
                    <img id="logo"src="crowdsight/src/assets/Nomura A1 (1).png" />
                </div>
            </body>
        </>
    )
}
export default Heatmap