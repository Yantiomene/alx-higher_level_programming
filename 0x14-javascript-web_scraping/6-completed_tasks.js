#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const taskCom = {};

request(url, function (err, response, body) {
  if (err === null) {
    const tasks = JSON.parse(body);

    for (const task of tasks) {
      if (task.userId in taskCom) {
        if (task.completed) {
          taskCom[task.userId] += 1;
        }
      } else {
        if (task.completed) {
          taskCom[task.userId] = 1;
        }
      }
    }
    console.log(taskCom);
  }
});
