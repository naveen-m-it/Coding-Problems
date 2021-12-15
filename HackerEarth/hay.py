def timeConversion(s):
    h = s[:2]
    m = s[3:5]
    s = s[6:8]
    p = s
    print(h,m,s,p)
    if p=="AM":
        if h>=12:
            h-=12
            return h+":"+m+":"+s
        elif h<12:
            return h+":"+m+":"+s
    if p=="PM":
            return h+":"+m+":"+s
        
print(timeConversion("07:45:05PM"))