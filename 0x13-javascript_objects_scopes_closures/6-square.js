#!/usr/bin/node
const squ = require('./5-square');
let character = 'X';
module.exports = class Square extends squ {
  charPrint (c) {
    if (c) {
      character = c;
    }
    console.log((character.repeat(this.width) + '\n').repeat(this.height - 1) + character.repeat(this.width));
  }
};
