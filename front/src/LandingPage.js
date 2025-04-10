// src/components/LandingPage.jsx
import React from 'react';
import { Box, Button, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import backgroundIMG from'./img.jpeg';

const LandingPage = () => {
  const navigate = useNavigate();

  const handleNavigate = () => {
    navigate("/employees");
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: 'silver',
        padding: 4,
        backgroundImage: `url(${backgroundIMG})`,
        backgroundSize: 'cover',        // makes sure the image covers the entire box
        backgroundPosition: 'center',     // centers the image
        backgroundRepeat: 'no-repeat',
        
        width: '100%',
        fontFamily: 'Fira Code',
        
        
      }}
    >
      <Typography variant="h2" gutterBottom align='center' color= 'white' style={{position: 'absolute',
          top: 200,    
          }}>
        Manage Your Restuarants Employees
      </Typography>
      <Typography variant="h5" gutterBottom color='white' style={{position: 'absolute',
          top: 300,    
          }}>
        Click the button below to manage employees.
      </Typography>
      <Button variant="contained" color="primary" onClick={handleNavigate}>
        Go to Employee Management
      </Button>
    </Box>
  );
};

export default LandingPage;
