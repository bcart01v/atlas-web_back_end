// http express
const express = require('express');
const fs = require('fs/promises');
const app = express();

const databaseFile = process.argv[2];

if (!databaseFile) {
    console.error('Error: The database file must be provided as a command-line argument');
    process.exit(1); 
}

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
    if (!databaseFile) {
        res.status(500).send('Database file not provided.');
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

        let output = 'This is the list of our students\n';
        output += `Number of students: ${students.length}\n`;

        for (const [field, studentList] of Object.entries(fieldCounts)) {
            output += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
        }

        res.set('Content-Type', 'text/plain');
        res.send(output);

    } catch (err) {
        res.status(500).send(`Cannot load the database: ${err.message}`);
    }
});

app.listen(1245, () => {
    console.log('Express server is running on port 1245');
});

module.exports = app;