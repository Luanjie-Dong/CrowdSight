# CrowdSight

![CrowdSight Dashboard](./crowdsight/src/assets/Nomura A1 (1).png)

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
