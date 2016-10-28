import re

def match( pattern, line ):
    matchObjs = re.findall( pattern, line ) ;
    if len(matchObjs) > 0:
        print "\tMatched line - " + line,
        for match in matchObjs:
            if isinstance( match, str ):
                print "\t  match = " + match
            else:
                for i, group in enumerate( match ):
                    print "\t  Group " + str(i) + " = " + group 

pattern = raw_input( "> Enter regex pattern or [exit] : " )
while( pattern != 'exit' ):
    with open( "sentences.txt", 'r') as fp:
        for line in fp:
            match( pattern, line )
    pattern = raw_input( "> Enter regex pattern or [exit] : " )
