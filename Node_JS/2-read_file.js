// Read file and display results.
const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file
    const data = fs.readFileSync(path, 'utf8');

    // Split the file and filter out empty lines.
    const lines = data.trim().split('\n').filter(line => line !== '');

    // Check if the file has any valid data
    if (lines.length <= 1) {
      throw new Error('No valid data found');
    }

    // The first line is the header, so don't include that.
    const headers = lines[0].split(',');
    const students = lines.slice(1);

    // Initialize a structure to keep track of students per field
    const fieldCounts = {};

    students.forEach((studentLine) => {
      // Split the student line and remove extra quotes Im getting
      const [firstname, lastname, age, field] = studentLine.split(',').map(item => item.trim().replace(/"/g, ''));

      if (!field) {
        return; // Skip if there's no field data
      }

      if (!fieldCounts[field]) {
        fieldCounts[field] = [];
      }

      // Push the student's first name into the correct field array
      fieldCounts[field].push(firstname);
    });

    // Log the total number of students
    console.log(`Number of students: ${students.length}`);

    // Log the number of students per field and their names
    for (const field in fieldCounts) {
      if (fieldCounts.hasOwnProperty(field)) {
        console.log(`Number of students in ${field}: ${fieldCounts[field].length}. List: ${fieldCounts[field].join(', ')}`);
      }
    }

  } catch (err) {
    // Catch and throw an error if there is one
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
