export default function getStudentIdsSum(objArray) {
  return objArray.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
}
