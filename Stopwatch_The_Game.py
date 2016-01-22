try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
n = 0
min = 0
sec = 0
tenth_sec = 0

is_running = False

count_stop = 0
count_success_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    global sec
    global tenth_sec
    global min
    #global is_running
    
    sec = int (t / 10)
    tenth_sec = t % 10
    min = int (t / 600)
    
    #return sec
    if sec < 10:
        return str(min) + ":0" + str(sec) + ":" + str(tenth_sec)
    elif sec >= 10 and sec <= 59:
        return str(min) + "0:" + str(sec) + ":" + str(tenth_sec)
    elif sec >= 60:
        sec = sec % 60
        if sec >=10:
            return str(min) + ":" + str(sec) + ":" + str(tenth_sec)
        else:
            return str(min) + ":" + "0" + str(sec) + ":" + str(tenth_sec)
    
    #is_running = True

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global count_start
    global is_running
    global check
    timer.start()
    is_running = True
    check = True

def button_stop():
    global count_stop
    global count_success_stop
    if timer.is_running():
        count_stop += 1
        if tenth_sec == 0:
            count_success_stop += 1
    timer.stop()
    
def button_reset():
    global n
    global count_stop
    global count_success_stop
    n = 0
    count_stop = 0
    count_success_stop = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global n
    n = n + 1
    #print n

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(n),[120,150],30,"Black")
    canvas.draw_text(str(count_stop),[230,40],20,"Green")
    canvas.draw_text("/",[250,40],20,"Green")
    canvas.draw_text(str(count_success_stop),[265,40],20,"Green")
    
# create frame


# register event handlers
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.add_button("Start",button_start)
frame.add_button("Stop",button_stop)
frame.add_button("Reset",button_reset)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
frame.set_draw_handler(draw_handler)
