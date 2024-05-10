export default class HolbertonClass {
  /**
  * @param {number} size - size of the class
  * @param {string} location - location of the class
  */
  constructor(size, location) {
    if (typeof size !== 'number' || typeof location !== 'string') {
      throw new TypeError('Size must be a number and location must be a string');
    }

    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    this._size = value
  }

  get location() {
    return this._location;
  }

  set location(value) {
    this._location = value
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
