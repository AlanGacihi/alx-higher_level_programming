#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const todos = JSON.parse(body);
    const ans = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (!ans[todo.userId]) ans[todo.userId] = 1;
        else ans[todo.userId]++;
      }
    }
    console.log(ans);
  }
});
