# * 14IM10029 Utkarsh Sinha Assignment 4
# * Initial solution is made keeping in mind the bigram
# * Cost function by fitt's law
# * Innovation is switch between keys: 
# 1. Relative position b/w 2nd layer & 1st layer. 
# * Probability is taken from bigram frequency in'Wikipedia'(That is why answer slightly diff. from that in the paper)
# * The keys are defined in 3 classes : 1st,2nd,3rd layer of hexagon
# * 15 best probabilities taken into consideration

import math
bigram=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*6 # initiating a 0 matrix of 2D

#initial solution(Space occupies the centre): 
x=['t','h','e','r','i','n'] #6 elements the first layer in the hexagon and relative bigram freq. highest (their order is already optimized)
y=['q','w','y','u','o','p','a','s','d','g','j','k','l'] #12 elements the second layer in the hexagon
z=['v','f','z','x','c','v','m'] #8 elements and belongs to the outermost area of hexagon, practically no affect on efficiency

# filling up the top 15 bigram layer-wise relative frequencies(after 1st layer use):
bigram[6-1][7-1]=0.82
bigram[6-1][9-1]=0.63
bigram[1-1][7-1]=0.59
bigram[6-1][5-1]=0.57
bigram[2-1][7-1]=0.56
bigram[3-1][8-1]=0.56
bigram[1-1][8-1]=0.55
bigram[3-1][9-1]=0.55
bigram[1-1][5-1]=0.52
bigram[3-1][7-1]=0.47
bigram[5-1][8-1]=0.46
bigram[4-1][5-1]=0.43
bigram[6-1][10-1]=0.18
bigram[3-1][9-1]=0.09
bigram[3-1][8-1]=0.08                  # 5,7,8,9 have highest frequencies in 2nd layer

# e is the change in energy
def wprob(e):

	return math.exp(-e/2.)/math.sqrt(2*math.pi)  # a normal dist. function (similar to the function given in paper) 
# there can be 12 innovations in this model
imp=[5,7,8,9]          # 5,7,9 coincides with n=3,4,5 8 lies in b/w 4,5
for i in range(1,12):
		q=y
		q.append(q[0])
		q.pop(0)
		print q
		# calculating the change in energy, considering the bigram too.(Why? no. of iterations being somewhat less, 
																	   #we need to compensate by utilization of available data.)
		# assumptions: 1. e is proportional to 1/(d^2) 2. d is the no. of centres encountered
		tdin=1
		for j in range(0,12):
			din=0
			for k in range(0,6):
				if (bigram[k][j]!=0):
					if (j+1%2!=0):
						if ((j+1+1)/2==k+1):
							din=1
						elif (abs(((j+1+1)/2))-(k+1)==1):
							din=2
						elif (abs(((j+1+1)/2))-(k+1)==2):
							din=3
						elif (abs(((j+1+1)/2))-(k+1)==3):
							din=3
						tdin+=din
					elif (j+1%2==0):
						if ((j+1)/2==k+1 or ((j+1)/2)+1==k+1):
							din=1
						elif (abs(((j+1)/2)-(k+1)==1 or abs(((j+1)/2)+1-(k+1))==1 )):
							din=2
						elif (abs(((j+1)/2)-(k+1)==2 or abs(((j+1)/2)+1-(k+1))==2 )):
							din=3
						tdin+=din
		
		dubigram=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*6
		dubigram[0]=bigram[0]
		
		for l in (1,5):
			dubigram[l]=bigram[l]
			dubigram[l].append(dubigram[l][0])
			dubigram[l].pop(0)

		tdfin=1
		for j in range(0,12):
			dfin=0
			for k in range(0,6):
				if (bigram[k][j]!=0):
					if (j+1%2!=0):
						if ((j+1+1)/2==k+1):
							dfin=1
						elif (abs(((j+1+1)/2))-(k+1)==1):
							dfin=2
						elif (abs(((j+1+1)/2))-(k+1)==2):
							dfin=3
						elif (abs(((j+1+1)/2))-(k+1)==3):
							dfin=3
						tdfin+=dfin
					elif (j+1%2==0):
						if ((j+1)/2==k+1 or ((j+1)/2)+1==k+1):
							dfin=1
						elif (abs(((j+1)/2)-(k+1)==1 or abs(((j+1)/2)+1-(k+1))==1 )):
							dfin=2
						elif (abs(((j+1)/2)-(k+1)==2 or abs(((j+1)/2)+1-(k+1))==2 )):
							dfin=3
						tdfin+=dfin





		en2=(1/(tdfin**2))
		en1=(1/(tdin**2))
		aprob = min([1.,wprob(en2)/wprob(en1)]) #acceptance probability
		
		
			
		for k in range(0,6):
				u=sum(bigram[k])/15
		if u < aprob:
			y=q
			dubigram=bigram

print y

	# we can see that the 2nd layer is now optimized. the outputs represent how the keybad evolved over iterations.



