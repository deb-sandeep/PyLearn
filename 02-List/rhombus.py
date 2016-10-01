import sys

sideLength = int(raw_input( 'Please enter side length of rhombus : ' )) #number of rows of rhombus triangle
lines = [] #for upper triangle 
bottomLines = [] #for lower triangle

for i in range( sideLength ):
    line = []
    arr = [ ' ' ]*sideLength #arr will have sidelength number of spaces

    arr[sideLength-i-1] = '*' #2n-1 stars for inner and outer respectively
    line += arr #print line of stars since rhombus is symmetric about all axes
    arr.reverse() #lower triangle
    line += arr[1:] #exclude character 1 
    
    lines.append( line ) #drawing line of stars
    bottomLines.insert( 0, line[:] )

lines += bottomLines[1:]

print
for line in lines:
    for char in line:
        sys.stdout.write( char )
    print
