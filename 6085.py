w, h, b = map(int, input().split( ))
if(b<=40 and b%4==0):
    print("%.2f" %(round(float(w*h*b/8/1024/1024), 2)) + " MB")