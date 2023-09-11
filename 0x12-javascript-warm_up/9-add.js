#!/usr/bin/node

const firstint = process.argv[2];
const secondint = process.argv[3];

if (isNaN(firstint) || isNaN(secondint)) {
  console.log('NaN');
} else {
  console.log(add(parseInt(firstint), parseInt(secondint)));
}

function add (a, b) {
  return a + b;
}
