#!/usr/bin/node
class Square extends Square {
  constructor (size) {
    // Call the constructor of Square
    super(size);
  }

  charPrint (c) {
    // If c is undefined, use 'X'
    c = c || 'X';

    // If width and height are both 0, do not print anything
    if (this.width === 0 || this.height === 0) {
      return;
    }

    // Print the square using 'c' character
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }
}
