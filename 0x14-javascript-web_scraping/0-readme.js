#!/usr/bin/node
const arguments = process.argv.slice(process.argv.length - 1);
const fs = require('fs');

fs.readFile(arguments.toString(), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
