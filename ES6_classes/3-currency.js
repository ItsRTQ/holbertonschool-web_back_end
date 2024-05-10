export default class Currency {
  /**
  *
  * @param {String} code - Code of currency
  * @param {String} name - name of currency
  */
  constructor(code, name) {
    if (typeof code !== 'string') throw TypeError('code must be string');
    if (typeof name !== 'string') throw TypeError('name must be string');
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') throw TypeError('code must be string');
    this._code = value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('name must be string');
    this._name = value;
  }

  displayFullCurrency() {
    return '${this._name} (${this._code})';
  }
}
