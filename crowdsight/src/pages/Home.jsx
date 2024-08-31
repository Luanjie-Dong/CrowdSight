import axios from "axios";
import React from "react";
import { useNavigate, Link } from "react-router-dom";
function Home(){

    const endpoint = import.meta.env.VITE_MONGODB_ENDPOINT;
    const apikey = import.meta.env.VITE_MONGODB_API_KEY;
    const navigate = useNavigate();

    // look for aoi file in mongodb

    const find_data = JSON.stringify({
        "dataSource":"ESGeePeeTee",
        "database" : "crowdsight",
        "collection" : "aoi",
        "filter":{},
    })

    const find_config = {
        method: 'post',
        url: endpoint + "/action/findOne",
        headers: {
        'Authorization': `Bearer ${apikey}`,
        'Content-Type': 'application/json',
        },
        data: find_data,
    };

    axios(find_config)
    .then((response) => {
        // Access the array of documents directly from response.data
        if (response.data.document !== null) {
            console.log('aoi already loaded');
            navigate('/heatmap');
        }
    });

    const submit = () => {
        event.preventDefault();
        const AOI_long = document.getElementById("AOI-long").value;
        const AOI_lat = document.getElementById("AOI-lat").value;
        const file_input = document.getElementById("file-input").files[0];

        if (AOI_lat == "" || AOI_long == "") {
            alert("Please enter latitude and longitude");
        }
        
        // const formData = new FormData();
        const blob = new Blob([JSON.stringify(file_input)], {
            type: 'application/json'
        })
        // console.log(file_input);

        // formData.append('file', file_input);

        const data = JSON.stringify({
            "dataSource":"ESGeePeeTee",
            "database" : "crowdsight",
            "collection" : "aoi",
            "document":{
                "longitude": AOI_long,
                "latitude": AOI_lat,
                "sitemap_file": blob,
            },
        })

        console.log(blob);

        const config = {
            method: 'post',
            url: endpoint + "/action/insertOne",
            headers: {
            'Authorization': `Bearer ${apikey}`,
            'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config)
        .then((response) => {
            // Access the array of documents directly from response.data
            if (response.data.document !== null) {
                console.log('successful');
                navigate('/heatmap');
            } else {
              alert("AOI not saved");
            }
        })


    }
    return(
        <>  
        
        <body id="home">
                    <div id="content">
                        <form action="#">
                        <div id="text">
            
                            <h1 class="headers">Area of Interest</h1>
                            <input type="text" id='AOI-lat'class="container textvalue" placeholder="Latitude"/>
                            <input type="text" id='AOI-long' class="container textvalue" placeholder="Longitude"/>
                        </div>
                        <div id="sitemap">
                            <h1 id="sitemapName" class="headers">Sitemap</h1>
                            <div id="site">
            
                            <label for="file-input">
                                <div>
                                    <i id="icons" class="fa-solid fa-cloud-arrow-up"></i>
                                    <p>Browse file to upload</p>
                                </div>
                            </label >
                            </div>
                            <input type="file" class="sitemap-input" id="file-input" accept=".geojson" hidden/>
                        </div>
                        <button class="container generate" onClick={submit}>Generate Heatmap</button>
                        </form>
                    </div>
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

export default Home;