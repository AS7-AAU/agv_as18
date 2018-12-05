#!/usr/bin/env python
import numpy as np
#import pandas as pd
import sys
import rospy as rp
from geometry_msgs.msg import Transform
from agv_as18.msg import Waypoints, Task

#locations
BEAST = ['BEAST',70.0,220.0]
AS = ['AS',170.0,125.0]
C1 = ['C1',5.0,200.0]
C2 = ['C2',5.0,170.0]
C3 = ['C3',5.0,140.0]
C4 = ['C4',5.0,110.0]
C5 = ['C5',5.0,80.0]
C6 = ['C6',5.0,50.0]
MWP1 = ['MWP1',52.5,222.5]
MWP2 = ['MWP2',52.5,125.0]
MWP3 = ['MWP3',52.5,27.7]

#distances
AS_MWP1 = np.sqrt((AS[1]-MWP1[1])**2 + (AS[2]-MWP1[2])**2)
AS_MWP2 = np.sqrt((AS[1]-MWP2[1])**2 + (AS[2]-MWP2[2])**2)
AS_MWP3 = np.sqrt((AS[1]-MWP3[1])**2 + (AS[2]-MWP3[2])**2)
C1_MWP1 = np.sqrt((C1[1]-MWP1[1])**2 + (C1[2]-MWP1[2])**2)
C1_MWP2 = np.sqrt((C1[1]-MWP2[1])**2 + (C1[2]-MWP2[2])**2)
C1_MWP3 = np.sqrt((C1[1]-MWP3[1])**2 + (C1[2]-MWP3[2])**2)
C2_MWP1 = np.sqrt((C2[1]-MWP1[1])**2 + (C2[2]-MWP1[2])**2)
C2_MWP2 = np.sqrt((C2[1]-MWP2[1])**2 + (C2[2]-MWP2[2])**2)
C2_MWP3 = np.sqrt((C2[1]-MWP3[1])**2 + (C2[2]-MWP3[2])**2)
C3_MWP1 = np.sqrt((C3[1]-MWP1[1])**2 + (C3[2]-MWP1[2])**2)
C3_MWP2 = np.sqrt((C3[1]-MWP2[1])**2 + (C3[2]-MWP2[2])**2)
C3_MWP3 = np.sqrt((C3[1]-MWP3[1])**2 + (C3[2]-MWP3[2])**2)
C4_MWP1 = np.sqrt((C4[1]-MWP1[1])**2 + (C4[2]-MWP1[2])**2)
C4_MWP2 = np.sqrt((C4[1]-MWP2[1])**2 + (C4[2]-MWP2[2])**2)
C4_MWP3 = np.sqrt((C4[1]-MWP3[1])**2 + (C4[2]-MWP3[2])**2)
C5_MWP1 = np.sqrt((C5[1]-MWP1[1])**2 + (C5[2]-MWP1[2])**2)
C5_MWP2 = np.sqrt((C5[1]-MWP2[1])**2 + (C5[2]-MWP2[2])**2)
C5_MWP3 = np.sqrt((C5[1]-MWP3[1])**2 + (C5[2]-MWP3[2])**2)
C6_MWP1 = np.sqrt((C6[1]-MWP1[1])**2 + (C6[2]-MWP1[2])**2)
C6_MWP2 = np.sqrt((C6[1]-MWP2[1])**2 + (C6[2]-MWP2[2])**2)
C6_MWP3 = np.sqrt((C6[1]-MWP3[1])**2 + (C6[2]-MWP3[2])**2)
C1_C2 = np.sqrt((C1[1]-C2[1])**2 + (C1[2]-C2[2])**2)
C1_C3 = np.sqrt((C1[1]-C3[1])**2 + (C1[2]-C3[2])**2)
C1_C4 = np.sqrt((C1[1]-C4[1])**2 + (C1[2]-C4[2])**2)
C1_C5 = np.sqrt((C1[1]-C5[1])**2 + (C1[2]-C5[2])**2)
C1_C6 = np.sqrt((C1[1]-C6[1])**2 + (C1[2]-C6[2])**2)
C2_C3 = np.sqrt((C2[1]-C3[1])**2 + (C2[2]-C3[2])**2)
C2_C4 = np.sqrt((C2[1]-C4[1])**2 + (C2[2]-C4[2])**2)
C2_C5 = np.sqrt((C2[1]-C5[1])**2 + (C2[2]-C5[2])**2)
C2_C6 = np.sqrt((C2[1]-C6[1])**2 + (C2[2]-C6[2])**2)
C3_C4 = np.sqrt((C3[1]-C4[1])**2 + (C3[2]-C4[2])**2)
C3_C5 = np.sqrt((C3[1]-C5[1])**2 + (C3[2]-C5[2])**2)
C3_C6 = np.sqrt((C3[1]-C6[1])**2 + (C3[2]-C6[2])**2)
C4_C5 = np.sqrt((C4[1]-C5[1])**2 + (C4[2]-C5[2])**2)
C4_C6 = np.sqrt((C4[1]-C6[1])**2 + (C4[2]-C6[2])**2)
C5_C6 = np.sqrt((C5[1]-C6[1])**2 + (C5[2]-C6[2])**2)

