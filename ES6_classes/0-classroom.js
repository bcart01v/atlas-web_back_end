export default class ClassRoom {
  constructor (maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }

  getMaxStudentSize() {
    return this._maxStudentsSize;
  }
}
