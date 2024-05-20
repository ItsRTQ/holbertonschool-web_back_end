export default function getStudentsByLocation(objArray, city) {
  const desired = objArray
    .filter((student) => student.location === city)
    .map((student) => student.location);
  return desired;
}
