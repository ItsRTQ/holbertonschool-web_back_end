export default class Building {
  /**
  * 
  * @param {number} sqft 
  */
  constructor(sqft) {
    if (typeof sqft !== 'number') throw TypeError('Sqft must me a number');
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
  
  set sqft(value) {
    if (typeof value !== 'number') throw TypeError('Sqft must me a number');
    this._sqft = value;
  }
  
  evacuationWarningMessage() {
    throw new Error("Class extending Building must override evacuationWarningMessage");
  }
}
