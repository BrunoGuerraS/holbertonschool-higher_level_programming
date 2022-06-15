#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];
const [result, endResult] = [{}, {}];

axios.get(url)
  .then(({ data }) => {
    data.forEach(task => {
      if (result[task.userId] === undefined) result[task.userId] = 0;
      if (task.completed) result[task.userId]++;
    });
    Object.keys(result).forEach(key => {
      if (result[key]) endResult[key] = result[key];
    });
    console.log(endResult);
  })
  .catch(({ mes }) => console.log(mes));
