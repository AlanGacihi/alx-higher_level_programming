#!/usr/bin/node
const size = parseInt(process.argv[2]);
let i = 0;
if (!size) {
  console.log('Missing size');
} else {
  for (i; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
