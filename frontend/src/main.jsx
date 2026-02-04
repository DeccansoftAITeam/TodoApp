/**
 * @fileoverview Application entry point - Bootstraps and renders the React application.
 * @module main
 */

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

/**
 * Initialize and render the React application.
 * Uses StrictMode for highlighting potential problems in the application.
 */
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
