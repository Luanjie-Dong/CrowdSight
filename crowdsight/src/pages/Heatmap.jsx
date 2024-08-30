import axios from "axios";
import React from "react";

function Heatmap(){
    const backend_endpoint = import.meta.env.VITE_BACKEND_ENDPOINT + "/create_map";

    const config = {
        method: 'get',
        url: backend_endpoint
    }

    axios(config)
    .then((response) => {
        if (response.data !== null) {
            console.log("heatmap successfully retrieved");
            const map_html = response.data;
        } else {
            alert("failed to retrieve heatmap");
        }
    })

    return(
        <>
            <iframe srcdoc={map_html} />
        </>
    )
}
export default Heatmap