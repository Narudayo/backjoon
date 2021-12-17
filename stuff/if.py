value = input()
list = value.split();

h = int(list[0]);
m = int(list[1]);

mi = m-45

if mi<0 :
    mi +=60
    h -=1
    if h==-1 :
        h=23
        
# elif mi>0 :
#     mi -=60
#     h +=1
#     if h==24 :
#         h=0

print('%d %d'%(h,mi))
    
