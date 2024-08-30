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
            <embed type="text/html" src={map_html} width="1200" height="800"></embed>
        </>
    )
}
export default Heatmap