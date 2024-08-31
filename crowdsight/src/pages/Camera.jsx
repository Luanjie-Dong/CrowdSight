import axios from "axios";
import React, {useState, useEffect} from "react";
import { Link } from 'react-router-dom';

function Camera(){
    const endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/find"
    const apikey = import.meta.env.VITE_MONGODB_API_KEY;

    const [documents, setDocuments] = useState([]);

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

    useEffect(() => {
        axios(config)
            .then((response) => {
                if (response.data && response.data.documents) {
                    setDocuments(response.data.documents);
                } else {
                    console.error("Failed to retrieve documents");
                }
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const submit = (event) => {
        event.preventDefault();

        const cam_name = document.getElementById("cam_name").value;
        const cam_long = document.getElementById("cam_long").value;
        const cam_lat = document.getElementById("cam_lat").value;
        const cam_url = document.getElementById("cam_url").value;

        const add_endpoint = import.meta.env.VITE_MONGODB_ENDPOINT + "/action/insertOne";
        const add_data = JSON.stringify({
            "dataSource": "ESGeePeeTee",
            "database": "crowdsight",
            "collection": "cctv",
            "document": {
                "name": cam_name,
                "longitude": cam_long,
                "latitude": cam_lat,
                "url": cam_url,
            },
        });

        const add_config = {
            method: 'post',
            url: add_endpoint,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apikey}`,
            },
            data: add_data,
        };

        axios(add_config)
            .then((response) => {
                if (response.data) {
                    alert("Camera added successfully!");
                    location.reload(); // Reload page to show updated data
                } else {
                    alert("Failed to add camera!");
                }
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <div id="add">
            <div id="content">
                <form action="#">
                    <div id="text">
                        <h1 className="headers">Add Camera</h1>
                        <input type="text" id="cam_name" className="container textvalue" placeholder="Name" />
                        <input type="text" id="cam_lat" className="container textvalue" placeholder="Latitude" />
                        <input type="text" id="cam_long" className="container textvalue" placeholder="Longitude" />
                        <input type="text" id="cam_url" className="container textvalue" placeholder="URL" />
                    </div>
                    <button className="container generate" onClick={submit}>Add Camera</button>
                </form>
            </div>

            <div id="marker_list">
                <h1 className="headers">Current Cameras</h1>
                <table id="mrt_stations_list" className="table_list">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Latitude</th>
                            <th>Longitude</th>
                            <th>URL</th>
                        </tr>
                    </thead>
                    <tbody>
                            {documents.map((document, index) => (
                                <tr key={index}>
                                    <td>{document.name}</td>
                                    <td>{document.latitude}</td>
                                    <td>{document.longitude}</td>
                                    <td><a href={document.url}>{document.url}</a></td>
                                </tr>
                            ))}
                        
                    </tbody>
                </table>
            </div>

            <div className="sidebar">
                <i id="icons" className="fa-solid fa-map"></i>
                <Link to={`/heatmap`}>Sitemap</Link>
                <i id="icons" className="fa-solid fa-video"></i>
                <Link to={`/camera`}>Cameras</Link>
                <i id="icons" className="fa-solid fa-location-dot"></i>
                <Link to={`/marker`}>Markers</Link>
                <img id="logo" src="crowdsight/src/assets/Nomura A1 (1).png" />
            </div>
        </div>
    );
}

export default Camera;
