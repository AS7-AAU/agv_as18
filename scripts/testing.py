import numpy as np
import sys
import random
import time


def unloading(component):
    if robot_items[i] == "C1":
        C_storage[0] += 1
    elif robot_items[i] == "C2":
        C_storage[1] +=1
    elif robot_items[i] == "C3":
        C_storage[2] +=1
    elif robot_items[i] == "C4":
        C_storage[3] +=1
    elif robot_items[i] == "C5":
        C_storage[4] +=1
    elif robot_items[i] == "C6":
        C_storage[5] +=1
def find_component(component):
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

def dijkstra(graph,start,goal):
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
        #print('Shortest distance is ' + str(shortest_distance[goal]))
        #print('And the path is ' + str(path))
        return path

P1 = [C1,C3,C4,C4]
P2 = [C1,C2,C5,C6]
P3 = [C3,C3,C5]
P4 = [C2,C3,C4]    


P_1 = [P1[0][0],P1[1][0],P1[2][0],P1[3][0]]
P_2 = [P2[0][0],P2[1][0],P2[2][0],P2[3][0]]
P_3 = [P3[0][0],P3[1][0],P3[2][0]]
P_4 = [P4[0][0],P4[1][0],P4[2][0]]

ProductList = [P1,P3,P2]
Product_List = [P_1,P_3,P_2]
QualityList = list(ProductList)
Quality_List = list(Product_List)
Construction_List = ['P1','P3','P2']

task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
print(task_sequence)
i = 2
while i < len(task_sequence):
    task_sequence.insert(i, AS)
    i += 3

task_sequence.append(AS)
robot_items = []
b=[]
for i in range(len(task_sequence)):

    if BEAST[1] > 52.5:
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


    c = dijkstra(graph,BEAST[0],task_sequence[i][0])


    for j in range(1,len(c)):
        b.append(c[j])
    BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
    BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
    #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
    #print("----------------------------------------------------------")
print(b)

AS_storage = []
robot_items = []
C_storage = [0,0,0,0,0,0]

