import imwatchingyou
import time

# imwatchingyou.show_debugger_window()    # Uncomment if you want to immediately display the debug window

counter = 0     # Some variable for you to watch / changing
# Using a loop in order to call the debugger refresh function on a periodic basis
while True:
    imwatchingyou.refresh_debugger()
    time.sleep(.1)          # Simulating doing a bunch of work
    # Using the counter to trigger the debug window display. You can use something else as your trigger. 
    if counter == 20:
        imwatchingyou.show_debugger_window()
    # do something with a variable that we can see/modify
    print(counter)
    counter += 1