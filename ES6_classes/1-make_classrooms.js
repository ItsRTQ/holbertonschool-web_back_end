import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  /**
   * Creates function @see {initializeRooms}
   * Returns rooms array
   */
  const rooms = [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
  return rooms;
}
