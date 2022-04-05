#!/usr/bin/node
const list = [];
exports.logMe = function (item) {
  let count = 0;
  list.unshift(item);
  console.log((list.length - 1) + ': ' + list[count]);
  count++;
};
