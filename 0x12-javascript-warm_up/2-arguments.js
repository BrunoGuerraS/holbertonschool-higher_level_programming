#!/usr/bin/node
const lonarg = process.argv.length - 2;
const print = console.log;

if (!lonarg) print('No argument');
if (lonarg === 1) print('Argument found');
if (lonarg > 1) print('Arguments found');
