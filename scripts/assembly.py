#!/usr/bin/env python
import rospy as rp
from time import time
from agv_as18.srv import Components, ComponentsRequest, ComponentsResponse
from agv_as18.msg import Faulty
from std_msgs.msg import Int32

AS = ['AS',125.0,66.0]
C1 = ['C1',200.0,210.0]
C2 = ['C2',170.0,210.0]
C3 = ['C3',140.0,210.0]
C4 = ['C4',110.0,210.0]
C5 = ['C5',80.0,210.0]
C6 = ['C6',50.0,210.0]

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
    '''check if the storage components are enough to construct the next product and return the new storage quantities'''
    C_storage = fetch_cloud()
    for component in ProductList[0]:
        y = False
        if C_storage[components.index(component[0])] > 0:
            y = True
            C_storage[components.index(component[0])] -= 1
        print(C_storage, y)
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
    flag = True
    ProductList.insert(0,Products[data.data])
    y, _ = buffer_check()
    reassembly_pub.publish(Faulty(data.data, y))

rp.init_node('assembly')
rp.wait_for_service('components')
service_components = rp.ServiceProxy('components', Components)
rp.Subscriber('qc', Int32, qc_cb)
assembled_pub = rp.Publisher('product_assembled', Int32, queue_size=1)
reassembly_pub = rp.Publisher('reassemble_check', Faulty, queue_size=1)

while not rp.is_shutdown():
    if len(ProductList)>0:
        y, C_storage = buffer_check()
        if y:
            set_cloud(C_storage)
            a = time()
            global flag
            rp.loginfo('assemblying: P'+str(Products.index(ProductList[0])+1))
            while not flag and time()-a < 15:
                pass

            if flag == True:
                rp.loginfo('stopped: P'+str(Products.index(ProductList[0])+1))
                C_storage = fetch_cloud()
                for component in ProductList[0]:
                    C_storage[components.index(component[0])] += 1
                set_cloud(C_storage)
                flag = False
            else:
                rp.loginfo('assembled: P'+str(Products.index(ProductList[0])+1))
                assembled_pub.publish(Products.index(ProductList[0]))
                del ProductList[0]
