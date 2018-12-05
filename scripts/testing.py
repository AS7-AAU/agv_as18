#module imports
import numpy as np
import sys
import random
import time

# list with the names of different components
components = ['C1','C2','C3','C4','C5','C6']

def unloading(component):
    """Updating component storages in the assembly"""
    if component == "C1":
        C_storage[0] += 1
    elif component == "C2":
        C_storage[1] +=1
    elif component == "C3":
        C_storage[2] +=1
    elif component == "C4":
        C_storage[3] +=1
    elif component == "C5":
        C_storage[4] +=1
    elif component == "C6":
        C_storage[5] +=1

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

def assembly_check(AS_storage,Product_components,C_storage):
    """check if the storage components are enough to construct the next product and return the new storage quantities"""
    for component in Product_components:
        if len(AS_storage) > 0:
            for component_ in AS_storage:
                if component == component_:
                    if component_ == 'C1':
                        C_storage[0] -=1
                    elif component == 'C2':
                        C_storage[1] -=1
                    elif component == 'C3':
                        C_storage[2] -=1
                    elif component == 'C4':
                        C_storage[3] -=1
                    elif component == 'C5':
                        C_storage[4] -=1
                    elif component == 'C6':
                        C_storage[5] -=1
                    del AS_storage[AS_storage.index(component_)]
                    y = True
                    break
                else:
                    y = False
        else:
            y = False
    return [y,AS_storage,C_storage]

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
ProductList = [P1,P3,P2]
Product_List = [P_1,P_3,P_2]

# Products that need to pass quality check
QualityList = list(ProductList)
Quality_List = list(Product_List)
Construction_List = ['P1','P3','P2']

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
# Initialize the list that keeps track of the items the robot carries
robot_items = []

#Initialize the assembly storage and the quantity of each different component in the storage
AS_storage = []
C_storage = [0,0,0,0,0,0]


