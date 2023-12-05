#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Get command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    // Write the response body to the file
    fs.writeFile(filePath, body, { encoding: 'utf8' }, function (err) {
      if (err) throw err;
    });
  } else {
    console.log('Error:', error);
  }
});
