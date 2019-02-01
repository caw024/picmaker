import os

def writeto():
    if os.path.exists("image.ppm"):
        os.remove("image.ppm")
    f = open("image.ppm", "a")
    f.write("P3 ")
    f.write("500 500 ")
    f.write("255 ")
    out = ""
    for x in range(500):
        for y in range(500):
            out += str(x % 256) + " " + str((500-y) % 256) + " " + str(255) + " "
    f.write(out)
    print(out)
    f.close()

writeto()
        
