#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from std_msgs.msg import Float32MultiArray, Bool
from agv_as18.msg import Faulty
from agv_as18.srv import *

# global variables
task_sequence = []  # order of components to gather and the AS unloading
temp_task_sequence = []
path = []  # this is a list of all the waypoints the robot will need to take to complete the product list
robot_items = []  # contains a maximum of two components that the robot is carrying
flag = False # true if the length of the temp_task_sequence is not 0

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

# name of the components
components = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

# products defined by the components
P1 = [C1, C3, C4, C4]
P2 = [C2, C1, C5, C6]
P3 = [C3, C3, C5]
P4 = [C2, C3, C4]
Products = [P1, P2, P3, P4]

# products for which we need to bring components in order to start assemblying
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
ProductList = [P1,P3,P2]  # this is for testing only

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
    elif component == 'MWP1':
        return MWP1
    elif component == 'MWP2':
        return MWP2
    elif component == 'MWP3':
        return MWP3
    elif component == 'AS':
        return AS

def send_waypoints():
    msg = Float32MultiArray()
    if len(path) > 0:
        while 1:
            node = find_component(path[0])
            msg.data.append(node[1])
            msg.data.append(node[2])
            if path[0] == 'C1' or path[0] == 'C2' or path[0] == 'C3' or path[0] == 'C4' or path[0] == 'C5' or path[0] == 'C6' or path[0] == 'AS':
                del path[0]
                break
            del path[0]
        waypoint_pub.publish(msg)

def serialize_tasks(tasks):
    serial = []
    for el in tasks:
        # append the waypoints name to the serialized list
        serial.append(el[0])
    return serial

def request_new_path(seq):
    try:
        global path
        path = service_path(PathRequest(serialize_tasks(seq))).path
        # rp.loginfo(path)
        send_waypoints()
    except rp.ServiceException as e:
        print(e)

def fetch_cloud():
    try:
        return list(service_components(ComponentsRequest()).buffer)
    except rp.ServiceException as e:
        print(e)

def set_cloud(buffer):
    try:
        service_components(ComponentsRequest(1, buffer))
    except rp.ServiceException as e:
        print(e)

def pos_cb(data):
    global BEAST
    BEAST[1] = data.translation.x
    BEAST[2] = data.translation.y

