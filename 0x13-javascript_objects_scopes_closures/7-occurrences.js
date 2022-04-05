#!/usr/bin/node
function nbOccurences (list, look) {
  const nm = list.reduce((count, e) => e === look ? count + 1 : count, 0);
  return (nm);
}
exports.nbOccurences = nbOccurences;
