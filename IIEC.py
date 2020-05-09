import curses
import time



def print_menu(stdscr, selected_row_idx,given_menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(given_menu):
        x = w//2 - len(row)//2
        y = h//2 - len(given_menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def menu_box(stdscr,menu_get):
    # turn off cursor blinking
    curses.curs_set(0)
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # specify the current selected row
    menu=menu_get
    current_row = 0
    # print the menu
    print_menu(stdscr, current_row, menu)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return(current_row)
            # if user selected last row, exit the program

        print_menu(stdscr, current_row ,menu)




def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #starting
    print_center(stdscr,"Welcome To My TUI")
    time.sleep(3)

    #asking for remote or local
    print_center(stdscr,"Where do you want te perform operations...??")
    time.sleep(2)
    menu_pass=['LOCALLY', 'REMOTELY']
    y=menu_box(stdscr, menu_pass)
    if(y==0):
        print_center(stdscr,"Please make a choice to proceed further...")
        time.sleep(3)
        menu_pass=['BASIC_OPERATIONS','PAKAGE_MANAGENMENT','DISC_MANAGENMENT','NETWORKING','WEBSERVER_MANAGENMENT','FILE_TRANSFER']
        x=menu_box(stdscr,menu_pass)
        if(x==0):
            print_center(stdscr,"Basic Operations")
            time.sleep(2)
        elif(x==1):
            print_center(stdscr, "Pakage Managenment")
            time.sleep(2)
        elif(x==2):
            print_center(stdscr, "Disc Managenment")
            time.sleep(2)
        elif(x==3):
            print_center(stdscr, "Networking")
            time.sleep(2)
        elif(x==4):
            print_center(stdscr, "Webserver Managenment")
            time.sleep(2)
        else:
            print_center(stdscr, "File Transfer")
            time.sleep(2)

    else:
        print_center(stdscr,"You selected remotely")
        time.sleep(3)
curses.wrapper(main)