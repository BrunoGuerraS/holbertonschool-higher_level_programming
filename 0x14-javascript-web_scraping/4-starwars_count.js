#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];
const search = '18';
let totalMovies = 0;

axios.get(url)
  .then(res => {
    const films = res.data.results;
    const size = films.length;
    for (let i = 0; i < size; i++) {
      films[i].characters.forEach(ch => {
        if (ch.includes(search)) {
          totalMovies++;
        }
      });
    }
    console.log(totalMovies);
  })
  .catch(err => {
    console.log('Error', err);
  });
