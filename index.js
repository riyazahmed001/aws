// Import the 'fs' module
const fs = require('fs');

// Define the file path
const filePath = 'example.txt';

// Read the file content asynchronously
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }
    // Write the file content to the console
    console.log('File content:', data);
});
