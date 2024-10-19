// Read file asynchronously and display results.
// This Follows the same structure as the previous task.

const fs = require('fs/promises');

function countStudents(path) {
    return fs.readFile(path, 'utf-8')
    .then((data) => {
        // Same thought as before, split file filter empty.
        const lines = data.trim().split('\n').filter(line => line !== '');

        if (lines.length <= 1) {
            throw new Error('No valid data found');
        }

        const headers = lines[0].split(',');

        const students = lines.slice(1);
        const fieldCounts = {};

        students.forEach((studentLine) => {
            const [firstname, lastname, age, field] = studentLine.split(',').map(item => item.trim().replace(/"/g, ''));

            if (!fieldCounts[field]) {
                fieldCounts[field] = [];
            }

            fieldCounts[field].push(firstname);
        });

        const totalStudents = students.length;
        console.log(`Number of students: ${totalStudents}`);

        for (const [field, students] of Object.entries(fieldCounts)) {
            console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        }
    })
    .catch((err) => {
        throw new Error('Cannot load the database');
    });
}
module.exports = countStudents;