restart = True
while restart:
    if len(Construction_List) == 0:
        restart = False
    else:
        for k in range(len(b)):
            print("BEAST is moving towards: {}".format(b[k]))
            time.sleep(1)
            if b[k] == 'C1' or b[k] == 'C2' or b[k] == 'C3' or b[k] == 'C4' or b[k] == 'C5' or b[k] == 'C6' :
                print("BEAST has arrived in station: {}".format(b[k]))
                print("BEAST is loading")
                del task_sequence[0]
                robot_items.append(b[k])
                time.sleep(1)
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
                #print(AS_storage)
                robot_items = []
                if len(Product_List)>0:
                    AS_storage_check = list(AS_storage)
                    C_storage_check = list(C_storage)
                    match = assembly_check(AS_storage_check,Product_List[0],C_storage_check)
                    if match[0] == True:
                        print("Product {} is getting assembled".format(Construction_List[0]))
                        QC = Construction_List[0]
                        
                        del ProductList[0]
                        del Product_List[0]
                        AS_storage = match[1]
                        C_storage = match[2]
                        
                        print("Quality Check")
                        quality_answer = input("Is the product okay?")

                        if quality_answer == '':
                            QC_check = False
                            print("Faulty Product")
                        else:
                            QC_check = True
                            del Construction_List[0]
                            del Quality_List[0]
                            del QualityList[0]
                            print("OK")
                            print("Product Assembled")
                        if QC_check == False:
                            
                            AS_storage_check = list(AS_storage)
                            C_storage_check = list(C_storage)
                            while assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[0] == True:
                                print("Product {} is getting reassembled".format(Construction_List[0]))
                                AS_storage = assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[1]
                                C_storage = assembly_check(AS_storage_check,Quality_List[0],C_storage_check)[2]
                                print("Quality Check")
                                quality_answer = input("Is the product okay?")
                                if quality_answer != '':
                                    del Construction_List[0]
                                    del Quality_List[0]
                                    del QualityList[0]
                                    break
                                else:
                                    ProductList.insert(0,QualityList[0])
                                    Product_List.insert(0,Quality_List[0])
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    
                            b =[]
                            k=0
                            print("Product added back to Construction List")
                            if (BEAST[1] > 52.5) and (len(robot_items) == 0):
                            
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


                                    c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                    for j in range(1,len(c)):
                                        b.append(c[j])
                                    BEAST[1] = task_sequence[i][1] 
                                    BEAST[2] = task_sequence[i][2] 
                                
                                break
                            elif (BEAST[1] > 52.5) and (len(robot_items) == 1):
                                if ((robot_items[0]=='C1') and C_storage[0]<3) or ((robot_items[0]=='C2') and C_storage[1]<3) or ((robot_items[0]=='C3') and C_storage[2]<3) or ((robot_items[0]=='C4') and C_storage[3]<3) or ((robot_items[0]=='C5') and C_storage[4]<3) or ((robot_items[0]=='C6') and C_storage[5]<3):
                                    print("BEAST has arrived in the Assembly station")
                                    print("BEAST is unloading")
                                    del task_sequence[0]
                                    AS_storage = AS_storage + robot_items
                                    BEAST[1] = AS[1]
                                    BEAST[2] = AS[2]
                                    
                                else :
                                    temp_task_sequence = [find_component(robot_items[0])]
                                   
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
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                    
                                    z=2
                                    while z < len(task_sequence):
                                        task_sequence.insert(z, AS)
                                        z += 3
                                    task_sequence.append(AS)
                                    for i in range(len(task_sequence)):

                                        if BEAST[1] > 52.5:
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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]
                                break
                            elif (BEAST[1] > 52.5) and (len(robot_items) == 2):
                                if ((robot_items[0]=='C1') and C_storage[0]<3) or ((robot_items[0]=='C2') and C_storage[1]<3) or ((robot_items[0]=='C3') and C_storage[2]<3) or ((robot_items[0]=='C4') and C_storage[3]<3) or ((robot_items[0]=='C5') and C_storage[4]<3) or ((robot_items[0]=='C6') and C_storage[5]<3) and ((robot_items[1]=='C1') and C_storage[0]<3) or ((robot_items[1]=='C2') and C_storage[1]<3) or ((robot_items[1]=='C3') and C_storage[2]<3) or ((robot_items[1]=='C4') and C_storage[3]<3) or ((robot_items[1]=='C5') and C_storage[4]<3) or ((robot_items[1]=='C6') and C_storage[5]<3):
                                    print("BEAST has arrived in the Assembly station")
                                    print("BEAST is unloading")
                                    del task_sequence[0]
                                    AS_storage = AS_storage + robot_items
                                    BEAST[1] = AS[1]
                                    BEAST[2] = AS[2]
                                else:
                                    temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                                    for i in range(len(temp_task_sequence)):
                                        if BEAST[1] > 52.5:
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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]
                                break

                            elif  (BEAST[1] < 52.5) and (len(robot_items) == 0):
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


                                    c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                    for j in range(1,len(c)):
                                        b.append(c[j])
                                    BEAST[1] = task_sequence[i][1] 
                                    BEAST[2] = task_sequence[i][2] 
                                
                                break
                            elif (BEAST[1] < 52.5) and (len(robot_items) == 1):
                                if robot_items[0] not in Quality_List[0]:
                                    temp_task_sequence = [find_component(robot_items[0])]
                                    graph = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
                                    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
                                    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
                                    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
                                    BEAST[0]:{C1[0]:np.sqrt((BEAST[1]-C1[1])**2+(BEAST[2]-C1[2])**2),C2[0]:np.sqrt((BEAST[1]-C2[1])**2+(BEAST[2]-C2[2])**2),C3[0]:np.sqrt((BEAST[1]-C3[1])**2+(BEAST[2]-C3[2])**2),
                                    C4[0]:np.sqrt((BEAST[1]-C4[1])**2+(BEAST[2]-C4[2])**2),C5[0]:np.sqrt((BEAST[1]-C5[1])**2+(BEAST[2]-C5[2])**2),C6[0]:np.sqrt((BEAST[1]-C6[1])**2+(BEAST[2]-C6[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
                                    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}

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
                                    task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                                    task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                                    
                                    z=2
                                    while z < len(task_sequence):
                                        task_sequence.insert(z, AS)
                                        z += 3
                                    task_sequence.append(AS)
                                    for i in range(len(task_sequence)):

                                        if BEAST[1] > 52.5:
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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]
                                elif robot_items[0] in Quality_List[0]:
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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]
                                elif robot_items[0] in Quality_List[0] and robot_items[1] in Quality_List[0].remove(Quality_List[robot_items[0]]):
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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]
                                elif robot_items[0] not in Quality_List[0] and robot_items[1] in Quality_List[0]:
                                    temp_task_sequence = [find_component(robot_items[0])]
                                    graph = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
                                    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
                                    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
                                    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
                                    BEAST[0]:{C1[0]:np.sqrt((BEAST[1]-C1[1])**2+(BEAST[2]-C1[2])**2),C2[0]:np.sqrt((BEAST[1]-C2[1])**2+(BEAST[2]-C2[2])**2),C3[0]:np.sqrt((BEAST[1]-C3[1])**2+(BEAST[2]-C3[2])**2),
                                    C4[0]:np.sqrt((BEAST[1]-C4[1])**2+(BEAST[2]-C4[2])**2),C5[0]:np.sqrt((BEAST[1]-C5[1])**2+(BEAST[2]-C5[2])**2),C6[0]:np.sqrt((BEAST[1]-C6[1])**2+(BEAST[2]-C6[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
                                    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}

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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]
                                elif robot_items[0] in Quality_List[0] and robot_items[1] not in Quality_List[0].remove(Quality_List[robot_items[0]]):
                                    temp_task_sequence = [find_component(robot_items[1])]
                                    graph = {AS[0]:{MWP1[0]:AS_MWP1,MWP2[0]:AS_MWP2,MWP3[0]:AS_MWP3},MWP1[0]:{AS[0]:AS_MWP1,C1[0]:C1_MWP1,C2[0]:C2_MWP1,C3[0]:C3_MWP1,C4[0]:C4_MWP1,C5[0]:C5_MWP1,C6[0]:C6_MWP1},MWP2[0]:{AS[0]:AS_MWP2,C1[0]:C1_MWP2,C6[0]:C6_MWP2,C2[0]:C2_MWP2,C5[0]:C5_MWP2,C3[0]:C3_MWP2,C4[0]:C4_MWP2},
                                    MWP3[0]:{AS[0]:AS_MWP3,C6[0]:C6_MWP3,C5[0]:C5_MWP3,C4[0]:C4_MWP3,C3[0]:C3_MWP3,C2[0]:C2_MWP3,C1[0]:C1_MWP3},C1[0]:{MWP1[0]:C1_MWP1,MWP2[0]:C1_MWP2,MWP3[0]:C1_MWP3,C2[0]:C1_C2,C3[0]:C1_C3,C4[0]:C1_C4,C5[0]:C1_C5,C6[0]:C1_C6},C2[0]:{MWP1[0]:C2_MWP1,MWP2[0]:C2_MWP2,MWP3[0]:C2_MWP3,C1[0]:C1_C2,C3[0]:C2_C3,C4[0]:C2_C4,C5[0]:C2_C5,C6[0]:C2_C6},
                                    C3[0]:{MWP1[0]:C3_MWP1,MWP2[0]:C3_MWP2,MWP3[0]:C3_MWP3,C1[0]:C1_C3,C2[0]:C2_C3,C4[0]:C3_C4,C5[0]:C3_C5,C6[0]:C3_C6},C4[0]:{MWP1[0]:C4_MWP1,MWP2[0]:C4_MWP2,MWP3[0]:C4_MWP3,C1[0]:C1_C4,C2[0]:C2_C4,C3[0]:C3_C4,C5[0]:C4_C5,C6[0]:C4_C6},
                                    C5[0]:{MWP1[0]:C5_MWP1,MWP2[0]:C5_MWP2,MWP3[0]:C5_MWP3,C1[0]:C1_C5,C2[0]:C2_C5,C3[0]:C3_C5,C4[0]:C4_C5,C6[0]:C5_C6},C6[0]:{MWP1[0]:C6_MWP1,MWP2[0]:C6_MWP2,MWP3[0]:C6_MWP3,C1[0]:C1_C6,C2[0]:C2_C6,C3[0]:C3_C6,C4[0]:C4_C6,C5[0]:C5_C6},
                                    BEAST[0]:{C1[0]:np.sqrt((BEAST[1]-C1[1])**2+(BEAST[2]-C1[2])**2),C2[0]:np.sqrt((BEAST[1]-C2[1])**2+(BEAST[2]-C2[2])**2),C3[0]:np.sqrt((BEAST[1]-C3[1])**2+(BEAST[2]-C3[2])**2),
                                    C4[0]:np.sqrt((BEAST[1]-C4[1])**2+(BEAST[2]-C4[2])**2),C5[0]:np.sqrt((BEAST[1]-C5[1])**2+(BEAST[2]-C5[2])**2),C6[0]:np.sqrt((BEAST[1]-C6[1])**2+(BEAST[2]-C6[2])**2),MWP1[0]:np.sqrt((BEAST[1]-MWP1[1])**2+(BEAST[2]-MWP1[2])**2),MWP2[0]:np.sqrt((BEAST[1]-MWP2[1])**2+(BEAST[2]-MWP2[2])**2),
                                    MWP3[0]:np.sqrt((BEAST[1]-MWP3[1])**2+(BEAST[2]-MWP3[2])**2)}}

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


                                        c = dijkstra(graph,BEAST[0],task_sequence[i][0])


                                        for j in range(1,len(c)):
                                            b.append(c[j])
                                        BEAST[1] = task_sequence[i][1] 
                                        BEAST[2] = task_sequence[i][2]                                   
                                break