import numpy
import math
import operator
import random
import scipy.cluster.vq
import sys

def cluster(samples): 

  print "BEGINNING CLUSTER CALC"

  num_samples=len(samples)

	# initialization
  center1 = samples[random.randrange(0,num_samples, 1)]
  center2 = samples[random.randrange(0,num_samples, 1)]


  new_1=0
  new_2=0
  

  while True :
    num_1 = 0
    num_2 = 0 

    center_assignments=[]
    for x in xrange (len(num_samples)):
      sample=samples[x]
      for y in xrange (len(sample)):
        center1_diff += (sample[y]-center1[y])**2
        center2_diff += (sample[y]-center2[y])**2
      min_diff = min(center1_diff,center2_diff)
      if min_diff==center1_diff:
        center_assignments.append(center1)
      else : 
        center_assignments.append(center2)

    cluster_1_vals=[]
    cluster_2_vals =[]

    for x in xrange (len(center_assignments)):
      if (center_assignments[x] == center1):
        new_1 += samples[x]
        num_1+=1
      else : 
        new_2 += samples[x]
        num_2+=1

    for x in xrange (len(samples[0])):
      new_1[x] = new_1[x]/num_1
      new_2[x]= new_2[x]/num_2

    if new_1== center1 and new_2==center2:
      break
    else : 
      center1=new_1
      center2=new_2
  
  print "DONE CLUSTER CALC"
  
  print "Center 1:"
  print center1
  print " Center 2:"
  print center2


def main ():
    samples = open("chatous_file", "r")
    cluster(samples)

if __name__ == '__main__':
   main(sys.argv)




    
