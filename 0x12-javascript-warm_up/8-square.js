#!/usr/bin/node
const x = parseInt(process.argv[2]);
const square = [];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    square.push('x');
  }
  square.forEach(() => console.log(square.join('')));
}
