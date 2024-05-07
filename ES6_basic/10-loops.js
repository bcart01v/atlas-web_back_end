export default function appendToEachArrayValue(array, appendString) {
  let output = [];
  for (const value of array) {
    output.push(appendString + value);
  }

  return output;
}
