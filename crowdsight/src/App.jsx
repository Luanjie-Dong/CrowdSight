import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './pages/Home.jsx'
import Heatmap from './pages/Heatmap.jsx'
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
        <Route element={<Heatmap />} />
      </Route>,
      
    ),
  );
  return(
  <>
    <RouterProvider router={router} />
  </>)
}

export default App
