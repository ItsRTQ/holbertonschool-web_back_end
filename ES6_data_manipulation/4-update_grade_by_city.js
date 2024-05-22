export default function updateStudentGradeByCity(studentsArr, city, newGrades) {
  const desiredStudents = studentsArr.filter((student) => student.location === city);
  const toChangeStudent = desiredStudents.map((student) => {
    for (const studInfo of newGrades) {
      if (student.id === studInfo.studentId) {
        student.grade = studInfo.grade; // eslint-disable-line no-param-reassign
      }
    }
    if (student.grade === undefined) {
      student.grade = 'N/A'; // eslint-disable-line no-param-reassign
    }
    return student;
  });
  return toChangeStudent;
}
