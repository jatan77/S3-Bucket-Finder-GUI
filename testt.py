cnt = 1

def dome():
      global cnt 
      cnt = cnt+1
      print(cnt)
      file = open('c.txt','w') 
      file.write(str(cnt)) 
      file.close() 
dome();
dome();
dome();
