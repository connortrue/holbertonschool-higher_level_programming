#!/usr/bin/node
const request = require('request');

// API URL
const url = 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API URL
request(url, function (error, response, body) {
  if (!error && response.statusCode == 200) {
      // Parse the response body to JSON
      const todos = JSON.parse(body);

      // Create an object to store the number of tasks completed by each user
      const completedTasks = {};

      // Iterate over the tasks
      todos.forEach(function(todo) {
          // If the task is completed and the user id is not already in the object, add it
          if (todo.completed && !completedTasks[todo.userId]) {
              completedTasks[todo.userId] = 1;
          } else if (todo.completed) {
              // If the user id is already in the object, increment the count
              completedTasks[todo.userId]++;
          }
      });

      // Print the number of tasks completed by each user
      for (let userId in completedTasks) {
          console.log(completedTasks);
      }
  } else {
      console.log('Error:', error);
  }
});
