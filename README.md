# CrowdSight

![CrowdSight Dashboard](./crowdsight/src/assets/Nomura%20A1%20(1).png)

## Project Description

CrowdSight enables event organizers to model their event locations and use CCTV footage to visualize crowd density along predetermined exit routes. The system features a dashboard that provides a real-time overview of the event map, layered with a crowd density heatmap around key exit routes. This data allows event organizers and crowd control staff to deploy resources effectively, ensuring the efficient movement of people in and out of the event.

## Project Reference

This project utilizes a vision model based on the work of Sindagi, V. A., & Patel, V. M. (2017). CNN-based cascaded multi-task learning of high-level prior and density estimation for crowd counting. You can read more about this model [here](https://doi.org/10.48550/arXiv.1707.09605).

## Project Features

### Backend
- **Model**: Implements a computer vision model for analyzing CCTV footage to estimate crowd density.
- **Heatmap**: Generates layered maps of the event venue, visualizing crowd density on top of the event layout.

### Frontend
- **CrowdSight**: The frontend code that powers the dashboard, providing the view of the event map with the crowd density heatmap.

To run the application:
1: ensure that ffmpeg is downloaded 
    for mac , run brew install ffmpeg in the terminal
    for windows, download from the link here https://www.ffmpeg.org/download.html

2: go to the crowdsight folder and use npm run dev to start the frontend server

3: go to the backend folder use python server.py to start the backend server

4: go to http://localhost:5173/ in your web browser to access the app, you may need to use a private browser as certain extentions block some of the function in our app
