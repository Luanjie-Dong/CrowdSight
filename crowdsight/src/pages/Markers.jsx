import axios from "axios";
import React from "react";

function Marker(){
    const submit = () => {
        event.preventDefault();
        console.log('yay');
    }
    return(
        <>
           <body id="add">
                   <div id="content">
                           <form action="#">
                           <div id="text">
                   
                    <h1 class="headers">Add Marker</h1>
                    <input type="text" id='cam_name' class="container textvalue" placeholder="Name"/>
                    <input type="text" id='cam_long' class="container textvalue" placeholder="Longitude"/>
                    <input type="text" id='cam_lat'class="container textvalue" placeholder="Latitude"/>
                           </div>
                           <button class="container generate" onClick={submit}>Add Camera</button>
                           </form>
                       </div>
                   
                       <div class="sidebar">
                           <i id="icons" class="fa-solid fa-map"></i>
                           <a href="#sitemap">Sitemap</a>
                           <img src="crowdsight/src/assets/cctv.png" />
                           <a href="#camera">Cameras</a>
                           <i id="icons"class="fa-solid fa-location-dot"></i>
                           <a href="#Marker">Markers</a>
                           <img id="logo"src="crowdsight/src/assets/Nomura A1 (1).png" />
                         </div>

           </body>
        </>
    )
}
export default Marker