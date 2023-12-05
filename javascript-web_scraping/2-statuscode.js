#!/usr/bin/node
const request = require('request');

// Get the URL from the command line argument
const url = process.argv[2];

// Perform the GET request
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`); // Display the status code
  }
});
