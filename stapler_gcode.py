import numpy as np 

f = open("stapler_test1.g",'w')

# assume we start zero'd such that x0y0z0a0 is the bottom-leftmost viable position on the first layer

z_feedrate = 200

layer = -1

z_max = 30
z_min = 0
z_close_offset = 4.5 # relative to z_down
z_clear_offset = 8 # relative to z_down
wait_s = 0.75

def init():
	f.write("G21\n")

def placePart():
	global z_close,z_down,z_clear,wait_s
	f.write("G0Z%f\n" % (z_close))
	f.write("G1Z%fF%f\n" % (z_down,z_feedrate))
	# f.write("M4\n")
	# f.write("G4P%f\n" % wait_s)
	# f.write("M5\n")
	f.write("G1Z%fF%f\n" % (z_down,z_feedrate))
	f.write("G0Z%f\n" % (z_clear))

def goToXY(part_pos):
	x = part_pos[0]*1.27 + 18.23*((layer+1)%2)
	y = part_pos[1]*1.27 #+ 0.6*(layer%2)
	f.write("G0X%fY%f\n" % (x,y))

def indexStage():
	f.write("G0A%f\n" % (((layer+1)%2)*0.3125))

def newLayer():
	global layer,z_close,z_clear,z_close_offset,z_clear_offset,z_min,z_down

	f.write("(new layer)\n")

	layer += 1
	z_down = z_min+1.5*layer
	z_close = z_down+z_close_offset
	z_clear = z_down+z_clear_offset
	indexStage()


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
