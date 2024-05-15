export default function divideFunction(numerator, denominator) {
    try {
        const result = numerator / denominator;
    } catch {
        throw TypeError('cannot divide by 0');
    } finally {
        return result;
    }
}