def qc_cb(data):
    Quality_List = [component[0] for component in Products[data.product]]
    QualityList = [component for component in Products[data.product]]
    global task_sequence
    global temp_task_sequence
    global robot_items
    global path
    global flag
    # if we have enough components to start the assembly immediately
    if data.y:
        # If the robot is on the right side and is empty
        if (BEAST[2] < 166) and (len(robot_items) == 0):

            # insert the components of the faulty product in the beginning of the task sequence
            task_sequence = [QualityList[i]
                             for i in range(len(QualityList))] + task_sequence
            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
            # Every 2 components, the robot needs to go to the Assembly station
            z = 2
            while z < len(task_sequence):
                task_sequence.insert(z, AS)
                z += 3  
            task_sequence.append(AS)

        # if the robot is on the right side of the map and it carries one component
        elif (BEAST[2] < 166) and (len(robot_items) == 1):

            C_storage = fetch_cloud()
            # checking if there is space in the buffers
            if C_storage[components.index(robot_items[0])] < 3:
                temp_task_sequence = [AS]
                # insert the components of the faulty product in the beginning of the task sequence
                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))
                z = 2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)
                
            # if there is no space in the buffers
            else:
                # create a temporary task sequence for the robot to return the component for which there is no space
                temp_task_sequence = [find_component(robot_items[0])]
                # Add this component back in the task sequence
                task_sequence.insert(0, find_component(robot_items[0]))

                # insert the components of the faulty product in the beginning of the task sequence
                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))
                z = 2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

        # If the robot is on the right side and it carries exactly 2 items
        elif (BEAST[2] < 166) and (len(robot_items) == 2):
            C_storage = fetch_cloud()
            # If there is space in the buffers for the first component
            if C_storage[components.index(robot_items[0])] < 3:
                C_storage_check = list(C_storage)
                C_storage_check[components.index(robot_items[0])] += 1
                # and if there is space for the second component too
                if C_storage_check[components.index(robot_items[1])] < 3:
                    temp_task_sequence = [AS]
                    # insert the components of the faulty product in the beginning of the task sequence
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)
                    

                # If there is no space for the second component
                else:
                    # create a temporary task sequence, unload the first component in the Assembly and carry the second component back to the its station
                    temp_task_sequence = [AS, find_component(robot_items[1])]
                    # Add the component back to the task sequence
                    task_sequence.insert(0, find_component(robot_items[1]))
                    # insert the components of the faulty product in the beginning of the task sequence
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

            # if there is no space in the buffers for the first component
            else:
                # If there is space for the second one
                if C_storage_check[components.index(robot_items[1])] < 3:
                    # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                    temp_task_sequence = [AS, find_component(robot_items[0])]
                    task_sequence.insert(0, find_component(robot_items[0]))
                    # insert the components of the faulty product in the beginning of the task sequence
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

                # if there is no space for the second component either
                else:
                    temp_task_sequence = [find_component(
                        robot_items[0]), find_component(robot_items[1])]

                    task_sequence.insert(0, find_component(robot_items[0]))
                    task_sequence.insert(0, find_component(robot_items[1]))

                    # insert the components of the faulty product in the beginning of the task sequence
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)
        # robot is on the left side and carries no components
        elif (BEAST[2] > 166) and (len(robot_items) == 0):
            task_sequence = [QualityList[i]
                             for i in range(len(QualityList))] + task_sequence
            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))

            z = 2
            while z < len(task_sequence):
                task_sequence.insert(z, AS)
                z += 3
            task_sequence.append(AS)

        # robot is on the left side and carries one component
        elif (BEAST[2] > 166) and (len(robot_items) == 1):

            # if the component is part of the product that is assembled
            if robot_items[0] in Quality_List:

                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))

                z = 1
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

            # if the component is not part of the product assembled
            else:
                # create a temporary task sequence to return the product to its storage station
                temp_task_sequence = [find_component(robot_items[0])]
                task_sequence.insert(0, find_component(robot_items[0]))

                # insert the components of the faulty product in the beginning of the task sequence
                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))
                z = 2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

        # if the robot is on the left side and carries 2 components
        elif (BEAST[2] > 166) and (len(robot_items) == 2):
            # if the first component is part of the product which is assembled
            if robot_items[0] in Quality_List:
                Quality_List_check = list(Quality_List)
                Quality_List_check.remove(robot_items[0])
                # and if the second one is part of the product as well
                if robot_items[1] in Quality_List_check:
                    temp_task_sequence = [AS]
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))

                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)
                    
                    

                # if the second component is not part of the product
                else:
                    # put it back in its storage station
                    temp_task_sequence = [find_component(robot_items[1])]
                    task_sequence.insert(0, find_component(robot_items[1]))

                    # insert the components of the faulty product in the beginning of the task sequence
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 1
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

            # if both components that the robot carries are not part of the product that is assembled
            elif robot_items[0] not in Quality_List and robot_items[1] not in Quality_List:
                # put both back to their stations
                temp_task_sequence = [find_component(
                    robot_items[0]), find_component(robot_items[1])]

                task_sequence.insert(0, find_component(robot_items[0]))
                task_sequence.insert(0, find_component(robot_items[1]))

                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))

                z = 2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

            # if the first component is not part of the product and the second one is
            elif robot_items[0] not in Quality_List and robot_items[1] in Quality_List:
                # put the first one back to its station
                temp_task_sequence = [find_component(robot_items[0])]
                task_sequence.insert(0, find_component(robot_items[0]))

                # insert the components of the faulty product in the beginning of the task sequence
                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))
                z = 1
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

    # if we do not have enough components to restart assembly immediately
    else:
        # find which components are missing from the assembly station in order to start the reassembly
        C_storage = fetch_cloud()
        AS_storage = []
        for i in range(len(C_storage)):
            if C_storage[i] > 0:
                AS_storage.extend(C_storage[i]*[components[i]])
        components_not_stored = []

        AS_storage_check = list(AS_storage)
        for component in Quality_List:
            if component in AS_storage:
                AS_storage_check.remove(component)
            else:
                components_not_stored.append(component)

        # The robot is on the right side of the map and it does not carry anything
        if (BEAST[2] < 166) and (len(robot_items) == 0):

            # if only one component is missing
            if len(components_not_stored) == 1:
                    # put in the beginning of the list and recalculate the waypoint list
                Quality_List.insert(0, Quality_List.pop(
                    Quality_List.index(components_not_stored[0])))
                QualityList.insert(0, QualityList.pop(
                    QualityList.index(find_component(components_not_stored[0]))))
            # if more than one components are missing
            else:
                # put two of them in the beginning of the list and recalculate the waypoint list
                Quality_List.insert(0, Quality_List.pop(
                    Quality_List.index(components_not_stored[0])))
                Quality_List.insert(0, Quality_List.pop(
                    Quality_List.index(components_not_stored[1])))
                QualityList.insert(0, QualityList.pop(
                    QualityList.index(find_component(components_not_stored[0]))))
                QualityList.insert(0, QualityList.pop(
                    QualityList.index(find_component(components_not_stored[1]))))

            # insert the components of the faulty product in the beginning of the task sequence
            task_sequence = [QualityList[i]
                             for i in range(len(QualityList))] + task_sequence
            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
            z = 2
            while z < len(task_sequence):
                task_sequence.insert(z, AS)
                z += 3
            task_sequence.append(AS)

        # the robot is on the right side and it carries exactly one component (can happen only if it carries the last component for the last product)
        elif (BEAST[2] < 166) and (len(robot_items) == 1):
            # if there is space for the first component
            if C_storage[components.index(robot_items[0])] < 3:
                # if we need only one component
                temp_task_sequence = [AS]
                if len(components_not_stored) == 1:
                    # put in the beginning of the list and recalculate the waypoint list
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    QualityList.insert(0, QualityList.pop(
                        Quality_List.index(find_component(components_not_stored[0]))))
                # if we need 2 or more components
                else:
                    # put two of them in the beginning of the list and recalculate the waypoint list
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[1])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[1]))))

                    # insert the components of the faulty product in the beginning of the task sequence
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)
                    

            # if there is no space in the buffers
            else:
                # if the component is not needed for the faulty product
                if robot_items[0] not in Quality_List:
                    # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                    temp_task_sequence = [find_component(robot_items[0])]
                    task_sequence.insert(0, find_component(robot_items[0]))

                    # if only one component is missing
                    if len(components_not_stored) == 1:
                        # put in the beginning of the list and recalculate the waypoint list
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                    # if more than one components are missing
                    else:
                        # add 2 of them in the beginning of the list and recalculate the waypoint list
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))

                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

                # if the component is needed for the assembly of the faulty component
                elif robot_items[0] in Quality_List:

                    # if only one component is missing
                    if len(components_not_stored) == 1:
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                        # insert the components of the faulty product in the beginning of the task sequence
                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 1
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

                    # if we are missing more than one components
                    else:
                        # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                        temp_task_sequence = [find_component(robot_items[0])]
                        task_sequence.insert(0, find_component(robot_items[0]))

                        # add 2 of them in the beginning of the list and recalculate the waypoint list
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 2
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

        # If the robot is on the right side and it carries exactly 2 components
        elif (BEAST[2] < 166) and (len(robot_items) == 2):

            # If there is space in the buffers for the first component
            if C_storage[components.index(robot_items[0])] < 3:
                C_storage_check = list(C_storage)
                C_storage_check[components.index(robot_items[0])] += 1
                # and if there is space for the second component too
                if C_storage_check[components.index(robot_items[1])] < 3:

                    if len(components_not_stored) == 1:
                            # put in the beginning of the list and recalculate the waypoint list
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                    else:
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                    # insert the components of the faulty product in the beginning of the task sequence
                    temp_task_sequence = [AS]
                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))
                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)
                    

                # if there is no space for the second component
                else:

                    if robot_items[1] not in Quality_List:
                        # create a temporary task sequence and find the fastest path to carry the component back to the storage station
                        temp_task_sequence = [
                            AS, find_component(robot_items[1])]
                        task_sequence.insert(0,find_component(robot_items[1]))

                        # if only one is needed
                        if len(components_not_stored) == 1:

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))                  

                        # if more than one components are needed
                        else:

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 2
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

                    # if the second component is part of the faulty component
                    elif robot_items[1] in Quality_List:
                        # if 1 component is missing
                        if len(components_not_stored) == 1:
                            temp_task_sequence = [AS]
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 1
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                            

                        # if 2 or more components are missing
                        else:
                            # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                            temp_task_sequence = [
                                AS, find_component(robot_items[1])]
                            task_sequence.insert(
                                0, find_component(robot_items[1]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 2
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)

            # if there is no space for the first component and there is space for the second one
            elif C_storage[components.index(robot_items[0])] >= 3 and C_storage[components.index(robot_items[1])] < 3:

                    # if the component for which there is no space is not needed for the faulty product
                if robot_items[0] not in Quality_List:
                    # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                    temp_task_sequence = [AS, find_component(robot_items[0])]
                    task_sequence.insert(0, find_component(robot_items[0]))

                    # if only one component is needed
                    if len(components_not_stored) == 1:

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                    # if 2 or more components are needed
                    else:
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                    task_sequence = [QualityList[i] for i in range(
                        len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))

                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

                # if the component is needed for the assembly of the faulty component
                elif robot_items[0] in Quality_List:

                    if len(components_not_stored) == 1:
                        temp_task_sequence = [AS]
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 1
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)
                        
                    # 2 or more components are missing
                    else:
                        # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                        temp_task_sequence = [
                            AS, find_component(robot_items[0])]
                        task_sequence.insert(0, find_component(robot_items[0]))

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 2
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

            # if there is no space for both components
            elif C_storage[components.index(robot_items[0])] >= 3 and C_storage[components.index(robot_items[1])] >= 3:
                # If both components are not part of the faulty product return them to their stations
                if robot_items[0] not in Quality_List and robot_items[1] not in Quality_List:
                    temp_task_sequence = [find_component(
                        robot_items[0]), find_component(robot_items[1])]
                    task_sequence.insert(0, find_component(robot_items[0]))
                    task_sequence.insert(0, find_component(robot_items[1]))

                    # if we are missing one component
                    if len(components_not_stored) == 1:
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                    # If we are missing 2 or more components
                    elif len(components_not_stored) == 2:
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))

                    z = 2
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

                # if the first component is not part of the faulty product and the second one is
                elif robot_items[0] not in Quality_List and robot_items[1] in Quality_List:
                    # if we are missing 1 component
                    if len(components_not_stored) == 1:
                        temp_task_sequence = [find_component(robot_items[0])]
                        task_sequence.insert(0, find_component(robot_items[0]))

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 1
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)
                    # if we are missing 2 or more
                    else:
                        temp_task_sequence = [find_component(
                            robot_items[0]), find_component(robot_items[1])]
                        task_sequence.insert(0, find_component(robot_items[0]))
                        task_sequence.insert(0, find_component(robot_items[1]))

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 2
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

                # if the first component is part of the faulty product
                elif robot_items[0] in Quality_List:
                    Quality_List_check = list(Quality_List)
                    Quality_List_check.remove(robot_items[0])
                    # if the second one is also part of the faulty product
                    if robot_items[1] in Quality_List_check:
                        # if only 1 component is missing
                        if len(components_not_stored) == 1:

                            temp_task_sequence = [
                                find_component(robot_items[0])]
                            task_sequence.insert(0,
                                find_component(robot_items[0]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 1
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                        # if two or more components are missing
                        else:
                            temp_task_sequence = [find_component(
                                robot_items[0]), find_component(robot_items[1])]
                            task_sequence.insert(
                                0, find_component(robot_items[0]))
                            task_sequence.insert(
                                0, find_component(robot_items[1]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 2
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                    # if the first component is part of the faulty product and the second one is not
                    else:
                        # if we are missing 1 component
                        if len(components_not_stored) == 1:
                            temp_task_sequence = [
                                find_component(robot_items[1])]
                            task_sequence.insert(
                                0, find_component(robot_items[1]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 1
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                        # if 2 or more are missing
                        else:

                            temp_task_sequence = [find_component(
                                robot_items[0]), find_component(robot_items[1])]
                            task_sequence.insert(
                                0, find_component(robot_items[0]))
                            task_sequence.insert(
                                0, find_component(robot_items[1]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 2
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)

        # if the robot is on the left side and is empty
        elif (BEAST[2] > 166) and (len(robot_items) == 0):
            # if 1 component is missing
            if len(components_not_stored) == 1:
                Quality_List.insert(0, Quality_List.pop(
                    Quality_List.index(components_not_stored[0])))
                QualityList.insert(0, QualityList.pop(
                    QualityList.index(find_component(components_not_stored[0]))))
            # if 2 or more components are missing
            else:
                Quality_List.insert(0, Quality_List.pop(
                    Quality_List.index(components_not_stored[0])))
                Quality_List.insert(0, Quality_List.pop(
                    Quality_List.index(components_not_stored[1])))
                QualityList.insert(0, QualityList.pop(
                    QualityList.index(find_component(components_not_stored[0]))))
                QualityList.insert(0, QualityList.pop(
                    QualityList.index(find_component(components_not_stored[1]))))

            task_sequence = [QualityList[i]
                             for i in range(len(QualityList))] + task_sequence
            task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))

            z = 2
            while z < len(task_sequence):
                task_sequence.insert(z, AS)
                z += 3
            task_sequence.append(AS)

        # if the robot is on the left side and carries 1 component
        elif (BEAST[2] > 166) and (len(robot_items) == 1):

            # if the component is not part of the faulty product
            if robot_items[0] not in Quality_List:
                temp_task_sequence = [find_component(robot_items[0])]
                task_sequence.insert(0, find_component(robot_items[0]))

                # if 1 component is missing
                if len(components_not_stored) == 1:
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))
                # if 2 or more components are missing
                else:
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[1])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[1]))))

                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))

                z = 2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

            # if the component is part of faulty the product
            elif robot_items[0] in Quality_List:

                # if 1 component is missing
                if len(components_not_stored) == 1:
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))

                    task_sequence = [(QualityList)[i] for i in range(
                        len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))

                    z = 1
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)

                # if 2 or more components are missing
                else:
                    # if the component we are carrying is not one of the components we are missing
                    if robot_items[0] not in components_not_stored:

                        temp_task_sequence = [find_component(robot_items[0])]
                        task_sequence.insert(0,find_component(robot_items[0]))

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 2
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)
                    # if the component we are carrying is one of the components that are missing
                    else:
                        components_not_stored.append(components_not_stored.pop(
                            components_not_stored.index(robot_items[0])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 1
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

        # if the robot is on the left side and it carries 2 components
        elif (BEAST[2] > 166) and (len(robot_items) == 2):

            # if both components are not part of the faulty product
            if robot_items[0] not in Quality_List and robot_items[1] not in Quality_List:
                temp_task_sequence = [find_component(
                    robot_items[0]), find_component(robot_items[1])]

                task_sequence.insert(0, find_component(robot_items[0]))
                task_sequence.insert(0, find_component(robot_items[1]))

                # if we are missing 1 component
                if len(components_not_stored) == 1:
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))

                # if we are missing two or more components
                else:
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[1])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[1]))))

                task_sequence = [QualityList[i]
                                 for i in range(len(QualityList))] + task_sequence
                task_sequence = list(
                    filter(lambda a: a[0] != 'AS', task_sequence))

                z = 2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)

            # if the first component is not part of the faulty product and the second one is
            elif robot_items[0] not in Quality_List and robot_items[1] in Quality_List:
                # if we are missing 1 component
                if len(components_not_stored) == 1:
                    temp_task_sequence = [find_component(robot_items[0])]
                    task_sequence.insert(0,find_component(robot_items[0]))

                    Quality_List.insert(0, Quality_List.pop(
                        Quality_List.index(components_not_stored[0])))
                    QualityList.insert(0, QualityList.pop(
                        QualityList.index(find_component(components_not_stored[0]))))

                    task_sequence = [QualityList[i]
                                     for i in range(len(QualityList))] + task_sequence
                    task_sequence = list(
                        filter(lambda a: a[0] != 'AS', task_sequence))

                    z = 1
                    while z < len(task_sequence):
                        task_sequence.insert(z, AS)
                        z += 3
                    task_sequence.append(AS)
                # if 2 or more components are missing
                else:
                    # if the second component is not one of the misiing ones
                    if robot_items[1] not in components_not_stored:
                        temp_task_sequence = [find_component(
                            robot_items[0]), find_component(robot_items[1])]
                        task_sequence.insert(0,find_component(robot_items[0]))
                        task_sequence.insert(0,find_component(robot_items[1]))

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 2
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)
                    # if the second component is one of the missing ones
                    else:
                        temp_task_sequence = [find_component(robot_items[0])]
                        task_sequence.insert(0,find_component(robot_items[0]))
                        components_not_stored.append(components_not_stored.pop(
                            components_not_stored.index(robot_items[1])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[1])))
                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[1]))))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 1
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)

            # if the first component is part of the faulty product
            elif robot_items[0] in Quality_List:
                Quality_List_check = list(Quality_List)
                Quality_List_check.remove(robot_items[0])
                # if the second one is also part of the faulty product
                if robot_items[1] in Quality_List_check:
                    # if we are missing 1 component
                    if len(components_not_stored) == 1:
                        # if both components are not the one missing from the assembly
                        if robot_items[0] not in components_not_stored and robot_items[1] not in components_not_stored:
                            temp_task_sequence = [
                                find_component(robot_items[0])]
                            task_sequence.insert(0,
                                find_component(robot_items[0]))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 1
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                        # if one of them is one of the components missing
                        else:
                            temp_task_sequence = [AS]
                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 2
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                           

                    # if 2 or more components are missing
                    else:
                        # if both components are not the ones missing
                        if robot_items[0] not in components_not_stored and robot_items[1] not in components_not_stored:
                            temp_task_sequence = [find_component(
                                robot_items[0]), find_component(robot_items[1])]
                            task_sequence.insert(0,
                                find_component(robot_items[0]))
                            task_sequence.insert(0,
                                find_component(robot_items[1]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 2
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                        # if the second one is one of the missing ones
                        elif robot_items[0] not in components_not_stored and robot_items[1] in components_not_stored:
                            temp_task_sequence = [
                                find_component(robot_items[0])]
                            task_sequence.insert(
                                0, find_component(robot_items[0]))
                            components_not_stored.append(components_not_stored.pop(
                                components_not_stored.index(robot_items[1])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 1
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                        # if the first one is one of the missing ones
                        elif robot_items[0] in components_not_stored:
                            components_not_stored_check = list(
                                components_not_stored)
                            components_not_stored_check.remove(robot_items[0])
                            if robot_items[1] not in components_not_stored_check:
                                temp_task_sequence = [
                                    find_component(robot_items[1])]
                                task_sequence.insert(
                                    0, find_component(robot_items[1]))

                                components_not_stored.append(components_not_stored.pop(
                                    components_not_stored.index(robot_items[0])))
                                Quality_List.insert(0, Quality_List.pop(
                                    Quality_List.index(components_not_stored[0])))
                                Quality_List.insert(0, Quality_List.pop(
                                    Quality_List.index(components_not_stored[1])))
                                QualityList.insert(0, QualityList.pop(
                                    QualityList.index(find_component(components_not_stored[0]))))
                                QualityList.insert(0, QualityList.pop(
                                    QualityList.index(find_component(components_not_stored[1]))))

                                task_sequence = [QualityList[i] for i in range(
                                    len(QualityList))] + task_sequence
                                task_sequence = list(
                                    filter(lambda a: a[0] != 'AS', task_sequence))

                                z = 1
                                while z < len(task_sequence):
                                    task_sequence.insert(z, AS)
                                    z += 3
                                task_sequence.append(AS)
                            # if both of them are missing
                            elif robot_items[1] in components_not_stored_check:
                                temp_task_sequence = [AS]
                                components_not_stored.append(components_not_stored.pop(
                                    components_not_stored.index(robot_items[0])))
                                components_not_stored.append(components_not_stored.pop(
                                    components_not_stored.index(robot_items[1])))
                                Quality_List.insert(0, Quality_List.pop(
                                    Quality_List.index(components_not_stored[0])))
                                Quality_List.insert(0, Quality_List.pop(
                                    Quality_List.index(components_not_stored[1])))
                                QualityList.insert(0, QualityList.pop(
                                    QualityList.index(find_component(components_not_stored[0]))))
                                QualityList.insert(0, QualityList.pop(
                                    QualityList.index(find_component(components_not_stored[1]))))

                                task_sequence = [QualityList[i] for i in range(
                                    len(QualityList))] + task_sequence
                                task_sequence = list(
                                    filter(lambda a: a[0] != 'AS', task_sequence))

                                z = 2
                                while z < len(task_sequence):
                                    task_sequence.insert(z, AS)
                                    z += 3
                                task_sequence.append(AS)

                # if the second one is not part of the faulty product
                else:
                    # if we are missing 1 component
                    if len(components_not_stored) == 1:
                        temp_task_sequence = [find_component(robot_items[1])]
                        task_sequence.insert(0,find_component(robot_items[1]))

                        Quality_List.insert(0, Quality_List.pop(
                            Quality_List.index(components_not_stored[0])))
                        QualityList.insert(0, QualityList.pop(
                            QualityList.index(find_component(components_not_stored[0]))))

                        task_sequence = [QualityList[i] for i in range(
                            len(QualityList))] + task_sequence
                        task_sequence = list(
                            filter(lambda a: a[0] != 'AS', task_sequence))

                        z = 1
                        while z < len(task_sequence):
                            task_sequence.insert(z, AS)
                            z += 3
                        task_sequence.append(AS)
                    # if 2 or more components are missing
                    else:
                        # if the first component is not one of the missing ones
                        if robot_items[0] not in components_not_stored:
                            temp_task_sequence = [find_component(
                                robot_items[0]), find_component(robot_items[1])]
                            task_sequence.insert(0,
                                find_component(robot_items[0]))
                            task_sequence.insert(0,
                                find_component(robot_items[1]))

                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 2
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)
                        # if the first component is one of the missing ones
                        else:
                            temp_task_sequence = [
                                find_component(robot_items[1])]
                            task_sequence.insert(
                                0, find_component(robot_items[1]))

                            components_not_stored.append(components_not_stored.pop(
                                components_not_stored.index(robot_items[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[0])))
                            Quality_List.insert(0, Quality_List.pop(
                                Quality_List.index(components_not_stored[1])))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[0]))))
                            QualityList.insert(0, QualityList.pop(
                                QualityList.index(find_component(components_not_stored[1]))))

                            task_sequence = [QualityList[i] for i in range(
                                len(QualityList))] + task_sequence
                            task_sequence = list(
                                filter(lambda a: a[0] != 'AS', task_sequence))

                            z = 1
                            while z < len(task_sequence):
                                task_sequence.insert(z, AS)
                                z += 3
                            task_sequence.append(AS)

    print('temp task seq {}'.format(temp_task_sequence))
    print('task seq {}'.format(task_sequence))
    if len(temp_task_sequence) == 0:
        request_new_path(task_sequence)
    else:
        flag = True
        request_new_path(temp_task_sequence)

