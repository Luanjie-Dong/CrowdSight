import axios from "axios";
import React from "react";
import { Link } from 'react-router-dom';

function Camera(){
    const submit = () => {
        event.preventDefault();
    }

    var object = "";

    return(
        <>
           <body id="add">
                   <div id="content">
                           <form action="#">
                           <div id="text">
                   
                    <h1 class="headers">Add Camera</h1>
                    <input type="text" id='cam_name' class="container textvalue" placeholder="Name"/>
                    <input type="text" id='cam_long' class="container textvalue" placeholder="Longitude"/>
                    <input type="text" id='cam_lat'class="container textvalue" placeholder="Latitude"/>
                    <input type="text" id='cam_uri'class="container textvalue" placeholder="URI"/>
                           </div>
                           <button class="container generate" onClick={submit}>Add Camera</button>
                           </form>
                       </div>
                   
                       <div class="sidebar">

                           <i id="icons" class="fa-solid fa-map"></i>
                           <Link to={`/heatmap`}>
                                Sitemap
                            </Link>
                           <img src="crowdsight/src/assets/cctv.png" />
                           <Link to={`/camera`}>
                                Cameras
                            </Link>
                           <i id="icons"class="fa-solid fa-location-dot"></i>
                           <Link to={`/marker`}>
                                Markers
                            </Link>
                           <img id="logo"src="crowdsight/src/assets/Nomura A1 (1).png" />
                       </div>

                       <div class="existing">
                        <table>
                            {/* object */}
                        </table>
                       </div>


           </body>
        </>
    )
}
export default Camera