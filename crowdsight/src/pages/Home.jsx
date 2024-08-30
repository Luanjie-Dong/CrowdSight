function Home(){
    function submit(){
        event.preventDefault()
        console.log('heatmap')

    }
    return(
        <> 
            <div id="content">
                <form action="#">
                <div id="AOI">
                    
                    <h1 class="headers">Area of Interest</h1>
                    <input type="text" class="AOI-input" placeholder="Longitude 1"/>
                    <input type="text" class="AOI-input" placeholder="Latitude 1"/>
                    <input type="text" class="AOI-input" placeholder="Longitude 2"/>
                    <input type="text" class="AOI-input" placeholder="Longitude 2"/>
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