import axios from "axios";
import React, {useState, useEffect} from "react";
import { Link } from 'react-router-dom';
function Heatmap(){
    const [mapHtml, setMapHtml] = useState(null); // Use state to hold the HTML content
    const backend_endpoint = import.meta.env.VITE_BACKEND_ENDPOINT + "/create_map";

    useEffect(() => {
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
                    console.log("Heatmap successfully retrieved");
                    setMapHtml(response.data); // Update the state with the HTML content
                } else {
                    alert("Failed to retrieve heatmap");
                }
            })
            .catch((error) => {
                console.error("There was an error retrieving the heatmap!", error);
            });
    }, []); // Empty dependency array ensures this effect runs only once when the component mounts

    return (
        <>

            <body id="home">
                {mapHtml ? <iframe srcDoc={mapHtml} width={1600} height={800}/> : <p>Loading heatmap...</p>}

                <div class="sidebar">
                    <i id="icons" class="fa-solid fa-map"></i>
                    <Link to={`/heatmap`}>
                        Sitemap
                    </Link>
                    <i id="icons"class="fa-solid fa-video"></i>
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

export default Heatmap;
