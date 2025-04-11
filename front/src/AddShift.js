import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Typography,
  Grid,
} from '@mui/material';

function AddShift() {
  const [shift, setShift] = useState({
    shift_id: '',
    date: '',
    duration: ''
  });

  const handleChange = (e) => {
    setShift({ ...shift, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/add_shift', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(shift),
      });

      if (response.ok) {
        alert('Shift added successfully');
        setShift({ shift_id: '', date: '', duration: '' });
      } else {
        alert('Error adding shift');
      }
    } catch (error) {
      alert('Error connecting to server');
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom sx={{ color: '#1e3c72' }}>
        Add Shift
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Shift_Id"
              name="shift_id"
              value={shift.shift_id}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Date"
              name="date"
              value={shift.date}
              onChange={handleChange}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Duration"
              name="duration"
              type="duration"
              value={shift.duration}
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
              Add Shift
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
}

export default AddShift;