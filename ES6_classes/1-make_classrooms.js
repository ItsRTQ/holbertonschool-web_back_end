import ClassRoom from "./0-classroom.js";

export default function initializeRooms() {
  /**
   * Creates function @see {initializeRooms}
   * Returns rooms array
   */
  const rooms = [ClassRoom(19), ClassRoom(20), ClassRoom(34)];
  return rooms;
}
