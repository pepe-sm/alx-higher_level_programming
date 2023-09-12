#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      c++;
    }
  }
  return c;
};
