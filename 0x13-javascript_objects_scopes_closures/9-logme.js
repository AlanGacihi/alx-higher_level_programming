#!/usr/bin/node
let current = 0;
exports.logMe = function (item) {
  console.log(current + ': ' + item);
  current++;
};
