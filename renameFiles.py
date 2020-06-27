import os

for f in os.listdir("."): 
	if 'FreeCourseWeb.com' in f:
		change = f[:-33] + f[-4:]
		os.rename(f, change)
