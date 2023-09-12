def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4 and s[2] == 0

def successors(s):
    g8, g5, g3  = s #glass 8, 5, 3
    #space of glass 8, 5, 3
    s8 = 8 - g8
    s5 = 5 - g5
    s3 = 3 - g3
#move g8 to g5 
    if g8 > 0 :
        if s5 > 0:
            if g8 > s5:           
                yield ((g8 - s5, 5, g3), s5)
            else : #g8<s5
                yield (( 0, g8 + g5, g3), g8)
#g8 > g3
        if s3 > 0:
            if g8 > s3:
                yield ((g8 - s3, g5, 3), s3)
            else : #g8<s3
                yield ((0, g5, g3 + g8), g8)
#g5
    if g5 > 0 :
        if s8 > 0:
            if g5 > s8:    #g5>g8       
                yield ((8, g5 - s8 , g3), s8)
            else : #g5<s8
                yield (( g8 + g5, 0, g3), g5)
#g5 > g3
        if s3 > 0:
            if g5 > s3:
                yield ((g8, g5-s3, 3), s3)
            else : #g5<s3
                yield ((g8, 0, g5 + g3), g5)
#g3 
    if g3 > 0 :
        if s8 > 0:
            if g3 > s8:
                yield ((8, g5, g3 - s8), s8)
            else: #g3<s8
                yield ((g8 + g3, g5, 0), g3)

#g3 > g5
        if s5 > 0:
            if g3 > s5:
                yield ((g8, 5, g3 - s5), s5)
            else: #g3 < s5
                yield ((g8, g5 + g3, 0), g3)
