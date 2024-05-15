export default function guardrail(mathFunction) {
  const queue = [];
  const msg = 'Guardrail was processed';
  try {
    queue.push(mathFunction());
  } catch(err) {
    queue.push(String(err));
  } finally {
    queue.push(msg);
  }
  return queue;
}
