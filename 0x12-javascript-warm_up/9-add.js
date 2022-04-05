#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
if (!isNaN(arg1) && !isNaN(arg2)) {
  console.log(arg1 + arg2);
} else {
  console.log(NaN);
}
