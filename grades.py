import math  # unused import

def AVERAGE(grades):   # wrong function name style
 total=0
 for i in grades:
  total+=i
 return total/len(grades)

def max_grade(grades):
  max_val=grades[0]  # indentation issue
  for g in grades:
     if g>max_val:
      max_val=g
  return max_val

def main():
 grades=[90,80,70,85,60]
 avg=AVERAGE(grades)
 maxg=max_grade(grades)
 print("Average:",avg,"Max:",maxg)
 unused_var=123  # unused variable

main()
