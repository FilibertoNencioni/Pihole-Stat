import time
import subprocess
from sys import stdout
import curses
import psutil #need to "pip install psutil" or "pip3 install psutil"

x = 0
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def stampa(res, MLine, RLine):
        stdscr.addstr(0, 0, "CPU USAGE: {0}%".format(res))
        stdscr.addstr(1, 0, "USED STORAGE: {0}".format(MLine))
        stdscr.addstr(2, 0, "RAM USAGE: {0}%".format(RLine))
        stdscr.refresh()

while x != 5:
        #CPU USAGE CALCULATION BY MPSTAT
        #You need to install mpstat on your pi by the command: sudo apt-get install mpstat
        cpuusage = str(subprocess.run('mpstat',capture_output=True))
        CLine = int(cpuusage[-21:-19])
        res = 100-CLine

        #STOREGE USE CALCUTATION
        memuse = str(subprocess.run('df',capture_output=True))
        MLine = memuse[155:158]

        #RAM USAGE CALCULATION
        RLine = str(psutil.virtual_memory().percent)

        stampa(res, MLine, RLine)
        time.sleep(1)