class Main

def main()
    while
        screen.display("Add students & courses ?")
        screen.addoptparse(1, "Go")
        screen.addoptparse(2, "Decline")

        if option1 == 1 
            screen.clear()
            NoS = int(number_of_student())
            screen.clear()
            for i in range(NoS)
            screen.addstr("Student ID: " + get("a1"), "Student name: " + get("a2"), "Student DOB: " + get("a3"))
            add_student()
            screen_clear()
            screen_refresh()
    
            screen.clear()
            NoC = int(number_of_courses())
            screen.clear()
            for i in range(NoC)
            screen.addstr("Course ID: " + get("b1"), "Course name: " + get("b2"))
            add_course()
            screen_clear()
            screen_refresh()

        break 
        else
            screen.dislay("Exit program?")
            screen.addoptparse(1, "Exit")
            screen.addoptparse(2, "Decline")
                if option2 == 1
                    exit()
                else option2 == 2
                    return main()
    screen.clear()
    screen.refresh()
    while 
        screen.display("Calculate GPA?")
        screen.addoptparse(1, "Go")
        screen.addoptparse(2, "Decline")

        if option3 == 2
            screen.dislay("Exit program?")
            screen.addoptparse(1, "Exit")
            screen.addoptparse(2, "Decline")
                if option2 == 1
                    exit()
                else option2 == 2
                    return main()
        else 
            screen.addstr("GPA list: ")
            option3 = int(screen.getstr().decode())
            screen_refresh()
            screen_clear()
    break   

