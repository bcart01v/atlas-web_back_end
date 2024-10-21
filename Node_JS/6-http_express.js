// Express server 
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello Atlas School!');
});

app.listen(1245, () => {
    console.log('Express server is running on port 1245');
});

module.exports = app;
