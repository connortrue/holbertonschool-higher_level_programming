#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of Rectangle
    super(size, size);
  }
};
