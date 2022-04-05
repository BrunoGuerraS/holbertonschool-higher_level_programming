#!/usr/bin/node
if (!process.argv[2] || parseInt(process.argv[2]) === 1) {
  console.log(0);
} else {
  const list = [];
  for (let i = 2; i < process.argv.length; i++) {
    list.push(parseInt(process.argv[i]));
  }
  list.sort(function (a, b) {
    return (b - a);
  });
  console.log(list[0]);
}
