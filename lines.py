import sys

n = 0
try:
    if len (sys.argv)==1:
        print ("To few command lines")
    elif len(sys.argv)>2:
        print ("To much command lines")
    else:
       with open(sys.argv[1]) as file:
            for line in file:
                if line.strip()=="":
                    pass
                elif line.strip()[0] != "#":
                    n += 1
        
    print("Total line is", n)
except FileNotFoundError:
    sys.exit("File not exist")  
