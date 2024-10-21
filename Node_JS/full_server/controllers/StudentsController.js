    // Get students logic

    import { readDatabase } from '../utils.js';

    class StudentsController {
        static async getAllStudents(req, res) {
            const filePath = process.argv[2];
            try {
                const fields = await readDatabase(filePath);
                let responseText = 'This is the list of our students\n';

                Object.keys(fields).sort().forEach((field) => {
                    responseText += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
                });

                res.status(200).send(responseText);
            } catch (error) {
                res.status(500).send('Cannot load the database');
            }
        }

        static async getAllStudentsByMajor(req, res) {
            const filePath = process.argv[2];
            const { major } = req.params;

            if (major !== 'CS' && major !== 'SWE') {
                res.status(500).send('Major parameter must be CS or SWE');
                return;
            }

            try {
                const fields = await readDatabase(filePath);

                if (!fields[major]) {
                    res.status(500).send('Major not found');
                    return;
                }

                res.status(200).send(`List: ${fields[major].join(', ')}`);
            } catch (error) {
                res.status(500).send('Cannot load the database');
            }
        }
    }

    export default StudentsController;