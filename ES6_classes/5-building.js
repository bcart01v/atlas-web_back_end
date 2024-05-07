export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error('Building cannot be called directly.');
    }
    if (this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must ovverride evacuationWarnningMessage');
    }
  this._sqft_sqft
  }

  get sqft() {
    return this._sqft
  }
}
