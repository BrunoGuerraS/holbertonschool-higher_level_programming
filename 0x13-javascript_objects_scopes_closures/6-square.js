#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      const area = [];
      for (let i = 0; i < this.width; i++) {
        area.push(c);
      }
      for (let j = 0; j < this.height; j++) {
        console.log(area.join(''));
      }
    }
  }
}
module.exports = Square;
