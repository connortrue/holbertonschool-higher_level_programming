#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the <link>Star Wars</link> API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a GET request to the API endpoint
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(`${movieData.title}`);
  } else {
    console.error(`Error fetching movie data: ${error}`);
  }
});
