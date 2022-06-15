#!/usr/bin/node
// cript that gets the contents of a webpage and stores it in a file
const axios = require('axios').default;
const fs = require('fs');
const [url, filePath] = process.argv.slices(2);

axios.get(url)
  .then(({ data }) => {
    fs.writeFile(filePath, data, 'utf8', err => {
      if (err) console.log(err.message);
    });
  })
  .catch(({ message }) => console.log(message));
