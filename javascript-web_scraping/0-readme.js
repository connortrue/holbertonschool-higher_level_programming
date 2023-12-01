#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line argument
const filePath = process.argv[2];

// Read and print the content of the file
fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.error(err); // Print the error object if an error occurred during reading
  } else {
    console.log(data); // Print the content of the file
  }
});
