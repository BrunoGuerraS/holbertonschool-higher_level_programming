#!/usr/bin/node
//script that imports a dictionary of occurrences
//by user id and computes a dictionary 
//of user ids by occurrence.
const { dict } = require('./101-data');

const currentValue = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});

console.log(currentValue);
