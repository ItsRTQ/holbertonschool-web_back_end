export default function updateUniqueItems(weeeGona) {
  if (!(weeeGona instanceof Map)) {
    throw new Error('Cannot process');
  }
  weeeGona.forEach((value, key) => {
    if (value === 1) {
      weeeGona.set(key, 100);
    }
  });
}
