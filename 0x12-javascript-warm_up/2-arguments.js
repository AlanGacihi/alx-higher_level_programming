#!/usr/bin/node
const nargs = process.argv.length;
if (nargs === 2) {
  console.log('No argument');
} else if (nargs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
