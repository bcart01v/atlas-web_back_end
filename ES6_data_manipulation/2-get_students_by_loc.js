export default function getSutdentsByLocation(students, city) {
  return students.filter((student) => student.location === city);
}
