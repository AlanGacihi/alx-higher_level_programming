#!/usr/bin/node
const fs = require('fs');
let f1;
let f2;
let res;
if (process.argv.length > 4) {
  f1 = fs.readFileSync(process.argv[2], 'utf8');
  f2 = fs.readFileSync(process.argv[3], 'utf8');
  res = f1 + f2;
  fs.writeFile(process.argv[4], res, function (err) { if (err) throw err; });
}
