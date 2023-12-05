#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = 18;

// Make a GET request to the API endpoint
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    // Filter the films where Wedge Antilles is present
    const filmsWithWedge = filmsData.results.filter(film =>
      film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)
    );
    console.log(`Number of movies where Wedge Antilles is present: ${filmsWithWedge.length}`);
  } else {
    console.error(`Error fetching movie data: ${error}`);
  }
});
