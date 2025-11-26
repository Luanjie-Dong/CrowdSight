# CrowdSight
![CrowdSight LOGO](./crowdsight/src/assets/Nomura%20A1%20(1).png)

## Overview
Developed for Ellipsis X HST Tech Series Hackathon 2024, CrowdSight enables event organizers to model their event locations and use CCTV footage to visualize crowd density along predetermined exit routes. The system features a dashboard that provides a real-time overview of the event map, layered with a crowd density heatmap around key exit routes. This data allows event organizers and crowd control staff to deploy resources effectively, ensuring the efficient movement of people in and out of the event.

## Features
| Feature | Description | Status |
|---------|-------------|--------|
| **Crowd Heat Map** | Visualizes crowd density using color gradients to highlight dense areas | ✅ Implemented |
| **Customizable Location Map** | Base map can be easily swapped to display detailed crowd information for different venues | ✅ Implemented |
| **Exit Routes** | Displays predefined exit locations on the map to support better decision-making | ✅ Implemented |

## Technical Implementation

- **Computer Vision Model**
   - Implements a computer vision model for analyzing CCTV footage to estimate crowd density
   - Processes real-time video feeds to generate density maps

- **Frontend (NextJS)**
   - Powers the interactive dashboard interface
   - Displays event maps with overlay crowd density heatmaps
   - Provides real-time visualization of crowd movement patterns

- **Backend (Flask API)**
   - Serves as the central API endpoint for data processing
   - Handles communication between computer vision model and frontend
   - Manages data flow and real-time updates


## Running the Application

Follow these steps to run the application:

1. **Ensure that FFmpeg is downloaded:**
   - For Mac: Run `brew install ffmpeg` in the terminal.
   - For Windows: Download from the [FFmpeg website](https://www.ffmpeg.org/download.html).

2. **Start the Frontend Server:**
   - Navigate to the `crowdsight` folder.
   - Run `npm run dev` to start the frontend server.

3. **Start the Backend Server:**
   - Navigate to the `backend` folder.
   - Run `python server.py` to start the backend server.

4. **Access the Application:**
   - Go to [http://localhost:5173/](http://localhost:5173/) in your web browser.
   - You may need to use a private browsing window if certain extensions block some functionality in the app.


## References
This project utilizes a vision model based on the research:
**Sindagi, V. A., & Patel, V. M. (2017).** *CNN-based cascaded multi-task learning of high-level prior and density estimation for crowd counting.*  
[Read the paper here](https://doi.org/10.48550/arXiv.1707.09605)
