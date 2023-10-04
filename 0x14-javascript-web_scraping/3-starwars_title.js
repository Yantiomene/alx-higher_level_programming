#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + id, function (error, response, body) {
  if (error === null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});