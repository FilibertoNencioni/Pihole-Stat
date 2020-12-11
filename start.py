import time
import subprocess
from sys import stdout
import curses

x = 0
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def stampa(res, MLine):
        stdscr.addstr(0, 0, "CPU USAGE: {0}".format(res))
        stdscr.addstr(1, 0, "USED STORAGE: {0}".format(MLine))
        stdscr.refresh()
while x != 5:
        #CPU USAGE CALCULATION BY MPSTAT
        #first of all you need to install mpstat on your pi by the command: sudo apt-get install mpstat
        cpuusage = str(subprocess.run('mpstat',capture_output=True))
        CLine = int(cpuusage[-21:-19])
        res = 100-CLine

        #STOREGE USE CALCUTATION
        memuse = str(subprocess.run('df',capture_output=True))
        MLine = memuse[155:158]
        stampa(res, MLine)

        time.sleep(1)