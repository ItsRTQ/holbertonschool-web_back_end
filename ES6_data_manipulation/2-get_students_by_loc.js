export default function getStudentsByLocation(objArray, targeted) {
  const desired = objArray
    .filter((student) => student.location === targeted)
    .map((student) => student.location);
  return desired;
}
