def left_pyramid_star_pattern(n):
    for i in range((n),0,-1):
        print(" "*i,"*"*(n+1-i))
