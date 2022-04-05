#!/usr/bin/node
const size = parseInt(process.argv[2]);
const square = [];

if (isNaN(size)) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) square.push('X');
  square.forEach(() => console.log(square.join('')));
}
