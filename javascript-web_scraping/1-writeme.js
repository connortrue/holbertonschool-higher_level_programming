#!/usr/bin/node
const fs = require('fs');

// Get the file path and the string to write from command line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred during writing
  }
});
