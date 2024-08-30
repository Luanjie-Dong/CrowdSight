import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './pages/Home.jsx'
import Heatmap from './pages/Heatmap.jsx'
import Camera from './pages/Camera.jsx'
import Marker from './pages/Markers.jsx'
import React from 'react'
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route
        path="/"
      >
        <Route index element={<Home />} />
        <Route path="heatmap" element={<Heatmap />} />
        <Route path="camera" element={<Camera />} />
        <Route path="marker" element={<Marker />} />
      </Route>,
      
    ),
  );
  return(
  <>
    <RouterProvider router={router} />
  </>)
}

export default App
