#!/usr/bin/node

const SquareS = require('./5-square');

class Square extends SquareS {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rect = '';
        for (let j = 0; j < this.width; j++) {
          rect += 'C';
        }
        console.log(rect);
      }
    }
  }
}

module.exports = Square;