# directed graph when the robot is in the right side of the map
graph_right = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
    BEAST[0]:{AS[0]:np.sqrt((BEAST[1]-AS[1])**2+(BEAST[2]-AS[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}

# directed graph when the robot is in the left side of the map
graph_left = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
    BEAST[0]:{C1[0]:np.sqrt((BEAST[1]-C1[1])**2+(BEAST[2]-C1[2])**2),C2[0]:np.sqrt((BEAST[1]-C2[1])**2+(BEAST[2]-C2[2])**2),C3[0]:np.sqrt((BEAST[1]-C3[1])**2+(BEAST[2]-C3[2])**2),
    C4[0]:np.sqrt((BEAST[1]-C4[1])**2+(BEAST[2]-C4[2])**2),C5[0]:np.sqrt((BEAST[1]-C5[1])**2+(BEAST[2]-C5[2])**2),C6[0]:np.sqrt((BEAST[1]-C6[1])**2+(BEAST[2]-C6[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}

# Product components with their locations
P1 = [C1,C3,C4,C4]
P2 = [C1,C2,C5,C6]
P3 = [C3,C3,C5]
P4 = [C2,C3,C4]    

# Product components, only the names
P_1 = [P1[0][0],P1[1][0],P1[2][0],P1[3][0]]
P_2 = [P2[0][0],P2[1][0],P2[2][0],P2[3][0]]
P_3 = [P3[0][0],P3[1][0],P3[2][0]]
P_4 = [P4[0][0],P4[1][0],P4[2][0]]

# Products for which we need to bring components in order to start assembling
'''
ProductList=[]
df = pd.read_csv('agv_assembly_order_train.csv')
for element in df.values:
    if element[0] == 1:
        ProductList.append(P1)
    elif element[0] == 2:
        ProductList.append(P2)
    elif element[0] == 3:
        ProductList.append(P3)
    elif element[0] == 4:
        ProductList.append(P4)
'''
ProductList = [P1,P3,P2]

#dijkstra algorithm
def dijkstra(graph,start,goal):
    """Based on a graph and a starting node, it finds the minimum distances to every other node and returns the path to the goal node"""
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = sys.maxsize
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        return path

def pos_cb(data):
  global BEAST
  BEAST[1]=data.translation.x
  BEAST[2]=data.translation.y

def new_b_cb(data):
    print('callback')
    b=[]
    task_sequence = data.task_seq
    for i in range(len(task_sequence)):

        if BEAST[1] > 52.5:
            graph = dict(graph_right)
        else:
            graph = dict(graph_left)

        c = dijkstra(graph,BEAST[0],task_sequence[i][0])

        for j in range(1,len(c)):
            b.append(c[j])
        BEAST[1] = task_sequence[i][1] 
        BEAST[2] = task_sequence[i][2]

    msg = Waypoints()
    for el in b:
        msg.b.append(el)
    for el in task_sequence:
        task = Task()
        task.name = el[0]
        task.x = el[1]
        task.y = el[2]
        msg.task_seq.append(task)
    waypoint_pub.publish(msg)



rp.init_node('waypoint_optimization')
rp.Subscriber('local_pos_ref', Transform, pos_cb)
rp.Subscriber('update_b', Waypoints, new_b_cb)
waypoint_pub = rp.Publisher('waypoints', Waypoints, queue_size=1)
rp.spin()









# Create a list of lists containing the name and location of each destination the robot needs to go in order to take all the components needed and deliver them to the assembly
task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
print(task_sequence)
i = 2
while i < len(task_sequence):
    task_sequence.insert(i, AS)
    i += 3
task_sequence.append(AS)



# Initialize a list that will contain all the waypoints
b=[]

# apply dijkstras algorithm for every task in the task sequence list
for i in range(len(task_sequence)):

    if BEAST[1] > 52.5:
        graph = dict(graph_right)
    else:
        graph = dict(graph_left)

    # stores a list of the path the robot needs to take in order to complete a task
    c = dijkstra(graph,BEAST[0],task_sequence[i][0])

    # Appends the path waypoints in a list
    for j in range(1,len(c)):
        b.append(c[j])

    #Update the position of the robot    
    BEAST[1] = task_sequence[i][1]
    BEAST[2] = task_sequence[i][2] 

print(b)


msg = Waypoints()
for el in b:
    msg.b.append(el)
for el in task_sequence:
    task = Task()
    task.name = el[0]
    task.x = el[1]
    task.y = el[2]
    msg.task_seq.append(task)
waypoint_pub.publish(msg)