const express = require('express');
const app = express();

// Add your middleware and route handlers here

// Start the server
const port = 8000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
