


bigstr = "aaa((a1+30324872659126519 ))"
prevch = ""
arr = []
num = ""
for ch in bigstr:
  
  print "ch", prevch, ch, num
  if ch == " ":
    prevch = " "
    continue 
  #first digit  
  if ch.isdigit() :
    #append num
    num += ch
  
  # num completed
  else:
    if len(num) > 0:
      # print "addnum"
      arr.append(num) 
      num = ""
    arr.append(ch) 
     
  prevch = ch

    
  

print arr
  




