#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If width or height is not a positive integer or equal to 0, create an empty object
      this.width = null;
      this.height = null;
    } else {
      // Initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === null || this.height === null) {
      console.log('Empty object');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
