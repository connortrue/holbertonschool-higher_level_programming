#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(0);
  process.exit(0);
}

const numbers = process.argv.slice(2).map(Number);

let max = -Infinity; let secondMax = -Infinity;

for (const num of numbers) {
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num < max) {
    secondMax = num;
  }
}

console.log(secondMax === -Infinity ? 0 : secondMax);
