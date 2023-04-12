from random import sample
from search import linear_search
from search import binary_search
import time

def run_lin(n):
   data=sample(range(1,n+1),n)
   start_time= time.time_ns()
   linear_search(data,data[-1])
   end_time=time.time_ns()
   time_taken=end_time- start_time
   return time_taken

def run_bin(data):
  
   start_time1=time.time_ns()
   binary_search(data,data[-1])
   end_time1=time.time_ns()
   time_taken1=end_time1- start_time1
   return time_taken1 
#a=[run_lin(1000000) for i in range (1,5)]
#b=max(a)
#print(b)
data = [x for x in range(100000000)]
c=[run_bin(data) for i in range (1,5)]
d=max(c)
print(d)
