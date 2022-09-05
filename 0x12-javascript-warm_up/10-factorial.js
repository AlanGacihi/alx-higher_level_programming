#!/usr/bin/node
const number = parseInt(process.argv[2]);
function fact (n) {
  if (!n) {
    return (1);
  } else {
    return (n * fact(n - 1));
  }
}
console.log(fact(number));
