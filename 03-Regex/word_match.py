import re

def match( pattern, word ):
    matchObj = re.match( pattern, word ) ;
    if matchObj:
        print "\tMatched word - " + matchObj.group(0)
        for i, group in enumerate( matchObj.groups() ):
            print "\t  Group " + str(i) + " = " + group 


pattern = raw_input( "> Enter regex pattern or [exit] : " )
while( pattern != 'exit' ):
    with open( "small_wordlist.txt", 'r') as fp:
        for word in fp:
            match( pattern, word )
    pattern = raw_input( "> Enter regex pattern or [exit] : " )
