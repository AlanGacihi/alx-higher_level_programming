#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1;
  const res = [];
  while (length >= 0) {
    res.push(list[length]);
    length--;
  }
  return (res);
};
