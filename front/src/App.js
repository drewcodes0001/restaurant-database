// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './LandingPage';
import EmployeeManagement from './EmployeeManagement';
import { Box } from '@mui/material';

function App() {
  return (
    <Box sx={{backgroundColor: 'silver'}}>
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/employees" element={<EmployeeManagement />} />
      </Routes>
    </Router>
    </Box>
  );
}

export default App;
