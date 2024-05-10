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

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
