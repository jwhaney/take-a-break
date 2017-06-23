# this program, once started, will open the default web browser or a new tab in the default browser,
# and play a funny .gif that tells you to take a break!
# the break can occur at whatever increment you want. below it is set to 2 hours (7200 seconds) and will
# run a maximum of 3 times throughout the day.

# author: john haney

import time, webbrowser

break_count = 0

print("Program started at: " + time.ctime())
while(break_count < 3):
    time.sleep(7200)
    webbrowser.open("http://media.riffsy.com/images/b35382f7ba569d6c6b3620889207c1cf/tenor.gif")
    break_count = break_count + 1

print("Program completed at: " + time.ctime())
