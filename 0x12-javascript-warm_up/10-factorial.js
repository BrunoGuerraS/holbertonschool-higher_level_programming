#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!num) {
  console.log(1);
} else {
  function factorial (n) {
    if (n < 0) return;
    if (n < 2) return 1;
    return (n * factorial(n - 1));
  }
  console.log(factorial(num));
}
