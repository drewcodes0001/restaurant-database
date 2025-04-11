import React from 'react';
import { Box, Container, Paper, Typography, Button } from '@mui/material';
import { ArrowLeft } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import AddEmployeeForm from './AddEmployeeForm';
import RemoveEmployeeForm from './RemoveEmployeeForm';

const EmployeeManagement = () => {
  const navigate = useNavigate();

  return (
    <Box
      sx={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)',
        py: 4,
      }}
    >
      <Container maxWidth="md">
        <Button
          startIcon={<ArrowLeft />}
          onClick={() => navigate('/')}
          sx={{ color: 'white', mb: 4 }}
        >
          Back to Home
        </Button>
        <Typography
          variant="h2"
          sx={{
            color: 'white',
            textAlign: 'center',
            mb: 6,
            textShadow: '0 2px 4px rgba(0,0,0,0.2)',
          }}
        >
          Employee Management
        </Typography>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <Paper
            
            sx={{
              p: 4,
              
              backgroundColor: 'white',
            }}
          >
            <AddEmployeeForm />
          </Paper>
          <Paper
            
            sx={{
              p: 4,
              
              backgroundColor: 'white',
            }}
          >
            <RemoveEmployeeForm />
          </Paper>
        </Box>
      </Container>
    </Box>
  );
};

export default EmployeeManagement;