import numpy as np 

f = open("stapler_test_parts.g",'w')

# assume we start zero'd such that x0y0z0a0 is the bottom-leftmost viable position on the first layer

z_feedrate = 250

layer = -1

z_max = 20
z_min = 0
z_close_offset = 4 # relative to z_down
z_clear_offset = 8 # relative to z_down
wait_s = 0.75
bl_overshoot = 1.

x=0
y=0

def init():
	f.write("G21\n")

def placePart():
	global z_close,z_down,z_clear,wait_s
	f.write("G0Z%f\n" % (z_close))
	f.write("G1Z%fF%f\n" % (z_down,z_feedrate))
	f.write("M4\n")
	f.write("G4P%f\n" % wait_s)
	f.write("M5\n")
	f.write("G1Z%fF%f\n" % (z_down,z_feedrate))
	f.write("G0Z%f\n" % (z_clear))

def goToXY(part_pos):
	# always approach location from +x and +y
	global x,y
	overshoot = False
	last_x = x
	last_y = y
	x = part_pos[0]*1.27 + 18.23*((layer+1)%2)
	y = part_pos[1]*1.27 + 0.907*((layer+1)%2)

	if (last_x < x):
		# need to overshoot by a bit and then come back
		x_bl = x+bl_overshoot
		overshoot = True
	else:
		x_bl = x

	if (last_y < y):
		y_bl = y+bl_overshoot
		overshoot = True
	else:
		y_bl = y

	if (overshoot):
		f.write("G0X%fY%f (bl comp)\n" % (x_bl,y_bl))

	f.write("G0X%fY%f\n" % (x,y))

def indexStage():
	f.write("G0A%f\n" % (((layer+1)%2)*0.3125))

def newLayer():
	global layer,z_close,z_clear,z_close_offset,z_clear_offset,z_min,z_down

	f.write("(new layer)\n")

	layer += 1
	z_down = z_min+1.4*layer
	z_close = z_down+z_close_offset
	z_clear = z_down+z_clear_offset
	indexStage()

def finish():
	global z_max
	f.write("G0Z%f"%(z_max))
	goToXY([0,0])


init()

newLayer()

goToXY([0,0])
placePart()
goToXY([1,1])
placePart()
goToXY([0,2])
placePart()
goToXY([1,3])
placePart()

newLayer()

goToXY([0,0])
placePart()
goToXY([1,1])
placePart()
goToXY([0,2])
placePart()
goToXY([1,3])
placePart()

newLayer()

goToXY([0,0])
placePart()
goToXY([1,1])
placePart()
goToXY([0,2])
placePart()
goToXY([1,3])
placePart()

newLayer()

goToXY([0,0])
placePart()
goToXY([1,1])
placePart()
goToXY([0,2])
placePart()
goToXY([1,3])
placePart()

finish()

# newLayer()

# goToXY([0,0])
# placePart()
# goToXY([1,1])
# placePart()
# goToXY([0,2])
# placePart()
# goToXY([1,3])
# placePart()
# goToXY([-4,0])
# placePart()
# goToXY([-3,1])
# placePart()
# goToXY([-4,2])
# placePart()
# goToXY([-3,3])
# placePart()

# newLayer()

# goToXY([0,0])
# placePart()
# goToXY([1,1])
# placePart()
# goToXY([0,2])
# placePart()
# goToXY([1,3])
# placePart()
# goToXY([0,4])
# placePart()
# goToXY([1,5])
# placePart()
# goToXY([0,6])
# placePart()
# goToXY([1,7])
# placePart()

# goToXY([0,0])
# placePart()
# goToXY([1,1])
# placePart()
# goToXY([0,2])
# placePart()
# goToXY([1,3])
# placePart()

# newLayer()


f.close()
