import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import requests
from bs4 import BeautifulSoup
import random
 
 
network=nx.Graph()
#network.add_edge(a,b)

reqs=requests.get('https://www.python.org//')
soup=BeautifulSoup(reqs.text, 'html.parser')

def add(x):
    req=requests.get(x)
    soupp=BeautifulSoup(req.text, 'html.parser')
    for link in soupp.find_all('a'):
        aa=link.get('href')
        if(aa):
            if(aa.startswith('https')):
                #print(aa)
                network.add_edge(x,aa)
 
  
for link in soup.find_all('a'):
    a=link.get('href')
    if(a.startswith('https')):
        #print(a)
        network.add_edge(reqs,a)
        add(a)
            


#generator zwracający listę o rozmiarze równym liczbie wierzchołków grafu zawierającą info o liczbie ich odwiedzin 
#neigbours
def randomWalk(gr):
    k=[]
    s=[]
    n=len(gr)
    grr=random.choice(list(gr.nodes))
    for i in range (len(gr)):
        a=random.choice(list(gr.neighbors(grr)))
        if a in k:
            s[k.index(a)]+=1
        else:
            k.append(a)
            s.append(1)
        yield s

def animate(ns, graph, fun):
 N=nx.number_of_nodes(graph)
 pos=nx.fruchterman_reingold_layout(graph)
 nodes=nx.draw_networkx_nodes(graph, pos, node_size=ns, node_color=np.fromiter((1/el for el in range(1,N+1)), float))
 nx.draw_networkx_edges(graph, pos,)

 def _animate(ns,gr):
  nodes.set_array(np.array([el/256 for el in ns]))
  nodes.set_sizes(np.array([el for el in ns]))
  return nodes

 fig = plt.gcf()
 #robi animacje-na czym ustawiamy rozmiar i kolor
 anim = FuncAnimation(fig, func=_animate, frames=fun, fargs=(graph,), interval=10, repeat=False)
 plt.show()

#N=rozmiar_utworzonego_grafu
N=len(network)
node_size=[10 for _ in range(N)],
animate(node_size, network, randomWalk(network))

#zadanie drugie
def bubble_sort(tab):
    change=1
    while change:
        change=0
        for i in range(len(tab)-1):
            if tab[i]>tab[i+1]:
                tmp=tab[i]
                tab[i]=tab[i+1]
                tab[i+1]=tmp
                change=1
        yield tab

a=bubble_sort([4,6,5,1,2,2,90])
for i in a:
    print(i)
def mergeSort(arr, start, end):
    if end <= start:
        return
    mid = start + ((end-start+1)//2)
    yield from mergeSort(arr, start, mid-1)
    yield from mergeSort(arr, mid, end)
    yield from merge(arr, start, mid-1, end)


def merge(arr, start, mid, end):
    result = []
    left_index = start
    right_index = mid + 1
    while left_index <= mid and right_index <= end:
        if arr[left_index] < arr[right_index]:
            result.append(arr[left_index])
            left_index+=1
        else:
            result.append(arr[right_index])
            right_index+=1
   
    while left_index <= mid:
        result.append(arr[left_index])
        left_index+=1
   
    while right_index <= end:
        result.append(arr[right_index])
        right_index+=1
   
    for index, value in enumerate(result):
        arr[start+index] = value
        yield arr

a=mergeSort([4,6,5,1,2,2,90],1,6)
for i in a:
    print(i) 


