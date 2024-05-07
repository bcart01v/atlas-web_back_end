export default function getListStudents() {
  const firstentry = { id: 1, firstName: 'Guillaume', location: 'San Francisco' };
  const secondentry = { id: 2, firstName: 'James', location: 'Columnbia' };
  const thirdentry = { id: 5, firstName: 'Serena', location: 'San Franscisco'};
  const ReturnArray = [firstentry, secondentry, thirdentry];
  return ReturnArray;
}