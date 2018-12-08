#!/usr/bin/env python
import numpy as np
import rospy as rp
from sys import maxsize as infinity
from geometry_msgs.msg import Transform
from agv_as18.srv import Path, PathResponse, PathRequest

robot = [0.0,0.0]

# locations
BEAST = ['BEAST', 0.0, 0.0]
AS = ['AS', 125.0,66.0]
C1 = ['C1',200.0,210.0]
C2 = ['C2', 170.0,210.0]
C3 = ['C3', 140.0,210.0]
C4 = ['C4', 110.0,210.0]
C5 = ['C5', 80.0,210.0]
C6 = ['C6', 50.0,210.0]
MWP1 = ['MWP1', 222.5,166.0]
MWP2 = ['MWP2', 125.0,166.0]
MWP3 = ['MWP3', 27.7,166.0]

# distances
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

def find_component(component):
  """Returns the name and the x, y position of the component of interest"""
  if component == 'C1':
      return C1
  elif component == 'C2':
      return C2
  elif component == 'C3':
      return C3
  elif component == 'C4':
      return C4
  elif component == 'C5':
      return C5
  elif component == 'C6':
      return C6
  elif component == 'AS':
      return AS

#dijkstra algorithm
def dijkstra(graph,start,goal):
    """Based on a graph and a starting node, it finds the minimum distances to every other node and returns the path to the goal node"""
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
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
  global robot
  robot[0]=data.translation.x
  robot[1]=data.translation.y

def server_cb(req):
    BEAST = ['BEAST', robot[0], robot[1]]
    path=[] # list that will contain all the waypoints

    # apply dijkstras algorithm for every task in the task sequence list
    for task in req.task_seq:
        if BEAST[2] < 166:
            graph = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
                    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
                    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
                    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
                    BEAST[0]:{AS[0]:np.sqrt((BEAST[1]-AS[1])**2+(BEAST[2]-AS[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
                    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}
        else:
            graph = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
                    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
                    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
                    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
                    BEAST[0]:{C1[0]:np.sqrt((BEAST[1]-C1[1])**2+(BEAST[2]-C1[2])**2),C2[0]:np.sqrt((BEAST[1]-C2[1])**2+(BEAST[2]-C2[2])**2),C3[0]:np.sqrt((BEAST[1]-C3[1])**2+(BEAST[2]-C3[2])**2),
                    C4[0]:np.sqrt((BEAST[1]-C4[1])**2+(BEAST[2]-C4[2])**2),C5[0]:np.sqrt((BEAST[1]-C5[1])**2+(BEAST[2]-C5[2])**2),C6[0]:np.sqrt((BEAST[1]-C6[1])**2+(BEAST[2]-C6[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
                    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}

        c = dijkstra(graph,BEAST[0],task) # stores a list of the path the robot needs to take in order to complete a task

        # appends the path waypoints in a list
        for i in range(1,len(c)):
            path.append(c[i])
        
        # update the position of the robot for the next iteration (needed for the new graph)
        BEAST[1] = find_component(task)[1]
        BEAST[2] = find_component(task)[2]

    return PathResponse(path)

rp.init_node('waypoint_optimization')
rp.Subscriber('local_pos_ref', Transform, pos_cb)
s = rp.Service('path_service', Path, server_cb)
rp.spin()