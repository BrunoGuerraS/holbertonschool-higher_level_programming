#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];

console.log(url);
axios.get(url)
  .then(res => {
    console.log('code: ', res.status);
  })
  .catch(err => {
    console.log('code :', err.response.status);
  });
