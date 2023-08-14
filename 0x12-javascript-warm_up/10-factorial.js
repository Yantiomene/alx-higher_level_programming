#!/usr/bin/node

function fact (a) {
  if (Number.isNaN(a) || a === 1) {
    return (1);
  }
  return (a * fact(a - 1));
}

const n = parseInt(process.argv[2]);

console.log(fact(n));
