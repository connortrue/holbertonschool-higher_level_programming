#!/usr/bin/node
exports.esrever = function (list) {
  // Create an empty array to store the reversed list
  const reversedList = [];

  // Iterate through the input list from the end to the beginning
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
