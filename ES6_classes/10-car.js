export default class Car {
  /**
   * This class represents a car
   * @param {String} brand - brand of the car
   * @param {String} motor - motor of the car
   * @param {String} color - color of the car
   */
  constructor(brand, motor, color) {
    if (typeof brand !== 'string' || typeof motor !== 'string' || typeof color !== 'string') {
      throw TypeError('Brand, Motor, and color of car must be type string');
    }
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  set brand(value) {
    this._brand = value;
  }

  get motor() {
    return this._motor;
  }

  set motor(value) {
    this._motor = value;
  }

  get color() {
    return this._color;
  }

  set color(value) {
    this._color = value;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Clone = this.constructor[Symbol.species];
    return new Clone(this._brand, this._motor, this._color);
  }
}
