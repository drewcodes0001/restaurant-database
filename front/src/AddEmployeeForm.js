import React, { useState } from 'react';
import Box from '@mui/material/Box';
import { Input, Typography } from '@mui/material';


function AddEmployeeForm() {
  const [employee, setEmployee] = useState({
    id: '',
    username: '',
    password: '',
    fullname: '',
    wage: ''
  });

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Adjust the URL as needed (if Flask is hosted on a different port)
    const response = await fetch('http://localhost:5000/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(employee)
    });

    if (response.ok) {
      alert('Employee added successfully');
      // Optionally reset the form here
      setEmployee({ id: '', username: '', password: '', fullname: '', wage: '' });
    } else {
      alert('Error adding employee');
    }
  };

  return (
    <Box sx= {{alignContent: 'center', display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center', top: '100px'}}>
      <Typography variant="h4" textAlign='center' color='white'> Add Employee</Typography>
      <form onSubmit={handleSubmit}>
        <input type="text" color= 'white' name="id" placeholder="Id" value={employee.id} onChange={handleChange} />
        <input type="text" name="username" placeholder="Username" value={employee.username} onChange={handleChange} />
        <input type="text" name="password" placeholder="Password" value={employee.password} onChange={handleChange} />
        <input type="text" name="fullname" placeholder="Full Name" value={employee.fullname} onChange={handleChange} />
        <input type="text" name="wage" placeholder="Wage" value={employee.wage} onChange={handleChange} />
        <input type="submit" value="Submit" />
      </form>
    </Box>
  );
}

export default AddEmployeeForm;
