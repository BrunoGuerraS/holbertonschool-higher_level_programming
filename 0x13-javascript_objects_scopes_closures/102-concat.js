#!/usr/bin/node
const fs = require('fs');

const cnstA = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const cnstB = fs.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });

const cnstC = cnstA.concat(cnstB);

fs.writeFile(process.argv[4], cnstC, 'utf8', function (err, result) { if (err) console.log('error', err); });
