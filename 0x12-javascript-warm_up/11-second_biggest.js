#!/usr/bin/node

let big = 0;
const listNum = [];
let i;

for (i = 2; i < process.argv.length; i++) {
  if (!Number.isNaN(parseInt(process.argv[i]))) {
    listNum[i - 2] = parseInt(process.argv[i]);
  }
}

if (listNum.length > 1) {
  big = Math.max.apply(null, listNum);
  i = listNum.indexOf(big);
  listNum[i] = -Infinity;
  big = Math.max.apply(null, listNum);
}

console.log(big);
