#1 pass : to neglect expected indented block error 
for i in range(1,10):
    pass

#2 break : to stop the loop 
#for i in range (1,10):
 #   if(i == 3):
  ##      break
    #print(i)

#3 continue : to stop current iteration
#for i in range(1,10):
 #   if(i == 5):  # 5 remove hoto
  #      continue
   # print(i)     


#4 else : will execute when loop execute successfully
for i in range (1,10):
    if(i == 4):
        continue        # break : 3 yeun stop honr 
    print(i)
else:
   print('else executed')