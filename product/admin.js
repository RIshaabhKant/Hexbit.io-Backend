// index.html:
// html
// code
<!DOCTYPE html>
<html>
  <head>
    <title>Product Admin</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="/bundle.js"></script>
  </body>
</html>
// theme.js:
//t
// code
import { createTheme } from '@material-ui/core/styles';

const theme = createTheme();

export default theme;
// App.js:
//t
// code
import React, { useState, useEffect } from 'react';
import { ThemeProvider } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import ProductList from './components/ProductList';
import ProductForm from './components/ProductForm';
import theme from './theme';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products from the server and update the state
  }, []);

  const handleProductSubmit = (productData) => {
    // Send product data to the server for creation or update
  };

  return (
    <ThemeProvider theme={theme}>
      <Container maxWidth="md">
        <Typography variant="h4" component="h1" align="center" gutterBottom>
          Product Admin
        </Typography>
        <ProductList products={products} />
        <ProductForm onSubmit={handleProductSubmit} />
      </Container>
    </ThemeProvider>
  );
}

export default App;
// index.js:
//t
// code
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
In the admin/backend directory, create an Express.js application:
app.js:
//t
// code
const express = require('express');
const path = require('path');
const productRoutes = require('../routes/productRoutes');

const app = express();

// Set up middleware, database connection, and other configurations

app.use('/products', productRoutes);

app.use(express.static(path.join(__dirname, '../frontend/public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/public/index.html'));
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});