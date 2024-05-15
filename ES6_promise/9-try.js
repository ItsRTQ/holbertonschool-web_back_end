export default function guardrail(mathFunction) {
  const queue = [];
  const msg = 'Guardrail was processed';
  try {
    result = mathFunction();
    queue.push(result);
  } catch(err) {
    queue.push(String(err));
  } finally {
    queue.push(msg);
    return queue;
  }
}
