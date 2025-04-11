import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Typography,
  Grid,
} from '@mui/material';

function RemoveEmployeeForm() {
  const [idToRemove, setIdToRemove] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/delete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id_remove: idToRemove }),
      });

      if (response.ok) {
        alert('Employee removed successfully');
        setIdToRemove('');
      } else {
        alert('Error removing employee');
      }
    } catch (error) {
      alert('Error connecting to server');
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom sx={{ color: '#1e3c72' }}>
        Remove Employee
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <TextField
              fullWidth
              label="Employee ID"
              name="id_remove"
              value={idToRemove}
              onChange={(e) => setIdToRemove(e.target.value)}
              variant="outlined"
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              type="submit"
              variant="contained"
              color="error"
              size="large"
              fullWidth
              sx={{ mt: 2 }}
            >
              Remove Employee
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
}

export default RemoveEmployeeForm;