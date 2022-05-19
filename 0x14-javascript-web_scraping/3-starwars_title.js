#!/usr/bin/node
const axios = require('axios');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(`${url}${movieId}`)
  .then(resp => {
    console.log(resp.data.title);
  });
