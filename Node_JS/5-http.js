// http server
// I tried using 3-read_file but it would only output to the console from
// the server side console, and I didn't want to change that program
// for this, so it's done here.
const http = require('http');
const fs = require('fs/promises');

const databaseFile = process.argv[2];

const app = http.createServer(async (req, res) => {
    if (req.url === '/') {
        // Root path response
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Atlas School!');

    } else if (req.url === '/students') {
        // Students path response
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('This is the list of our students\n');

        if (!databaseFile) {
            res.write('Database file not provided.');
            res.end();
            return;
        }

        try {
            const data = await fs.readFile(databaseFile, 'utf-8');
            const lines = data.trim().split('\n').filter(line => line !== '');

            if (lines.length <= 1) {
                throw new Error('No valid data found');
            }

            const students = lines.slice(1);
            const fieldCounts = {};

            students.forEach((studentLine) => {
                const [firstname, lastname, age, field] = studentLine.split(',').map(item => item.trim().replace(/"/g, ''));

                if (!fieldCounts[field]) {
                    fieldCounts[field] = [];
                }

                fieldCounts[field].push(firstname);
            });

            let output = `Number of students: ${students.length}\n`;

            for (const [field, studentList] of Object.entries(fieldCounts)) {
                output += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
            }

            res.write(output);
        } catch (err) {
            res.write(`Cannot load the database: ${err.message}`);
        } finally {
            res.end();
        }
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

app.listen(1245, () => {
    console.log('Server is running on port 1245');
});

module.exports = app;
