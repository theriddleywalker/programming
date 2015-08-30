#!/usr/bin/python

val=0
for x in range(-99999, -9999): #negative range
	tmp=str(x)[1:]
	for y in tmp:
		val+=int(y)
	
	val=val-(2*(int(tmp[0])))
	
	if pow(val,3) == x:
		print str(x)+': '+str(val)+' ^3: '+str(pow(val,3))
	val=0
	tmp=0

for x in range(10000, 100000): #positive range
	for y in str(x):
		val+=int(y)
	if pow(val,3) == x:
		print str(x)+': '+str(val)+' ^3: '+str(pow(val,3))
	val=0
	tmp=0
