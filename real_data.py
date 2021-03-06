import sys
import csv

from clustering import clustering
from my_implementation import dijkstra

def main(): 
	csvfile= open('airport_CnToCn_ajc.csv','rU')
	reader = csv.reader(csvfile,delimiter=",")
	allRows = list(reader)
	
	numData=[[allRows[j][i] for i in xrange(1, 228)] for j in xrange(1, 228)]
	#print numData

	n= len(numData)
	
	A=[[0 for x in xrange(n)] for x in xrange(n)] 
	
	
	for x in xrange(n):
		for y in xrange(n):
			if int(numData[x][y])>=1:
				A[x][y]=1
	
	
	total_cost = []
	for i in xrange(n):
		start = i
		costs = dijkstra(A, start)
		print "from", allRows[0][i+1], "costs are: ", costs, "\n"
		total_cost.append(sum(costs))

	#print "\nTotal cost:", total_cost, "\n"

	characterstic_pathlength = sum(total_cost)/float(n**2)
	print "Characterstic pathlength:", characterstic_pathlength, "\n"
	
	
	#Clustering Coefficient of the graph:
	clustering_coefficient=clustering(A)	
	for k in xrange(n):
		print "Clustering coefficients of", allRows[0][k+1], "is: ", clustering_coefficient[k], "\n"


	#Average clustering coefficient of the graph
	aver_clustering=sum(clustering_coefficient)/n
	print "Average clustering coefficient of the network:", aver_clustering, "\n"
	
	
	return 2





if __name__ == "__main__":
	sys.exit(main())
