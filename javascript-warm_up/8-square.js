#!/usr/bin/node
const printSquare = (size) => {
  const sizeInt = parseInt(size);

  if (isNaN(sizeInt)) {
    console.log('Missing size');
    return;
  }

  for (let i = 0; i < sizeInt; i++) {
    let row = '';
    for (let j = 0; j < sizeInt; j++) {
      row += 'X';
    }
    console.log(row);
  }
};

printSquare(process.argv[2]);
