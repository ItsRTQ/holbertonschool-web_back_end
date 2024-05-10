import Building from './5-building';

export default class SkyHighBuilding extends Building {
  /**
   * SkyHighBuilding is object that represents a Building
   * @param {number} sqft - sqare feats of building
   * @param {number} floors - Amount of floor on building
   */
  constructor(sqft, floors) {
    super(sqft);
    if (typeof floors !== 'number') throw TypeError('Floors must be a number');
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    if (typeof value !== 'number') throw TypeError('Floors must be a number');
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
