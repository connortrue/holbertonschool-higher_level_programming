#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object
      this.width = 0;
      this.height = 0;
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
    this.width = this.width * 4;
    this.width = this.height * 4;
  }
}
