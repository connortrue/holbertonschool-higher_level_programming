#!/usr/bin/node
const findSecondLargest = (...args) => {
  if (args.length <= 1) {
    console.log(0);
    return;
  }

  const numbers = args.map(Number);
  const sortedNumbers = numbers.sort((a, b) => b - a);
  const secondLargest = sortedNumbers[1];

  console.log(secondLargest);
};
