export default function cleanSet(set, startString) {
  if (!startString || startString.length === 0) {
    return '';
  }

  const filteredValues = [];
  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      filteredValues.push(value.substring(startString.length));
    }
  }

  return filteredValues.join('-');
}
