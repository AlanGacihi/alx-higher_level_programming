#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
      if (err) console.log(err);
    });
  }
});
