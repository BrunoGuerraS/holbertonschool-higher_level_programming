#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (const e of list) {
    reverse.unshift(e);
  }
  return reverse;
};
