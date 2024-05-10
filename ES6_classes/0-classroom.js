export default class ClassRoom {
    /**
    * Creates a new ClassRoom instance.
    * @param {number} maxStudentsSize - The maximum number of students that can be accommodated in the classroom.
    */
    constructor(maxStudentsSize) {
        this._maxStudentsSize = Number(maxStudentsSize);
    }
}