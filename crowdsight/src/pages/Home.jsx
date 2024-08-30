import axios from "axios";
import { useNavigate } from "react-router-dom";
function Home(){
    function submit(){
        event.preventDefault();
        const AOI_long = document.getElementById("AOI-long").value;
        const AOI_lat = document.getElementById("AOI-lat").value;
        const sitemap_file = document.getElementById("file-input");
        const endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/insertOne"
        const apikey = import.meta.env.VITE_MONGODB_API_KEY + "/action/insertOne"
        const navigate = useNavigate();

        const data = json.stringify({
            "dataSource":"mongodb-atlas",
            "database" : "crowdsight",
            "collections" : "AOI",
            "document":{
                "longitude": AOI_long,
                "latitude": AOI_lat,
                "sitemap_file": sitemap_file
            }
        })

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
              navigate('/Heatmap');
            } else {
              alert("Couldn't find company. Have you entered the right name?");
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