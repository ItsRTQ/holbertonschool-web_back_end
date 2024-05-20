export default function getListStudentIds(objArray) {
  if (Array.isArray(objArray)) {
    return objArray.map(obj => obj.id);
  } else {
    return [];
  };
}
