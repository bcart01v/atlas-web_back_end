// Creating a small HTTP Server.

const http = require('http');

// Server Creation and response defitinions
const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    res.end('Hello Atlas School!');
});

// Listener
app.listen(1245, () => {
    console.log('Server is running on port 1245');
});

module.exports = app;
