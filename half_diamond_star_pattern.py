def half_diamond_star_pattern(n):
    for i in range(n):
        print("*"*(i+1))
    for i in range(n-1,0,-1):
        print("*"*(i))
