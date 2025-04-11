import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Typography,
  Grid,
} from '@mui/material';

function AddEmployeeForm() {
  const [employee, setEmployee] = useState({
    id: '',
    username: '',
    password: '',
    fullname: '',
    wage: '',
  });

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(employee),
      });

      if (response.ok) {
        alert('Employee added successfully');
        setEmployee({ id: '', username: '', password: '', fullname: '', wage: '' });
      } else {
        alert('Error adding employee');
      }
    } catch (error) {
      alert('Error connecting to server');
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom sx={{ color: '#1e3c72' }}>
        Add Employee
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="ID"
              name="id"
              value={employee.id}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Username"
              name="username"
              value={employee.username}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Password"
              name="password"
              type="password"
              value={employee.password}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Full Name"
              name="fullname"
              value={employee.fullname}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Wage"
              name="wage"
              type="number"
              value={employee.wage}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              size="large"
              fullWidth
              sx={{ mt: 2 }}
            >
              Add Employee
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
}

export default AddEmployeeForm;