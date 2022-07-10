#!/usr/bin/node
function addMeMaybe (n, callback) {
  callback(n + 1);
}

exports.addMeMaybe = addMeMaybe;
