#!/usr/bin/node
const input = process.argv[2];
const x = parseInt(input);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < x) {
    console.log('C is fun');
    count++;
  }
}
