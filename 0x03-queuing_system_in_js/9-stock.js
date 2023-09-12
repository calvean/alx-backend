const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Create a Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Data: list of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get an item by its ID
function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

// Function to reserve stock for an item in Redis
async function reserveStockById(itemId, stock) {
  const key = `item.${itemId}`;
  await setAsync(key, stock);
}

// Function to get the current reserved stock for an item from Redis
async function getCurrentReservedStockById(itemId) {
  const key = `item.${itemId}`;
  const stock = await getAsync(key);
  return stock ? parseInt(stock) : 0;
}

// Create the Express server
const app = express();
app.use(express.json());

// Route to get the list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get the product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    const productDetails = { ...item, currentQuantity };
    res.json(productDetails);
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity === 0) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }

  await reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
const port = 1245;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

