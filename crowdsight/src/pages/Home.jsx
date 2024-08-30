import axios from "axios";
import React from "react";
import { useNavigate, Link } from "react-router-dom";
function Home(){
    const endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/insertOne"
    const apikey = import.meta.env.VITE_MONGODB_API_KEY;
    const navigate = useNavigate();

    const submit = () => {
        event.preventDefault();
        const AOI_long = document.getElementById("AOI-long").value;
        const AOI_lat = document.getElementById("AOI-lat").value;
        const sitemap_file = document.getElementById("file-input");

        const data = JSON.stringify({
            "dataSource":"ESGeePeeTee",
            "database" : "crowdsight",
            "collection" : "aoi",
            "document":{
                "longitude": AOI_long,
                "latitude": AOI_lat,
                // "sitemap_file": sitemap_file
            },
        })

        console.log(data);

        const config = {
            method: 'post',
            url: endpoint,
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
            <div id="content">
                <form action="#">
                <div id="AOI">
                    
                    <h1 class="headers">Area of Interest</h1>
                    <input type="text" id='AOI-long' class="AOI-input" placeholder="Longitude"/>
                    <input type="text" id='AOI-lat'class="AOI-input" placeholder="Latitude"/>
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
                    <input type="file" class="sitemap-input" id="file-input" hidden/>
                </div>
                <button onClick={submit}>Generate Heatmap</button>
                </form>
            </div>
        </>
    )
}

export default Home;