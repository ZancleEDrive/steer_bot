# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import tkinter as Tkinter
from datetime import datetime
from PIL import ImageTk, Image
import rospy
from nav_msgs.msg import Odometry

node_name="chronometer"
gazebo_odometry_topic = '/steer_bot/ackermann_steering_controller/odom'
counter_reading=0
initial_x=0
initial_y=0


#value of target point to end chronometer and radius
target_x=20
target_y=20
radius=1

counter = 0
running = False




def is_inside(x ,y):
    return (x-target_x)**2 + (y-target_y)**2 < (radius)**2



def counter_label(label):
	def count():
		if running:
			global counter

			tt = datetime.fromtimestamp(counter)
			string = tt.strftime("%M:%S")
			display=string

			label['text']=display # Or label.config(text=display)

			# label.after(arg1, arg2) delays by
			# first argument given in milliseconds
			# and then calls the function given as second argument.
			# Generally like here we need to call the
			# function in which it is present repeatedly.
			# Delays by 1000ms=1 seconds and call count again.
			label.after(1000, count)
			counter += 1

	# Triggering the start of the counter.
	count()	

# start function of the stopwatch
def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Stop function of the stopwatch
def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Reset function of the stopwatch
def Reset(label):
	global counter
	counter=0

	# If rest is pressed after pressing stop.
	if running==False:	
		reset['state']='disabled'
		label['text']='00:00'

	# If reset is pressed while the stopwatch is running.
	else:			
		label['text']='00:00'

root = Tkinter.Tk()
root.title("Cronometro")
# Fixing the window size.
root.minsize(width=500, height=200)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("/home/tano/catkin_ws/src/steer_bot/steer_bot_gazebo/src/logo.png"))

# Create a Label Widget to display the text or Image
label = Tkinter.Label(root, image = img)
label.pack()
label = Tkinter.Label(root, text="00:00", fg="black", font="Verdana 50 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=10, height=2 ,command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=10, height=2, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=10, height=2, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=10)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")



def movement(data):
    global counter_reading
    global initial_x
    global initial_y
    print("Reading")
    if (counter_reading==0):
        print("Reading initial position")
        initial_x=data.pose.pose.position.x
        initial_y=data.pose.pose.position.y
        counter_reading+=1

    elif (abs(data.pose.pose.position.x - initial_x)>0.5 or abs(data.pose.pose.position.y - initial_y)>0.5) and counter_reading==1:
        Start(label)
        print("Chronometer Started")
        counter_reading+=1

    elif is_inside(data.pose.pose.position.x, data.pose.pose.position.y):
        Stop()
        print("Chronometer Stopped")

rospy.init_node(node_name, anonymous=True)
while not rospy.is_shutdown():
    rospy.Subscriber(gazebo_odometry_topic, Odometry, movement)
    root.mainloop()
