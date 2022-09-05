#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  for (i; i < x; i++) {
    theFunction();
  }
};
