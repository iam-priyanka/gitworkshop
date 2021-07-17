# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:21:53 2020

@author: PRIYANKA
"""
size=int(input("HT Size:"))
ht=[None]*size
def hashCode(x):
    return (x%size)
def insert(x):
    hc=hashCode(x)
    if ht[hc]==None:
        ht[hc]=x
        print("Inseted at:",hc)
    else:
        t=(hc+1)%size
        while(ht[t]!=None) and t!=hc:
            t=(t+1)%size
        if(ht[t]==None):
            ht[t]=x
            print("Inseted at:",t)
        else:
           print("HT is full!")

def search(a):
     hc = hashCode(a)
     if ht[hc] == a:
         return hc
     elif ht[hc] is None:
         return -1
     else:
         t = (hc + 1) % size
         while ht[t] is not None and ht[t] != a and t != hc:
             t = (t + 1) % size
         if ht[t] == a:
             return t
     return -1
def delete(b):
    t = search(b)
    pos = t
    if t == -1:
        print("element not found")
    else:
        ht[t] = None
        print(b, "is deleted from position", pos + 1)
         
def display():
    for i in range(size):
        print(i,end="\t")
    print()
    for i in ht:
        print(i,end="\t")
    print()
   
while (1):
  print("1. Insert")
  print("2. Search")
  print("3. Delete")
  print("4. Display")
  ch = int(input("Your Choice: "))
  if ch==1:
    insert(int(input("Enter number:")))
  elif ch==2:
    f=search(int(input("Enter number:")))
    if(f != -1):
      print("Found at: ", f)
    else:
      print("Not Found")
  elif ch==3:
    delete(int(input("Enter number:")))
  elif ch==4:
    display()
  else:
    break
