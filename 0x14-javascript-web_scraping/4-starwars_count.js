#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let filmCount = 0;

request(url, function (error, response, body) {
  if (error === null) {
    const films = JSON.parse(body);
    const res = films.results;
    for (const film of res) {
      const characters = film.characters;
      for (const charac of characters) {
        if (charac.search('18') > 0) {
          filmCount++;
        }
      }
    }
  }
  console.log(filmCount);
});
