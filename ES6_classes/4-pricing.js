import Currency from './3-currency'

export default class Pricing {
  /**
  *
  * @param {Number} amount - quantity of this currency
  * @param {Currency} currency - working currency
  */
  constructor(amount, currency) {
    if (typeof amount !== 'number') throw TypeError("Amount must be a number");
    if (typeof currency !== 'Currency') throw TypeError("currency must be a Currency");
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') throw TypeError("Amount must be a number");
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (typeof value !== 'Currency') throw TypeError("Currency must be a Currency");
    this._currency = value;
  }

  displayFullPrice() {
    format = `${this._amount} ${this._currency.name} (${this._currency.code})`;
    return format;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') throw TypeError("amount must be a number");
    if (typeof conversionRate !== 'number') throw TypeError("conversionRate must be a number");
    return amount * conversionRate
  }
}
