#!/usr/bin/node
const request = require('request');

function getCompletedTasks(url) {
 return new Promise((resolve, reject) => {
  url = process.argv[2];
  request(url, (error, response, body) => {
    if (error) {
      reject(error);
    } else {
      const tasks = JSON.parse(body);
      const userTasks = tasks.filter(task => task.completed);
      const userCounts = {};

      userTasks.forEach(task => {
        if (userCounts[task.userId]) {
          userCounts[task.userId]++;
        } else {
          userCounts[task.userId] = 1;
        }
      });

      console.log(userCounts);
      resolve(userCounts);
    }
  });
 });
}

getCompletedTasks(process.argv[2])
 .catch(error => console.error(error));