restart = True
while restart:
    # The code ends when all the components are constructed
    if len(Construction_List) == 0:
        restart = False
    else:
        # iterate over every waypoint in the waypoint list
        for k in range(len(b)):
            print("BEAST is moving towards: {}".format(b[k]))
            time.sleep(1)
            # If the waypoint is a component station, load and delete the task from the task sequence
            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                print("BEAST has arrived in station: {}".format(b[k]))
                print("BEAST is loading")
                del task_sequence[0]
                robot_items.append(b[k])
                time.sleep(1)
            # if the waypoint is the assembly station, unload, delete the task, update the assembly storage and the quantities
            elif b[k] == 'AS':
                print("BEAST has arrived in the Assembly station")
                print("BEAST is unloading")
                del task_sequence[0]
                AS_storage = AS_storage + robot_items
                if len(robot_items) == 2:
                    time.sleep(2)
                else:
                    time.sleep(1)
                for i in range(len(robot_items)):
                    unloading(robot_items[i])
                print("C_storage: {}".format(C_storage))
                
                robot_items = []
                # Every time the robot unloads in the assembly station, check if the first component in the Product List can be assembled
                if len(Product_List)>0:
                    AS_storage_check = list(AS_storage)
                    C_storage_check = list(C_storage)
                    match = assembly_check(AS_storage_check,Product_List[0],C_storage_check)
                    if match[0] == True:
                        print("Product {} is getting assembled".format(Construction_List[0]))
                        # Delete the product from the product list since the robot starts to gather components for the next product
                        del ProductList[0]
                        del Product_List[0]
                        # Update the storage after the use of components by the assembly statiion
                        AS_storage = match[1]
                        C_storage = match[2]
                        
                        
                        print("Quality Check")
                        quality_answer = input("Is the product okay?")

                        # Quality check based on user input
                        if quality_answer == '':
                            # if the user presses enter, the constructed product is faulty
                            QC_check = False
                            print("Faulty Product")
                        else:
                            # in any other occasion the product is fine and we delete it from the associated lists
                            QC_check = True
                            del Construction_List[0]
                            del Quality_List[0]
                            del QualityList[0]
                            print("OK")
                            print("Product Assembled")
                        if QC_check == False:
                            # If the product is faulty immediately check if there are already enough components in the assembly for the reconstruction to start immediately
                            AS_storage_check = list(AS_storage)
                            C_storage_check = list(C_storage)
                            if assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[0] == True:
                                while assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[0] == True:
                                    print("Product {} is getting reassembled".format(Construction_List[0]))
                                    AS_storage = assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[1]
                                    C_storage = assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[2]
                                    print("Quality Check")
                                    quality_answer = input("Is the product okay?")
                                    if quality_answer != '':
                                        # product is ok
                                        del Construction_List[0]
                                        del Quality_List[0]
                                        del QualityList[0]
                                        break
                                    else:
                                        # product is faulty
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])
                                        # we must add in the task sequence the components of the product that was faulty
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                # if the robot is in the right side of the map and does not carry anything
                                if (BEAST[1] > 52.5) and (len(robot_items) == 0):

                                    b=[]

                                    ProductList.insert(0,QualityList[0])
                                    Product_List.insert(0,Quality_List[0])

                                    # insert the components of the faulty product in the beginning of the task sequence 
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                    z=2
                                    while z < len(task_sequence):
                                        task_sequence.insert(z, AS)
                                        z += 3
                                    task_sequence.append(AS)

                                    # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    # exit the for loop and restart with the new waypoint list
                                    break
                                # if the robot is on the right side of the map and it carries one component
                                elif (BEAST[1] > 52.5) and (len(robot_items) == 1):

                                    b=[]    
                                    # checking if there is space in the buffers
                                    if C_storage[components.index(robot_items[0])]<3:
                                        # if there is space then unload the component
                                        print("BEAST has arrived in the Assembly station")
                                        print("BEAST is unloading")
                                        del task_sequence[0]
                                        AS_storage = AS_storage + robot_items
                                        BEAST[1] = AS[1]
                                        BEAST[2] = AS[2]

                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])

                                        # insert the components of the faulty product in the beginning of the task sequence 
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)

                                        # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    # if there is no space in the buffers         
                                    else:
                                        # create a temporary task sequence for the robot to return the component for which there is no space
                                        temp_task_sequence = [find_component(robot_items[0])]
                                        graph = dict(graph_right)

                                        c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                        for j in range(1,len(c)):
                                            b.append(c[j])

                                        for k in range(len(b)):
                                            print("BEAST is moving towards: {}".format(b[k]))
                                            time.sleep(1)
                                            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                print("BEAST has arrived in station: {}".format(b[k]))
                                                print("BEAST is unloading")

                                                task_sequence.insert(0,find_component(robot_items[0]))
                                                BEAST[1] = find_component(robot_items[0])[1]
                                                BEAST[2] = find_component(robot_items[0])[2]
                                        
                                                robot_items=[]
                                                time.sleep(1)
                                        b=[]
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])

                                        # insert the components of the faulty product in the beginning of the task sequence 
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)

                                        # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    break

                                # If the robot is on the right side and it carries exactly 2 items
                                elif (BEAST[1] > 52.5) and (len(robot_items) == 2):
                                    b=[]
                                    # If there is space in the buffers for the first component
                                    if C_storage[components.index(robot_items[0])]<3:
                                        C_storage_check = list(C_storage)
                                        C_storage_check[components.index(robot_items[0])]+=1
                                        # and if there is space for the second component too
                                        if C_storage_check[components.index(robot_items[1])]<3:
                                            print("BEAST has arrived in the Assembly station")
                                            print("BEAST is unloading")
                                            del task_sequence[0]
                                            AS_storage = AS_storage + robot_items
                                            BEAST[1] = AS[1]
                                            BEAST[2] = AS[2]

                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            # insert the components of the faulty product in the beginning of the task sequence
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)

                                            # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                        # If there is no space for the second component        
                                        else:
                                            #unload only the first
                                            print("BEAST has arrived in the Assembly station")
                                            print("BEAST is unloading")
                                            del task_sequence[0]
                                            AS_storage = AS_storage + robot_items[0]
                                            del robot_items[0]
                                            BEAST[1] = AS[1]
                                            BEAST[2] = AS[2]
                                            
                                            # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                                            temp_task_sequence = [find_component(robot_items[0])]
                                            graph = dict(graph_right)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    robot_items=[]
                                                    time.sleep(1)
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            # insert the components of the faulty product in the beginning of the task sequence
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)

                                            # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    # if there is no space in the buffers for the first component            
                                    else:
                                        # If there is space for the second one
                                        if C_storage_check[components.index(robot_items[1])]<3:
                                            print("BEAST has arrived in the Assembly station")
                                            print("BEAST is unloading")
                                            del task_sequence[0]
                                            AS_storage = AS_storage + robot_items[1]
                                            del robot_items[1]
                                            BEAST[1] = AS[1]
                                            BEAST[2] = AS[2]
                                            
                                            # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                                            temp_task_sequence = [find_component(robot_items[0])]
                                            graph = dict(graph_right)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    robot_items=[]
                                                    time.sleep(1)
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            # insert the components of the faulty product in the beginning of the task sequence
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)

                                            # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                        # if there is no space for the second component either
                                        else:
                                            temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                                            for i in range(len(temp_task_sequence)):
                                                if BEAST[1] > 52.5:
                                                    graph = dict(graph_right)
                                                else:
                                                    graph = dict(graph_left)
                                                for j in range(1,len(c)):
                                                    b.append(c[j])
                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                        time.sleep(1)
                                            task_sequence.insert(0,find_component(robot_items[0]))
                                            task_sequence.insert(0,find_component(robot_items[1]))
                                            robot_items=[]
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            # insert the components of the faulty product in the beginning of the task sequence
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)

                                            # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    break
                                # robot is in the left side and carries no components
                                elif  (BEAST[1] < 52.5) and (len(robot_items) == 0):
                                    b=[]
                                    ProductList.insert(0,QualityList[0])
                                    Product_List.insert(0,Quality_List[0])
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                    
                                    z=2
                                    while z < len(task_sequence):
                                        task_sequence.insert(z, AS)
                                        z += 3
                                    task_sequence.append(AS)
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
                                    break
                                # robot is in the left side and carries one component
                                elif  (BEAST[1] < 52.5) and (len(robot_items) == 1):
                                    b=[]
                                    # if the component is part of the product that is assembled
                                    if robot_items[0] in Quality_List[0]:
                                        Quality_List[0].append(robot_items[0])
                                        Quality_List[0].remove([robot_items[0]])
                                        QualityList[0].append(find_component(robot_items[0]))
                                        QualityList[0].remove(find_component(robot_items[0]))

                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        
                                        z=1
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)
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
                                    # if the component is not part of the product assembled 
                                    else:
                                        #create a temporary task sequence to return the product to its storage station
                                        temp_task_sequence = [find_component(robot_items[0])]
                                        graph = dict(graph_right)

                                        c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                        for j in range(1,len(c)):
                                            b.append(c[j])

                                        for k in range(len(b)):
                                            print("BEAST is moving towards: {}".format(b[k]))
                                            time.sleep(1)
                                            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                print("BEAST has arrived in station: {}".format(b[k]))
                                                print("BEAST is unloading")

                                                task_sequence.insert(0,find_component(robot_items[0]))
                                                BEAST[1] = find_component(robot_items[0])[1]
                                                BEAST[2] = find_component(robot_items[0])[2]
                                        
                                                robot_items=[]
                                                time.sleep(1)
                                        b=[]
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])

                                        # insert the components of the faulty product in the beginning of the task sequence 
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)

                                        # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                
                                
                                    break
                                # if the robot is on the left side and carries 2 components
                                elif  (BEAST[1] < 52.5) and (len(robot_items) == 2):
                                    b=[]
                                    # if the first component is part of the product which is assembled
                                    if robot_items[0] in Quality_List[0]:
                                        Quality_List_check = list(Quality_List[0])
                                        Quality_List_check.remove(robot_items[0])
                                        # and if the second one is part of the product as well
                                        if robot_items[1] in Quality_List_check:
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)
                                            # the first task would be to bring the products that the robot carries to the assembly station
                                            task_sequence.insert(0,AS)
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
                                        # if the second component is not part of the product
                                        else:
                                            #put it back in its storage station
                                            temp_task_sequence = [find_component(robot_items[1])]
                                            graph = dict(graph_left)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    robot_items=[]
                                                    time.sleep(1)
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])

                                            # insert the components of the faulty product in the beginning of the task sequence 
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            z=1
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)

                                            # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    # if both components that the robot carries are not part of the product that is assembled
                                    elif robot_items[0] not in Quality_List[0] and robot_items[1] not in Quality_List[0]:
                                        # put both back to their stations
                                        temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                                        for i in range(len(temp_task_sequence)):
                                            if BEAST[1] > 52.5:
                                                graph = dict(graph_right)
                                            else:
                                                graph = dict(graph_left)
                                            for j in range(1,len(c)):
                                                b.append(c[j])
                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                                    time.sleep(1)
                                        task_sequence.insert(0,find_component(robot_items[0]))
                                        task_sequence.insert(0,find_component(robot_items[1]))
                                        robot_items=[]
                                        b=[]
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)
                                        task_sequence.insert(0,AS)
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
                                    # if the first component is not part of the product and the second one is
                                    elif robot_items[0] not in Quality_List[0] and robot_items[1] in Quality_List[0]:
                                        # put the first one back to its station
                                        temp_task_sequence = [find_component(robot_items[0])]
                                        graph = dict(graph_left)

                                        c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                        for j in range(1,len(c)):
                                            b.append(c[j])

                                        for k in range(len(b)):
                                            print("BEAST is moving towards: {}".format(b[k]))
                                            time.sleep(1)
                                            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                print("BEAST has arrived in station: {}".format(b[k]))
                                                print("BEAST is unloading")

                                                task_sequence.insert(0,find_component(robot_items[0]))
                                                BEAST[1] = find_component(robot_items[0])[1]
                                                BEAST[2] = find_component(robot_items[0])[2]
                                        
                                                robot_items=[]
                                                time.sleep(1)
                                        b=[]
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])

                                        # insert the components of the faulty product in the beginning of the task sequence 
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        z=1
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)

                                        # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                        break
                            # if we do not have enough components to restart assembly immediately
                            else:
                                b =[]
                                k=0
                                # The robot is on the right side of the map and it does not carry anything
                                if (BEAST[1] > 52.5) and (len(robot_items) == 0):
                                    # find which components are missing from the assembly station in order to start the reassembly
                                    components_not_stored = []
                                    components_stored = []
                                    AS_storage_check = list(AS_storage)
                                    for component in Quality_List[0]:
                                        if component in AS_storage:
                                            components_stored.append(component)
                                            AS_storage_check.remove(component)
                                        else:
                                            components_not_stored.append(component)
                                    # if only one component is missing
                                    if len(components_not_stored) == 1:
                                        # put in the beginning of the list and recalculate the waypoint list
                                        Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                        QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                    # if more than one components are missing
                                    else:
                                        # put two of them in the beginning of the list and recalculate the waypoint list
                                        Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                        Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                        QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                        QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                
                                    ProductList.insert(0,QualityList[0])
                                    Product_List.insert(0,Quality_List[0])

                                    # insert the components of the faulty product in the beginning of the task sequence 
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                    z=2
                                    while z < len(task_sequence):
                                        task_sequence.insert(z, AS)
                                        z += 3
                                    task_sequence.append(AS)

                                    # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                    # exit the for loop and restart with the new waypoint list
                                    break
                                # the robot is in the right side and it carries exactly one item (can happen only if it carries the last component for the last product)
                                elif (BEAST[1] > 52.5) and (len(robot_items) == 1):
                                    # checking if there is space in the buffers
                                    if C_storage[components.index(robot_items[0])]<3:
                                        # if there is space then unload the component
                                        print("BEAST has arrived in the Assembly station")
                                        print("BEAST is unloading")
                                        del task_sequence[0]
                                        AS_storage = AS_storage + robot_items
                                        BEAST[1] = AS[1]
                                        BEAST[2] = AS[2]

                                        components_not_stored = []
                                        components_stored = []
                                        AS_storage_check = list(AS_storage)
                                        for component in Quality_List[0]:
                                            if component in AS_storage:
                                                components_stored.append(component)
                                                AS_storage_check.remove(component)
                                            else:
                                                components_not_stored.append(component)

                                        if len(components_not_stored) == 1:
                                            # put in the beginning of the list and recalculate the waypoint list
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            QualityList[0].insert(0, QualityList[0].pop(Quality_List[0].index(find_component(components_not_stored[0]))))
                                        else:
                                            # put two of them in the beginning of the list and recalculate the waypoint list
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                
                                        

                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])

                                        # insert the components of the faulty product in the beginning of the task sequence
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)

                                        # Apply dijkstras for the new task sequence and create a new waypoint list
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

                                    # if there is no space in the buffers
                                    else :
                                        # if the component is not needed for the faulty product
                                        if robot_items[0] not in Quality_List[0]:
                                            # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                                            temp_task_sequence = [find_component(robot_items[0])]
                                            graph = dict(graph_right)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    robot_items=[]
                                                    time.sleep(1)
                                            # check how many of the components needed for the faulty product are not in the assembly storage
                                            components_not_stored = []
                                            components_stored = []
                                            AS_storage_check = list(AS_storage)
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                    AS_storage_check.remove(component)
                                                else:
                                                    components_not_stored.append(component)
                                            # if only one component is missing
                                            if len(components_not_stored) == 1:
                                                b=[]
                                                # put in the beginning of the list and recalculate the waypoint list
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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
                                            # if more than one components are missing
                                            else:
                                                # add 2 of them in the beginning of the list and recalculate the waypoint list
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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
                                            
                                        # if the component is needed for the assembly of the faulty component
                                        elif robot_items[0] in Quality_List[0]:
                                            # check how many of the components needed for the faulty product are not in the assembly storage
                                            components_not_stored = []
                                            components_stored = []
                                            AS_storage_check = list(AS_storage)
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                    AS_storage_check.remove(component)
                                                else:
                                                    components_not_stored.append(component)
                                            # if only one component is missing
                                            if len(components_not_stored) == 1:
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                b=[]
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                # insert the components of the faulty product in the beginning of the task sequence
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=1
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)

                                                # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                            # if we are missing more than one components
                                            else:
                                                # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                                                temp_task_sequence = [find_component(robot_items[0])]
                                                graph = dict(graph_right)

                                                c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                for j in range(1,len(c)):
                                                    b.append(c[j])

                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        task_sequence.insert(0,find_component(robot_items[0]))
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                
                                                        robot_items=[]
                                                        time.sleep(1)
                                                b=[]
                                                # add 2 of them in the beginning of the list and recalculate the waypoint list
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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
                                    break            
                                
                                # If the robot is on the right side and it carries exactly 2 items
                                elif (BEAST[1] > 52.5) and (len(robot_items) == 2):
                                    # If there is space in the buffers for the first component
                                    if C_storage[components.index(robot_items[0])]<3:
                                        C_storage_check = list(C_storage)
                                        C_storage_check[components.index(robot_items[0])]+=1
                                        # and if there is space for the second component too
                                        if C_storage_check[components.index(robot_items[1])]<3:
                                            print("BEAST has arrived in the Assembly station")
                                            print("BEAST is unloading")
                                            del task_sequence[0]
                                            AS_storage = AS_storage + robot_items
                                            BEAST[1] = AS[1]
                                            BEAST[2] = AS[2]


                                            # find which components are needed
                                            components_not_stored = []
                                            components_stored = []
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                else:
                                                    components_not_stored.append(component)
                                            
                                            if len(components_not_stored) == 1:
                                                # put in the beginning of the list and recalculate the waypoint list
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                            else:
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))

                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            # insert the components of the faulty product in the beginning of the task sequence
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)

                                            # Apply dijkstras for the new task sequence and create a new waypoint list
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
                                        # if there is no space for the second component
                                        else:
                                            print("BEAST has arrived in the Assembly station")
                                            print("BEAST is unloading")
                                            del task_sequence[0]
                                            AS_storage = AS_storage + robot_items[0]
                                            del robot_items[0]
                                            BEAST[1] = AS[1]
                                            BEAST[2] = AS[2]
                                            if robot_items[0] not in Quality_List[0]:
                                                # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                                                temp_task_sequence = [find_component(robot_items[0])]
                                                graph = dict(graph_right)

                                                c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                for j in range(1,len(c)):
                                                    b.append(c[j])

                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        task_sequence.insert(0,find_component(robot_items[0]))
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                
                                                        robot_items=[]
                                                        time.sleep(1)
                                                # find which components are needed
                                                components_not_stored = []
                                                components_stored = []
                                                for component in Quality_List[0]:
                                                    if component in AS_storage:
                                                        components_stored.append(component)
                                                    else:
                                                        components_not_stored.append(component)
                                                # if only one is needed
                                                if len(components_not_stored) == 1:
                                                    b=[]
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=2
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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
                                                # if more than one components are needed
                                                else:
                                                    b=[]
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=2
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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
                                            # if the component is needed for the assembly of the faulty component
                                            elif robot_items[0] in Quality_List[0]:

                                                components_not_stored = []
                                                components_stored = []
                                                for component in Quality_List[0]:
                                                    if component in AS_storage:
                                                        components_stored.append(component)
                                                    else:
                                                        components_not_stored.append(component)

                                                if len(components_not_stored) == 1:
                                                    
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=1
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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

                                                else:
                                                    # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                                                    temp_task_sequence = [find_component(robot_items[0])]
                                                    graph = dict(graph_right)

                                                    c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                    for j in range(1,len(c)):
                                                        b.append(c[j])

                                                    for k in range(len(b)):
                                                        print("BEAST is moving towards: {}".format(b[k]))
                                                        time.sleep(1)
                                                        if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                            print("BEAST has arrived in station: {}".format(b[k]))
                                                            print("BEAST is unloading")

                                                            task_sequence.insert(0,find_component(robot_items[0]))
                                                            BEAST[1] = find_component(robot_items[0])[1]
                                                            BEAST[2] = find_component(robot_items[0])[2]
                                                    
                                                            robot_items=[]
                                                            time.sleep(1)

                                                    b=[]
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))            
                                    # if there is no space for the first component and there is space for the second one
                                    elif C_storage[components.index(robot_items[0])]>=3 and C_storage[components.index(robot_items[1])]<3:
                                        # leave the second one in the buffer
                                        print("BEAST has arrived in the Assembly station")
                                        print("BEAST is unloading")
                                        del task_sequence[0]
                                        AS_storage = AS_storage + robot_items[1]
                                        del robot_items[1]
                                        BEAST[1] = AS[1]
                                        BEAST[2] = AS[2]
                                        
                                        # if the component for which there is no space is not needed for the faulty product
                                        if robot_items[0] not in Quality_List[0]:
                                            # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                                            temp_task_sequence = [find_component(robot_items[0])]
                                            graph = dict(graph_right)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    robot_items=[]
                                                    time.sleep(1)
                                            b=[]
                                            # check which components are needed
                                            components_not_stored = []
                                            components_stored = []
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                else:
                                                    components_not_stored.append(component)

                                            # if only one component is needed
                                            if len(components_not_stored) == 1:
                                                
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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

                                            # if 2 or more components are needed
                                            else:
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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
                                            
                                        # if the component is needed for the assembly of the faulty component
                                        elif robot_items[0] in Quality_List[0]:

                                            components_not_stored = []
                                            components_stored = []
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                else:
                                                    components_not_stored.append(component)

                                            if len(components_not_stored) == 1:
                                                
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=1
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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

                                            else:
                                                # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                                                temp_task_sequence = [find_component(robot_items[0])]
                                                graph = dict(graph_right)

                                                c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                for j in range(1,len(c)):
                                                    b.append(c[j])

                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        task_sequence.insert(0,find_component(robot_items[0]))
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                
                                                        robot_items=[]
                                                        time.sleep(1)

                                                b=[]
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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

                                    elif C_storage[components.index(robot_items[0])]>=3 and C_storage[components.index(robot_items[1])]>=3:
                                        if robot_items[0] not in Quality_List[0] and robot_items[1] not in Quality_List[0]:
                                            temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                                            for i in range(len(temp_task_sequence)):
                                                if BEAST[1] > 52.5:
                                                    graph = dict(graph_right)
                                                else:
                                                    graph = dict(graph_left)
                                                for j in range(1,len(c)):
                                                    b.append(c[j])
                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                        time.sleep(1)
                                            task_sequence.insert(0,find_component(robot_items[0]))
                                            task_sequence.insert(0,find_component(robot_items[1]))
                                            robot_items=[]
                                            b=[]

                                            
                                            components_not_stored = []
                                            components_stored = []
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                else:
                                                    components_not_stored.append(component)
                                            
                                            if len(components_not_stored) == 1:
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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

                                            elif len(components_not_stored) == 2:
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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
                                            

                                        elif robot_items[0] not in Quality_List[0] and robot_items[1] in Quality_List[0]:
                                            temp_task_sequence = [find_component(robot_items[0])]
                                            graph = dict(graph_right)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    del robot_items[0]
                                                    time.sleep(1)
                                            b=[]

                                            components_not_stored = []
                                            components_stored = []
                                            for component in Quality_List[0]:
                                                if component in AS_storage:
                                                    components_stored.append(component)
                                                else:
                                                    components_not_stored.append(component)
                                            if  len(components_not_stored) == 1:
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=1
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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

                                            else:
                                                b=[]
                                                temp_task_sequence = [find_component(robot_items[0])]
                                                graph = dict(graph_right)

                                                c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                for j in range(1,len(c)):
                                                    b.append(c[j])

                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        task_sequence.insert(0,find_component(robot_items[0]))
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                
                                                        del robot_items[0]
                                                        time.sleep(1)
                                                b=[]
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                
                                                ProductList.insert(0,QualityList[0])
                                                Product_List.insert(0,Quality_List[0])
                                                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                
                                                z=2
                                                while z < len(task_sequence):
                                                    task_sequence.insert(z, AS)
                                                    z += 3
                                                task_sequence.append(AS)
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
                                            
                                        
                                        elif robot_items[0] in Quality_List[0]:
                                            Quality_List_check = list(Quality_List[0])
                                            Quality_List_check.remove(robot_items[0])
                                            if robot_items[1] in Quality_List_check:
                                                components_not_stored = []
                                                components_stored = []
                                                for component in Quality_List[0]:
                                                    if component in AS_storage:
                                                        components_stored.append(component)
                                                    else:
                                                        components_not_stored.append(component)
                                                if len(components_not_stored)==1:
                                                    b=[]
                                                    temp_task_sequence = [find_component(robot_items[0])]
                                                    graph = dict(graph_right)

                                                    c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                    for j in range(1,len(c)):
                                                        b.append(c[j])

                                                    for k in range(len(b)):
                                                        print("BEAST is moving towards: {}".format(b[k]))
                                                        time.sleep(1)
                                                        if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                            print("BEAST has arrived in station: {}".format(b[k]))
                                                            print("BEAST is unloading")

                                                            task_sequence.insert(0,find_component(robot_items[0]))
                                                            BEAST[1] = find_component(robot_items[0])[1]
                                                            BEAST[2] = find_component(robot_items[0])[2]
                                                    
                                                            del robot_items[0]
                                                            time.sleep(1)

                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=1
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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
                                                else:
                                                    temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                                                    for i in range(len(temp_task_sequence)):
                                                        if BEAST[1] > 52.5:
                                                            graph = dict(graph_right)
                                                        else:
                                                            graph = dict(graph_left)
                                                        for j in range(1,len(c)):
                                                            b.append(c[j])
                                                        for k in range(len(b)):
                                                            print("BEAST is moving towards: {}".format(b[k]))
                                                            time.sleep(1)
                                                            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                                print("BEAST has arrived in station: {}".format(b[k]))
                                                                print("BEAST is unloading")

                                                                
                                                                BEAST[1] = find_component(robot_items[0])[1]
                                                                BEAST[2] = find_component(robot_items[0])[2]
                                                                time.sleep(1)
                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    task_sequence.insert(0,find_component(robot_items[1]))
                                                    robot_items=[]
                                                    b=[]
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=2
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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
                                            else:
                                                temp_task_sequence = [find_component(robot_items[1])]
                                                graph = dict(graph_right)

                                                c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                for j in range(1,len(c)):
                                                    b.append(c[j])

                                                for k in range(len(b)):
                                                    print("BEAST is moving towards: {}".format(b[k]))
                                                    time.sleep(1)
                                                    if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                        print("BEAST has arrived in station: {}".format(b[k]))
                                                        print("BEAST is unloading")

                                                        task_sequence.insert(0,find_component(robot_items[0]))
                                                        BEAST[1] = find_component(robot_items[0])[1]
                                                        BEAST[2] = find_component(robot_items[0])[2]
                                                
                                                        del robot_items[1]
                                                        time.sleep(1)
                                                b=[]
                                                components_not_stored = []
                                                components_stored = []
                                                for component in Quality_List[0]:
                                                    if component in AS_storage:
                                                        components_stored.append(component)
                                                    else:
                                                        components_not_stored.append(component)

                                                if  len(components_not_stored) == 1:
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=1
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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
                                                else:
                                                    b=[]
                                                    temp_task_sequence = [find_component(robot_items[0])]
                                                    graph = dict(graph_right)

                                                    c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                                    for j in range(1,len(c)):
                                                        b.append(c[j])

                                                    for k in range(len(b)):
                                                        print("BEAST is moving towards: {}".format(b[k]))
                                                        time.sleep(1)
                                                        if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                            print("BEAST has arrived in station: {}".format(b[k]))
                                                            print("BEAST is unloading")

                                                            task_sequence.insert(0,find_component(robot_items[0]))
                                                            BEAST[1] = find_component(robot_items[0])[1]
                                                            BEAST[2] = find_component(robot_items[0])[2]
                                                    
                                                            del robot_items[0]
                                                            time.sleep(1)
                                                    b=[]
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                                    Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                                    QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                                    
                                                    ProductList.insert(0,QualityList[0])
                                                    Product_List.insert(0,Quality_List[0])
                                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                                    
                                                    z=2
                                                    while z < len(task_sequence):
                                                        task_sequence.insert(z, AS)
                                                        z += 3
                                                    task_sequence.append(AS)
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


                                    break

                                elif  (BEAST[1] < 52.5) and (len(robot_items) == 0):
                                    components_not_stored = []
                                    components_stored = []
                                    for component in Quality_List[0]:
                                        if component in AS_storage:
                                            components_stored.append(component)
                                        else:
                                            components_not_stored.append(component)

                                    if len(components_not_stored) ==1:
                                        Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                        QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))

                                    else:
                                        Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                        Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                        QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                        QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))

                                    ProductList.insert(0,QualityList[0])
                                    Product_List.insert(0,Quality_List[0])
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                    
                                    z=2
                                    while z < len(task_sequence):
                                        task_sequence.insert(z, AS)
                                        z += 3
                                    task_sequence.append(AS)
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
                                    
                                    break
                                elif (BEAST[1] < 52.5) and (len(robot_items) == 1):

                                    if robot_items[0] not in Quality_List[0]:
                                        temp_task_sequence = [find_component(robot_items[0])]
                                        graph = dict(graph_left)

                                        c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])
                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        for k in range(len(b)):
                                            print("BEAST is moving towards: {}".format(b[k]))
                                            time.sleep(1)
                                            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                print("BEAST has arrived in station: {}".format(b[k]))
                                                print("BEAST is unloading")

                                                task_sequence.insert(0,find_component(robot_items[0]))
                                                BEAST[1] = find_component(robot_items[0])[1]
                                                BEAST[2] = find_component(robot_items[0])[2]
                                        
                                                robot_items=[]
                                                time.sleep(1)
                                        b=[]
                                        components_not_stored = []
                                        components_stored = []
                                        for component in Quality_List[0]:
                                            if component in AS_storage:
                                                components_stored.append(component)
                                            else:
                                                components_not_stored.append(component)

                                        if len(components_not_stored) ==1:
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                        else:
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                        b=[]
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)
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

                                    elif robot_items[0] in Quality_List[0]:
                                        components_not_stored = []
                                        components_stored = []
                                        for component in Quality_List[0]:
                                            if component in AS_storage:
                                                components_stored.append(component)
                                            else:
                                                components_not_stored.append(component)

                                        if len(components_not_stored) ==1:
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            
                                            z=1
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)
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

                                        else:

                                            b=[]
                                            temp_task_sequence = [find_component(robot_items[0])]
                                            graph = dict(graph_right)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])

                                            for j in range(1,len(c)):
                                                b.append(c[j])

                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    task_sequence.insert(0,find_component(robot_items[0]))
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                            
                                                    del robot_items[0]
                                                    time.sleep(1)
                                                    
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)
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
                                    break   

                                elif (BEAST[1] < 52.5) and (len(robot_items) == 2):
                                    if robot_items[0] not in Quality_List[0] and robot_items[1] not in Quality_List[0]:
                                        temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                                        for i in range(len(temp_task_sequence)):
                                            if BEAST[1] > 52.5:
                                                graph = dict(graph_left)
                                            else:
                                                graph = dict(graph_right)
                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[i][0])
                                            for j in range(1,len(c)):
                                                b.append(c[j])
                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                                    
                                                    BEAST[1] = find_component(robot_items[0])[1]
                                                    BEAST[2] = find_component(robot_items[0])[2]
                                                    time.sleep(1)
                                            task_sequence.insert(0,find_component(robot_items[0]))
                                            task_sequence.insert(0,find_component(robot_items[1]))
                                            robot_items=[]
                                            b=[]
                                        if len(components_not_stored) ==1:
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                        elif len(components_not_stored) >=2:
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                                            Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[1])))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                                            QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[1]))))
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        
                                        z=2
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)
                                        for i in range(len(task_sequence)):

                                            if BEAST[1] > 52.5:
                                                graph = dict(graph_left)
                                            else:
                                                graph = dict(graph_right)


                                            c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                            for j in range(1,len(c)):
                                                b.append(c[j])
                                            BEAST[1] = task_sequence[i][1] 
                                            BEAST[2] = task_sequence[i][2]
                                    elif robot_items[0] not in Quality_List[0] and robot_items[1] in Quality_List[0]:
                                        temp_task_sequence = [find_component(robot_items[0])]
                                        graph = dict(graph_left)

                                        c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])
                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        for k in range(len(b)):
                                            print("BEAST is moving towards: {}".format(b[k]))
                                            time.sleep(1)
                                            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                print("BEAST has arrived in station: {}".format(b[k]))
                                                print("BEAST is unloading")

                                        
                                                BEAST[1] = find_component(robot_items[0])[1]
                                                BEAST[2] = find_component(robot_items[0])[2]
                                        
                                        
                                                time.sleep(1)
                                        robot_items.remove(robot_items[0])
                                        task_sequence.insert(0,find_component(robot_items[0]))
                                        b=[]
                                        ProductList.insert(0,QualityList[0])
                                        Product_List.insert(0,Quality_List[0])
                                        task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                        
                                        z=1
                                        while z < len(task_sequence):
                                            task_sequence.insert(z, AS)
                                            z += 3
                                        task_sequence.append(AS)
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

                                    elif robot_items[0] in Quality_List[0]:
                                        Quality_List_check = list(Quality_List[0])
                                        Quality_List_check.remove(robot_items[0])
                                        if robot_items[1] in Quality_List_check:
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            
                                            z=2
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)
                                            task_sequence.insert(0,AS)
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
                                    
                                        else:
                                            temp_task_sequence = [find_component(robot_items[1])]
                                            graph = dict(graph_left)

                                            c = dijkstra(graph,BEAST[0],temp_task_sequence[0][0])
                                            for j in range(1,len(c)):
                                                b.append(c[j])
                                            for k in range(len(b)):
                                                print("BEAST is moving towards: {}".format(b[k]))
                                                time.sleep(1)
                                                if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                                                    print("BEAST has arrived in station: {}".format(b[k]))
                                                    print("BEAST is unloading")

                                            
                                                    BEAST[1] = find_component(robot_items[1])[1]
                                                    BEAST[2] = find_component(robot_items[1])[2]
                                            
                                            
                                                    time.sleep(1)
                                            robot_items.remove(robot_items[1])
                                            task_sequence.insert(0,find_component(robot_items[1]))
                                            b=[]
                                            ProductList.insert(0,QualityList[0])
                                            Product_List.insert(0,Quality_List[0])
                                            task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                            
                                            z=1
                                            while z < len(task_sequence):
                                                task_sequence.insert(z, AS)
                                                z += 3
                                            task_sequence.append(AS)
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
                                        break