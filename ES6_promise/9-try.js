export default function guardrail(mathFunction) {
  const data = [];
  const msg = 'Guardrail was processed';
  try {
    result = mathFunction;
    data.push(result);
    data.push(msg);
  } catch(err) {
    data.push(err);
    data.push(msg);
  } finally {
    return data;
  }
}
