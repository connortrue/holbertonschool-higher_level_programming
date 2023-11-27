#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = null;
      this.height = null;
    }
  }

    if (this.width === null || this.height === null) {
      return 'Empty object';
    } else {
      let rectangle = '';
      for (let i = 0; i < this.height; i++) {
        rectangle += 'X'.repeat(this.width) + '\n';
      }
      return rectangle;
    }
  }
}
