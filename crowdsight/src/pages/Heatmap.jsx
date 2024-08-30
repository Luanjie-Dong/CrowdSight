import axios from "axios";
import React from "react";

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
        </>
    )
}
export default Heatmap