def loading_cb(data):
    global robot_items
    global flag

    # if we are in a temporary task sequence situation (we need to unload components back to their stations)
    if flag:
        # if the waypoint is a component station, unload and delete the task from the task sequence
        if temp_task_sequence[0][0] == 'C1' or temp_task_sequence[0][0] == 'C2' or temp_task_sequence[0][0] == 'C3' or temp_task_sequence[0][0] == 'C4' or temp_task_sequence[0][0] == 'C5' or temp_task_sequence[0][0] == 'C6':
            robot_items.remove(temp_task_sequence[0][0])
            print("unloading: {}".format(temp_task_sequence[0][0]))
            del temp_task_sequence[0]
            rp.sleep(1)
        
        # if the waypoint is the assembly station, unload, delete the task, update the assembly storage and the quantities
        elif temp_task_sequence[0][0] == 'AS':
            del temp_task_sequence[0]
            tmp_robot_items = list(robot_items)
            for component in robot_items:
                C_storage = fetch_cloud()
                if C_storage[components.index(component)] < 3:
                    C_storage[components.index(component)] += 1
                    set_cloud(C_storage)
                    print("unloading: {}".format(component))
                    tmp_robot_items.remove(component)
                    rp.sleep(1)
            robot_items = list(tmp_robot_items)

        if len(temp_task_sequence) == 0:
                flag = False
                request_new_path(task_sequence)
        else:
            send_waypoints()

    # if the robot follows the official task sequence
    else:
        # if the waypoint is a component station, load and delete the task from the task sequence
        if task_sequence[0][0] == 'C1' or task_sequence[0][0] == 'C2' or task_sequence[0][0] == 'C3' or task_sequence[0][0] == 'C4' or task_sequence[0][0] == 'C5' or task_sequence[0][0] == 'C6':
            robot_items.append(task_sequence[0][0])
            print("loading: {}".format(task_sequence[0][0]))
            del task_sequence[0]
            rp.sleep(1)

        # if the waypoint is the assembly station, unload, delete the task, update the assembly storage and the quantities
        elif task_sequence[0][0] == 'AS':
            del task_sequence[0]
            while len(robot_items) != 0:
                C_storage = fetch_cloud()
                if C_storage[components.index(robot_items[0])] < 3:
                    C_storage[components.index(robot_items[0])] += 1
                    set_cloud(C_storage)
                    print("unloading: {}".format(robot_items[0]))
                    del robot_items[0]
                    rp.sleep(1)
                else: 
                    robot_items.append(robot_items.pop(0))

        send_waypoints()

rp.init_node('task_tracking')
rp.Subscriber('local_pos_ref', Transform, pos_cb)
rp.Subscriber('reassemble_check', Faulty, qc_cb)
rp.Subscriber('arrived_at_target', Bool, loading_cb)
waypoint_pub = rp.Publisher('nodes', Float32MultiArray, queue_size=1, latch=True)
rp.wait_for_service('components')
rp.wait_for_service('path_service')
service_components = rp.ServiceProxy('components', Components)
service_path = rp.ServiceProxy('path_service', Path)

# initial list containing the name and location of each destination the robot needs to go in order to take all the components needed and deliver them to the assembly
task_sequence = [(ProductList[i])[j] for i in range(len(ProductList)) for j in range(len(ProductList[i]))]
i = 2
while i < len(task_sequence):
    task_sequence.insert(i, AS)
    i += 3
task_sequence.append(AS)

request_new_path(task_sequence)

rp.spin()
