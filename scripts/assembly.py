#!/usr/bin/env python
import rospy as rp
from agv_as18.srv import *
import sys
from time import time
from std_msgs.msg import Int32
def fetch_cloud():
  try:
    resp = sp(ComponentsRequest())
    return resp.buffer
  except rp.ServiceException as e:
    print(e)

def set_cloud(buffer):
  try:
    sp(ComponentsRequest(1, buffer))
  except rp.ServiceException as e:
    print(e)

rp.wait_for_service('components')
sp = rp.ServiceProxy('components', Components)

pub = rp.Publisher('product_assembled',Int32, queue_size=1)

rp.Subscriber('qc',Int32,qc_cb)

def qc_cb(data):
    global flag
    ProductList.insert(0,Products[data.data])
    flag = True



comps = ['C1','C2','C3','C4','C5','C6']

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
ProductList = [P1,P3,P2]

flag = False


# Every time the robot unloads in the assembly station, check if the first component in the Product List can be assembled
while not rp.is_shutdown():
    if len(ProductList)>0:
        tmp = []
        for p in ProductList[0]:
            tmp.append(p[0])

        C_storage = fetch_cloud()
        AS_storage = []
        for i in range(len(C_storage)):
            if C_storage[i]>0:
                AS_storage.extend(C_storage[i]*[comps[i]])
        #check if the storage components are enough to construct the next product and return the new storage quantities
        for component in tmp:
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
        if y:
            set_cloud(C_storage)
            a = time()

            global flag
            while not flag or time()-a < 15:
                pass
            if flag == True:
                flag = False
            else:
                pub.publish(Products.index(ProductList[0]))
                del ProductList[0]



