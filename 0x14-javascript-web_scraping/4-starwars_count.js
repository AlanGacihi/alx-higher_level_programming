#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const movies = JSON.parse(body).results;
    let count = 0;
    let characters = [];
    for (const movie of movies) {
      characters = characters.concat(movie.characters);
    }
    count = characters.filter(x => x.includes('18')).length;
    console.log(count);
  }
});
