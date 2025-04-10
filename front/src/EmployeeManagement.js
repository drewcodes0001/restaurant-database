import React from 'react';
import AddEmployeeForm from './AddEmployeeForm';
import RemoveEmployeeForm from './RemoveEmployeeForm';
import { Box, Typography } from '@mui/material';
import backimg from './img.jpeg';

const EmployeeManagement = () => {
  return (
    <Box sx={{ p: 4,  justifyContent: 'center', alignItems: 'center', display: 'flex',
        flexDirection: 'column', backgroundSize: 'cover',     
        backgroundPosition: 'center',     
        backgroundRepeat: 'no-repeat',
       
        
        width: '100%', }} >
      <Typography variant="h2" gutterBottom color='white'>
        Employee Management
      </Typography>
      <AddEmployeeForm />
      <RemoveEmployeeForm />
    </Box>
  );
};

export default EmployeeManagement;
