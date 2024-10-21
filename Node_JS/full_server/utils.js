// Utilities
import fs from 'fs/promises';

export async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf-8');
        const lines = data.trim().split('\n').filter(line => line !== '');

        if (lines.length <= 1) {
            throw new Error('No valid data found');
        }

        const headers = lines[0].split(',');
        const students = lines.slice(1);
        
        const fields = {};

        // Process each line (student)
        students.forEach((line) => {
            const studentData = line.split(',');
            const firstname = studentData[0].trim().replace(/"/g, '');
            const field = studentData[3].trim().replace(/"/g, '');

            if (!fields[field]) {
                fields[field] = [];
            }

            fields[field].push(firstname);
        });

        return fields;
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}