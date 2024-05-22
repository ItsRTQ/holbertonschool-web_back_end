export default function cleanSet(set, startString) {
  if (!set && !startString && !(set instanceof Set) && typeof startString !== 'string') {
    return '';
  }
  const arr = [];
  for (const value of set.values()) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      const valueSub = value.substring(startString.length);
      if (valueSub && valueSub !== value) {
        arr.push(valueSub);
      }
    }
  }
  return arr.join('-');
}
