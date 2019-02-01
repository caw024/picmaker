#!/usr/bin/env python

def writeto():
    f = open("image.ppm", "a")
    f.write("P3\n")
    f.write("5 5\n")
    f.write("255\n")
    for x in range(500):
        for y in range(500):
            f.write(str(x % 256) + " " + str(y % 256) + " " + str(255) + " " )
    f.close()

print( writeto() )
        
