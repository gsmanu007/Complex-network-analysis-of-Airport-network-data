import sys
import random

from clustering import clustering


INF = 1000000

def dijkstra(adj_mat, source):
	
	nodes = len(adj_mat)
	dist = [INF for i in range(nodes)]
	visit = [0 for x in xrange(nodes)]

	dist[source] = 0

	while True:
		min_val = INF
		current = -1
		for i in range(nodes):
			if visit[i] == 0:
				if dist[i] < min_val:
					min_val = dist[i]
					current = i

		if current == -1: #All nodes have been visited
			return dist

		visit[current] = 1

		for n in range(nodes):
			if visit[n] == 0 and adj_mat[current][n] == 1:
				temp = dist[current] + 1
				if temp < dist[n]:
					dist[n] = temp



def main():
	n = 5	#Number of nodes
	e = 7	#Number of edges
	A = [[0 for x in xrange(n)] for x in xrange(n)]  #Adjacency Matrix 

	i = 1	#iterator

	while i <= e:
		a = random.randint(0,n-1)
		b = random.randint(0,n-1)

		if a!=b and A[a][b]!=1:
			A[a][b] = 1
			A[b][a] = 1
		else:
			i=i-1
		i+=1

	print A, "\n"

	total_cost = []
	for i in xrange(len(A)):
		start = i
		costs = dijkstra(A, start)
		print i, ":", costs, 
		total_cost.append(sum(costs))

	print "\nTotal cost:", total_cost, "\n"

	characterstic_pathlength = sum(total_cost)/float(n)

	print "Characterstic pathlength:", characterstic_pathlength, "\n"


	#Clustering Coefficient of the graph:
	clustering_coefficient=clustering(A)	
	print "Clustering coefficients are:", clustering_coefficient, "\n"


	#Average clustering coefficient of the graph
	aver_clustering=sum(clustering_coefficient)/n
	print "Average clustering coefficient of the network:", aver_clustering, "\n"


	return 2



if __name__ == "__main__":
	sys.exit(main())
