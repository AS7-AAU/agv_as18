#!/usr/bin/env python
import rospy as rp
from time import time
from agv_as18.srv import Components, ComponentsRequest, ComponentsResponse
from agv_as18.msg import Faulty
from std_msgs.msg import Int32


AS = ['AS',170.0,125.0]
C1 = ['C1',5.0,200.0]
C2 = ['C2',5.0,170.0]
C3 = ['C3',5.0,140.0]
C4 = ['C4',5.0,110.0]
C5 = ['C5',5.0,80.0]
C6 = ['C6',5.0,50.0]
P1 = [C1,C3,C4,C4]
P2 = [C1,C2,C5,C6]
P3 = [C3,C3,C5]
P4 = [C2,C3,C4]
Products = [P1,P2,P3,P4]
components = ['C1','C2','C3','C4','C5','C6']

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

flag = False

def buffer_check():
    tmp = []
    for p in ProductList[0]:
        tmp.append(p[0])

    print('tmp', tmp)

    C_storage = fetch_cloud()
    AS_storage = []
    for i in range(len(C_storage)):
        if C_storage[i]>0:
            AS_storage.extend(C_storage[i]*[components[i]])
    print('AS storage', AS_storage)
    #check if the storage components are enough to construct the next product and return the new storage quantities
    for component in tmp:
        print('component', component)
        if len(AS_storage) > 0:
            for component_ in AS_storage:
                if component == component_:
                    if component == 'C1':
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
    return y, C_storage

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

def qc_cb(data):
    global flag
    ProductList.insert(0,Products[data.data])
    y, _ = buffer_check()
    pub_2.publish(Faulty(data.data, y))
    flag = True

rp.init_node('assembly')
rp.wait_for_service('components')
print('components')
service_components = rp.ServiceProxy('components', Components)
rp.Subscriber('qc', Int32, qc_cb)
pub = rp.Publisher('product_assembled', Int32, queue_size=1)
pub_2 = rp.Publisher('reassemble_check', Faulty, queue_size=1)

# Every time the robot unloads in the assembly station, check if the first component in the Product List can be assembled
while not rp.is_shutdown():
    if len(ProductList)>0:
        y, C_storage = buffer_check()
        if y:
            set_cloud(C_storage)
            a = time()

            global flag
            print(flag)
            while not flag and time()-a < 15:
                pass

            if flag == True:
                C_storage = fetch_cloud()
                for component in ProductList[0]:
                    if component[0] == 'C1':
                        C_storage[0] +=1
                    elif component[0] == 'C2':
                        C_storage[1] +=1
                    elif component[0] == 'C3':
                        C_storage[2] +=1
                    elif component[0] == 'C4':
                        C_storage[3] +=1
                    elif component[0] == 'C5':
                        C_storage[4] +=1
                    elif component[0] == 'C6':
                        C_storage[5] +=1
                set_cloud(C_storage)
                flag = False
            else:
                pub.publish(Products.index(ProductList[0]))
                del ProductList[0]



