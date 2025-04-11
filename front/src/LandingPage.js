import React from 'react';
import { Box, Button, Typography, Container
 } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import FastfoodIcon from '@mui/icons-material/Fastfood';
const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <Box
      sx={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)',
        display: 'flex',
        alignItems: 'center',
      }}
    >
      <Container maxWidth="lg">
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            textAlign: 'center',
            color: 'white',
            gap: 4,
          }}
        >
         <FastfoodIcon sx={{ fontSize: 40 }}/>
          <Typography
            variant="h2"
            sx={{
              fontWeight: 700,
              marginBottom: 2,
              textShadow: '0 2px 4px rgba(0,0,0,0.2)',
            }}
          >
            Restaurant Staff Management
          </Typography>
          <Typography
            variant="h5"
            sx={{
              maxWidth: '800px',
              marginBottom: 4,
              opacity: 0.9,
            }}
          >
            Track schedules, manage payroll, and optimize employee performance all in one place.
          </Typography>
          <Button
            variant="contained"
            size="large"
            onClick={() => navigate('/employees')}
            sx={{
              backgroundColor: 'white',
              color: '#1e3c72',
              
              px: 6,
              py: 2,
            }}
          >
            Get Started Today
          </Button>
        </Box>
      </Container>
    </Box>
  );
};

export default LandingPage;