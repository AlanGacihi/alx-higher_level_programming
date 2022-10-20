#!/usr/bin/node
const request = require('request');
request('https://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    const dict = {};
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err2, res2, body2) {
        if (err) console.log(err);
        else {
          dict[i] = JSON.parse(body2).name;
          if (Object.entries(dict).length === characters.length) for (const key in dict) console.log(dict[key]);
        }
      });
    }
  }
});
