export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
}

let buffer = new ArrayBuffer(length);
let int8View = new DataView(buffer);

try {
    int8View.setInt8(position, value);
} catch (error) {
    throw new Error('Position outside range');
}

return int8View;
}
