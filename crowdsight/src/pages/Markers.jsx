import axios from "axios";
import React, {useState, useEffect} from "react";
import { Link } from 'react-router-dom';
function Marker(){
    const endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/find"
    const apikey = import.meta.env.VITE_MONGODB_API_KEY;

    const [documents, setDocuments] = useState([]);
    // console.log(endpoint);

    const data = JSON.stringify({
        "dataSource":"ESGeePeeTee",
        "database" : "crowdsight",
        "collection" : "marker",
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

    useEffect(() => {
        axios(config)
            .then((response) => {
                // Access the array of documents directly from response.data
                setDocuments(response.data.documents);
            }).catch((error) => {
                console.error(error);
            })
    }, []);

    const submit = () => {
        event.preventDefault();

        const marker_label = document.getElementById('marker_label').value;
        const marker_long = document.getElementById('marker_long').value;
        const marker_lat = document.getElementById('marker_lat').value;
        const marker_type = document.getElementById('marker_type').value;

        // console.log("mar_label:", marker_label);
        // console.log("mar_long:", marker_long);
        // console.log("mar_lat:", marker_lat);
        // console.log("mar_type:", marker_type);
        if (marker_label==""|| marker_lat==""|| marker_long==""|| marker_type=="Select Type") {
            alert("Fill in all blanks!");
        } 
        else {
        const add_endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/insertOne";
        const add_data = JSON.stringify({
            "dataSource":"ESGeePeeTee",
            "database" : "crowdsight",
            "collection" : "marker",
            "document" : {
                "label" : marker_label,
                "longitude" : marker_long,
                "latitude" : marker_lat,
                "type" : marker_type,
            }
        })
        const add_config = {
            method: 'post',
            url: add_endpoint,
            headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apikey}`,
            },
            data: add_data,
        }
        axios(add_config)
           .then((response) => {
                console.log(response.data);
                alert("Marker added successfully!");
                location.reload();
            }).catch((error) => {
                console.error(error);
                alert("Failed to add marker!");
            })
        }
    }
    return(
        <>
           <div id="add">
                <div id="content">
                    <form action="#">
                        <div id="text">
                            <h1 className="headers">Add Marker</h1>
                            <input type="text" id='marker_label' className="container textvalue" placeholder="Label"/>
                            <input type="number" id='marker_lat'className="container textvalue" placeholder="Latitude"/>
                            <input type="number" id='marker_long' className="container textvalue" placeholder="Longitude"/>
                            <select id='marker_type' className="container textvalue">
                                <option selected disabled>Select Type</option>
                                <option value="mrt_station">MRT Station</option>
                                <option value="bus_stop">Bus Stop</option>
                            </select>
                        </div>
                        <button className="container generate" onClick={submit}>Add Camera</button>
                    </form>
                </div>
                <div id="marker_list">
                    <h1 className="headers">Current Markers</h1>
                    <table id="mrt_stations_list" className="table_list">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Name</th>
                                <th>Latitude</th>
                                <th>Longitude</th>
                            </tr>
                        </thead>
                        <tbody>
                        {
                            documents.map((document, index) => {
                                return(
                                <tr key={index}>
                                    <td>{document.type}</td>
                                    <td>{document.label}</td>
                                    <td>{document.latitude}</td>
                                    <td>{document.longitude}</td>
                                </tr>
                                )
                            })
                        }
                        </tbody>
                    </table>
                </div>

                <div className="sidebar">

                    <i id="icons" className="fa-solid fa-map"></i>
                    <Link to={`/heatmap`}>
                        Sitemap
                    </Link>
                    <i id="icons"class="fa-solid fa-video"></i>
                    <Link to={`/camera`}>
                        Cameras
                    </Link>
                    <i id="icons"className="fa-solid fa-location-dot"></i>
                    <Link to={`/marker`}>
                        Markers
                    </Link>
                    <img id="logo"src="crowdsight/src/assets/Nomura A1 (1).png" />
                </div>

           </div>
        </>
    )
}
export default Marker