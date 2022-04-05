#!/usr/bin/node
const list = process.argv.splice(2).map((e) => parseInt(e)).sort((a, b) => b - a);
if (list.length <= 1) console.log(0);
else console.log(list[1]);
