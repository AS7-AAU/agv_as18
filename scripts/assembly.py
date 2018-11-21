#!/usr/bin/env python
import time

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
Construction_List = ['P1','P3','P2']




AS_storage = []
robot_items = []
C1_storage = 0
C2_storage = 0
C3_storage = 0
C4_storage = 0 
C5_storage = 0
C6_storage = 0

"""restart = True
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
                robot_items.append(b[k])
                time.sleep(1)
            elif b[k] == 'AS':
                print("BEAST has arrived in the Assembly station")
                print("BEAST is unloading")
                AS_storage = AS_storage + robot_items
                if len(robot_items) == 2:
                    time.sleep(2)
                else:
                    time.sleep(1)
                for i in range(len(robot_items)):
                    if robot_items[i] == "C1":
                        C1_storage += 1
                    elif robot_items[i] == "C2":
                        C2_storage +=1
                    elif robot_items[i] == "C3":
                        C3_storage +=1
                    elif robot_items[i] == "C4":
                        C4_storage +=1
                    elif robot_items[i] == "C5":
                        C5_storage +=1
                    elif robot_items[i] == "C6":
                        C6_storage +=1
                print("C1_storage: {}, C2_storage: {}, C3_storage: {}, C4_storage: {}, C5_storage: {}, C6_storage: {}".format(C1_storage,C2_storage,C3_storage,C4_storage,C5_storage,C6_storage))
                #print(AS_storage)
                robot_items = []"""
#get the status of the buffers from the server


                
                if len(Product_List)>0:
                    AS_storage_check = list(AS_storage)
                    C1_storage_check = C1_storage
                    C2_storage_check = C2_storage
                    C3_storage_check = C3_storage
                    C4_storage_check = C4_storage
                    C5_storage_check = C5_storage
                    C6_storage_check = C6_storage
                    for component in Product_List[0]:
                        if len(AS_storage_check) >= len(Product_List[0]):
                            for component_ in AS_storage_check:
                                if component == component_:
                                    if component_ == 'C1':
                                        C1_storage_check -=1
                                    elif component == 'C2':
                                        C2_storage_check -=1
                                    elif component == 'C3':
                                        C3_storage_check -=1
                                    elif component == 'C4':
                                        C4_storage_check -=1
                                    elif component == 'C5':
                                        C5_storage_check -=1
                                    elif component == 'C6':
                                        C6_storage_check -=1
                                    del AS_storage_check[AS_storage_check.index(component_)]
                                    y = True
                                    break
                                else:
                                    y = False
                        else:
                            y = False
                    if y == True:
                        print("Product {} is starting to assemble".format(Construction_List[0]))
                        QC = Construction_List[0]
                        
                        AS_storage = AS_storage_check
                        C1_storage = C1_storage_check
                        C2_storage = C2_storage_check
                        C3_storage = C3_storage_check
                        C4_storage = C4_storage_check
                        C5_storage = C5_storage_check
                        C6_storage = C6_storage_check
                        #Cloud needs to be updated
                        w = time.time()
                        while (time.time() - w <15) or not flag:
                            pass
                        if flag:
                            #implement the Fault Product Logic
                            flag = False
                        else:

                            del ProductList[0]
                            del Product_List[0]
                            del Construction_List[0]
                            msg = Bool()
                            msg.data = True
                            pub.publish(msg)


                        print("Quality Check")
                        quality_answer = input("Is the product okay?")

                        if quality_answer == 'n':
                            QC_check = False
                            print("Faulty Product")
                        else:
                            QC_check = True
                            print("OK")
                            print("Product Assembled")
                        if QC_check == False:
                            b =[]
                            k=0
                            print("Product added back to Construction List")
                            if (BEAST[1] > 52.5) and (len(robot_items) == 0):
                                if QC == "P1":
                                    ProductList.insert(0,P1)
                                    Product_List.insert(0,P_1)
                                    Construction_List.insert(0,"P1")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    
                                    break
                                elif QC == "P2":
                                    ProductList.insert(0,P2)
                                    Product_List.insert(0,P_2)
                                    Construction_List.insert(0,"P2")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    
                                    break
                                elif QC == "P3":
                                    ProductList.insert(0,P3)
                                    Product_List.insert(0,P_3)
                                    Construction_List.insert(0,"P3")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    
                                    break
                                elif QC == "P4":
                                    ProductList.insert(0,P4)
                                    Product_List.insert(0,P_4)
                                    Construction_List.insert(0,"P4")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    #print("time:", time.time()-a)
                                    break
                            
                            elif (BEAST[1] < 52.5) and (len(robot_items) == 0):
                                if QC == "P1":
                                    ProductList.insert(0,P1)
                                    Product_List.insert(0,P_1)
                                    Construction_List.insert(0,"P1")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    
                                    break
                                elif QC == "P2":
                                    ProductList.insert(0,P2)
                                    Product_List.insert(0,P_2)
                                    Construction_List.insert(0,"P2")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    
                                    break
                                elif QC == "P3":
                                    ProductList.insert(0,P3)
                                    Product_List.insert(0,P_3)
                                    Construction_List.insert(0,"P3")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    
                                    break
                                elif QC == "P4":
                                    ProductList.insert(0,P4)
                                    Product_List.insert(0,P_4)
                                    Construction_List.insert(0,"P4")
                                    task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
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
                                        BEAST[1] = task_sequence[i][1] #+ random.randint(-100,100)/100
                                        BEAST[2] = task_sequence[i][2] #+ random.randint(-100,100)/100
                                        #print("Robot location: ({},{})".format(BEAST[1],BEAST[2]))
                                        #print("----------------------------------------------------------")
                                    #print("time:", time.time()-a)
                                    break
                            #elif (BEAST[1] > 52.5) and (len(robot_items) > 0):


            #print("the robot is carrying: ", robot_items)