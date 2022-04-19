from timetable import TimeTableGenerator
from timetable import Activity
from timetable import ClassRoom
from timetable import Group


def run():

    classRooms = [
        ClassRoom(0),
        ClassRoom(1),
        ClassRoom(2),
        ClassRoom(3),
        ClassRoom(4),
    ]

    groups = [
        Group(
            1,
            [
                Activity(1, "Maths 101", 5, 7, [0, 1]),
                Activity(1, "PHYS 101", 6, 7, [3, 5]),
                Activity(1, "COMP 103", 7, 9, [2, 6]),
            ],
        ),
        Group(
            2,
            [
                Activity(2, "COMP 204", 7, 9, [2]),
                Activity(2, "", 5, 7, [3, 6]),
                Activity(2, "", 6, 8, [4]),
                Activity(2, "", 9, 10, [1]),
                Activity(2, "EEEG 202", 11, 12, [5, 4]),
            ],
        ),
        Group(
            3,
            [
                Activity(3, "COMP 204", 6, 8, [0, 3]),
                Activity(3, "MCSC 201", 8, 9, [5, 6]),
                Activity(3, "MATH 208", 10, 12, [2, 4]),
                Activity(3, "COMP 202", 11, 12, [1]),
            ],
        ),
        Group(
            4,
            [
                Activity(4, "COMP 204", 5, 6, [3]),
                Activity(4, "COMP 231", 6, 8, [1]),
                Activity(4, "COMP 232", 10, 12, [5]),
            ],
        ),
        Group(
            5,
            [
                Activity(5, "MGTS 301", 8, 10, [6]),
                Activity(5, "COMP 307", 7, 8, [0]),
                Activity(5, "COMP 301", 9, 10, [2]),
            ],
        ),
        Group(
            6,
            [
                Activity(6, "COMP 314", 10, 12, [4]),
                Activity(6, "COMP 302", 7, 9, [5]),
                Activity(6, "COMP 304", 11, 12, [3]),
            ],
        ),
    ]

    t = TimeTableGenerator(classRooms, groups)

    table = []

    for i in range(0, 7):
        table.append([])

        for j, g in enumerate(classRooms):
            table[i].append([])

    for a in t.generate():
        day = a[0]
        classRoom = a[1].name
        table[day][classRoom] = a[2]

    weekDays = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]

    for row, days in enumerate(table):
        print(weekDays[row])
        for col, classRoom in enumerate(days):
            for activity in table[row][col]:
                print("Class No. " + str(col) + ": " + str(activity), end="\n")
        print("\n\n")


if __name__ == '__main__':
    run()


