import sys

sideLength = int(raw_input( 'Please enter side length of rhombus : ' ))
lines = []
bottomLines = []

for i in range( sideLength ):
    line = []
    arr = [ ' ' ]*sideLength

    arr[sideLength-i-1] = '*'
    line += arr
    arr.reverse()
    line += arr[1:] 
    
    lines.append( line )
    bottomLines.insert( 0, line[:] )

lines += bottomLines[1:]

print
for line in lines:
    for char in line:
        sys.stdout.write( char )
    print
