// src/components/RemoveEmployeeForm.js
import React, { useState } from 'react';
import { Typography } from '@mui/material';

function RemoveEmployeeForm() {
  const [idToRemove, setIdToRemove] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:5000/delete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id_remove: idToRemove })
    });

    if (response.ok) {
      alert('Employee removed successfully');
      setIdToRemove('');
    } else {
      alert('Error removing employee');
    }
  };

  return (
    <div>
      <Typography variant="h4" textAlign='center' color='white'> Remove Employee</Typography>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="id_remove"
          placeholder="Id"
          value={idToRemove}
          onChange={(e) => setIdToRemove(e.target.value)}
        />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default RemoveEmployeeForm;
