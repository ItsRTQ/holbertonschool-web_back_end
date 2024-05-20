export default function getStudentsByLocation(objArray, city) {
  const desired = objArray
    .filter((student) => student.location === city);
  return desired;
}
