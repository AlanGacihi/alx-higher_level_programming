#!/usr/bin/node
const times = parseInt(process.argv[2]);
let i = 0;
if (!times) {
  console.log('Missing number of occurrences');
} else {
  for (i; i < times; i++) {
    console.log('C is fun');
  }
}
