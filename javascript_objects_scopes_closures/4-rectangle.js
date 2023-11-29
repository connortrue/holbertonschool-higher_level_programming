#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Print the rectangle using 'X' character
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    // Swap width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Multiply width and height by 2
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
