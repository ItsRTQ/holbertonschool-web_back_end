export default class Airport {
  /**
  * @param {string} name - name of the airport
  * @param {string} code - code of the airport as of state
  */
  constructor(name, code) {
    if (typeof name !== 'string' || typeof code !== 'string') {
      throw new TypeError('Name and code must be strings');
    }
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('name must be string')
    this._name = value
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') throw TypeError('code must be string')
    this._code = value
  }

  toString() {
    return this._code;
  }
}
