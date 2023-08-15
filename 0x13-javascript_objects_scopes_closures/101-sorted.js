#!/usr/bin/node

const dic = require('./101-data').dict;
const newDic = {};

Object.keys(dic).map(function (key) {
  if (newDic[dic[key]] === undefined) {
    newDic[dic[key]] = [];
  }
  newDic[dic[key]].push(key);
});

console.log(newDic);
