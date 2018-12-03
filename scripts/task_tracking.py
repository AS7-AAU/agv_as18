#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from agv_as18.msg import Waypoints, Task, Faulty
from agv_as18.srv import *

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


P1 = [C1,C3,C4,C4]
P2 = [C1,C2,C5,C6]
P3 = [C3,C3,C5]
P4 = [C2,C3,C4]

Products = [P1,P2,P3,P4]



components = ['C1','C2','C3','C4','C5','C6'] 

task_sequence=[]
b=[]
buffer=[]
robot_items=[]

def pos_cb(data):
  global BEAST
  BEAST[1]=data.translation.x
  BEAST[2]=data.translation.y

def waypoints_cb(data):
  global task_sequence
  global b
  task_sequence = []
  b = []

  b = data.b
  for task in data.task_seq:
    el = []
    el.append(task.name)
    el.append(task.x)
    el.append(task.y)
    task_sequence.append(el)

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

rp.init_node('task_tracking')
rp.Subscriber('local_pos_ref', Transform, pos_cb)
rp.Subscriber('waypoints', Waypoints, waypoints_cb)
#waypoint_pub = rp.Publisher('', , queue_size=1)
rp.wait_for_service('components')
sp = rp.ServiceProxy('components', Components)
rp.Subscriber('reassemble_check',Faulty,qc_cb)

def qc_cb(data):
  Quality_List = [component[0] for component in Products[data.product]]
  QualityList = [component for component in Products[data.product]]
  global task_sequence
  global robot_items
  if data.y:
    if (BEAST[1] > 52.5) and (len(robot_items) == 0):

      # insert the components of the faulty product in the beginning of the task sequence 
      task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
      task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
      z=2
      while z < len(task_sequence):
          task_sequence.insert(z, AS)
          z += 3
      task_sequence.append(AS)

    # if the robot is on the right side of the map and it carries one component
    elif (BEAST[1] > 52.5) and (len(robot_items) == 1):

      C_storage = fetch_cloud()    
      # checking if there is space in the buffers
      if C_storage[components.index(robot_items[0])]<3:
        
        # insert the components of the faulty product in the beginning of the task sequence 
        task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
        z=2
        while z < len(task_sequence):
            task_sequence.insert(z, AS)
            z += 3
        task_sequence.append(AS)
        task_sequence.insert(0,AS)
      # if there is no space in the buffers         
      else:
        # create a temporary task sequence for the robot to return the component for which there is no space
        temp_task_sequence = [find_component(robot_items[0])]

        # insert the components of the faulty product in the beginning of the task sequence 
        task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
        z=2
        while z < len(task_sequence):
            task_sequence.insert(z, AS)
            z += 3
        task_sequence.append(AS)

          

    # If the robot is on the right side and it carries exactly 2 items
    elif (BEAST[1] > 52.5) and (len(robot_items) == 2):
      C_storage = fetch_cloud()
      # If there is space in the buffers for the first component
      if C_storage[components.index(robot_items[0])]<3:
        C_storage_check = list(C_storage)
        C_storage_check[components.index(robot_items[0])]+=1
        # and if there is space for the second component too
        if C_storage_check[components.index(robot_items[1])]<3:
            
          # insert the components of the faulty product in the beginning of the task sequence
          task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
          task_sequence.insert(0,AS)
              
        # If there is no space for the second component        
        else:     
          # create a temporary task sequence and find the fastest path to carry the component back to the storage station
          temp_task_sequence = [AS,find_component(robot_items[1])]
          task_sequence.insert(0,find_component(robot_items[1]))
          # insert the components of the faulty product in the beginning of the task sequence
          task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)

      
      # if there is no space in the buffers for the first component            
      else:
        # If there is space for the second one
        if C_storage_check[components.index(robot_items[1])]<3:
          # create a temporary task sequence and find the fastest path to carry the component back to the storage station
          temp_task_sequence = [AS,find_component(robot_items[0])]
          task_sequence.insert(0,find_component(robot_items[0]))
          # insert the components of the faulty product in the beginning of the task sequence
          task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)

              
        # if there is no space for the second component either
        else:
          temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
          
          task_sequence.insert(0,find_component(robot_items[0]))
          task_sequence.insert(0,find_component(robot_items[1]))
      
          # insert the components of the faulty product in the beginning of the task sequence
          task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
    # robot is in the left side and carries no components
    elif  (BEAST[1] < 52.5) and (len(robot_items) == 0):
      task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
      task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
      
      z=2
      while z < len(task_sequence):
          task_sequence.insert(z, AS)
          z += 3
      task_sequence.append(AS)
        
    # robot is in the left side and carries one component
    elif  (BEAST[1] < 52.5) and (len(robot_items) == 1):
      
      # if the component is part of the product that is assembled
      if robot_items[0] in [component[0] for component in Products[data.product]]:
      
        task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
        
        z=1
        while z < len(task_sequence):
            task_sequence.insert(z, AS)
            z += 3
        task_sequence.append(AS)
          
      # if the component is not part of the product assembled 
      else:
        #create a temporary task sequence to return the product to its storage station
        temp_task_sequence = [find_component(robot_items[0])]
        task_sequence.insert(0,find_component(robot_items[0]))

        # insert the components of the faulty product in the beginning of the task sequence 
        task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
        z=2
        while z < len(task_sequence):
            task_sequence.insert(z, AS)
            z += 3
        task_sequence.append(AS)

    # if the robot is on the left side and carries 2 components
    elif  (BEAST[1] < 52.5) and (len(robot_items) == 2):
      # if the first component is part of the product which is assembled
      if robot_items[0] in Quality_List:
        Quality_List_check = list(Quality_List)
        Quality_List_check.remove(robot_items[0])
        # and if the second one is part of the product as well
        if robot_items[1] in Quality_List_check:
            
          task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
            
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
          # the first task would be to bring the products that the robot carries to the assembly station
          task_sequence.insert(0,AS)
            
        # if the second component is not part of the product
        else:
          #put it back in its storage station
          temp_task_sequence = [find_component(robot_items[1])]
          task_sequence.insert(0,find_component(robot_items[1]))
          
          # insert the components of the faulty product in the beginning of the task sequence 
          task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          z=1
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)

      # if both components that the robot carries are not part of the product that is assembled
      elif robot_items[0] not in Quality_List and robot_items[1] not in Quality_List:
        # put both back to their stations
        temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
        
        task_sequence.insert(0,find_component(robot_items[0]))
        task_sequence.insert(0,find_component(robot_items[1]))
        
        task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
        
        z=2
        while z < len(task_sequence):
            task_sequence.insert(z, AS)
            z += 3
        task_sequence.append(AS)
          
          
      # if the first component is not part of the product and the second one is
      elif robot_items[0] not in Quality_List and robot_items[1] in Quality_List:
        # put the first one back to its station
        temp_task_sequence = [find_component(robot_items[0])]
        task_sequence.insert(0,find_component(robot_items[0]))
      
        # insert the components of the faulty product in the beginning of the task sequence 
        task_sequence = [(Products[data.product])[i] for i in range(len(Products[data.product]))] + task_sequence
        task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
        z=1
        while z < len(task_sequence):
            task_sequence.insert(z, AS)
            z += 3
        task_sequence.append(AS)

  # if we do not have enough components to restart assembly immediately
  else:
    # The robot is on the right side of the map and it does not carry anything
    if (BEAST[1] > 52.5) and (len(robot_items) == 0):
      # find which components are missing from the assembly station in order to start the reassembly
      C_storage = fetch_cloud()
      AS_storage = []
      for i in range(len(C_storage)):
        if C_storage[i]>0:
          AS_storage.extend(C_storage[i]*[components[i]])

      components_not_stored = []
      components_stored = []
      AS_storage_check = list(AS_storage)
      for component in Quality_List:
        if component in AS_storage:
          components_stored.append(component)
          AS_storage_check.remove(component)
        else:
          components_not_stored.append(component)
      # if only one component is missing
      if len(components_not_stored) == 1:
          # put in the beginning of the list and recalculate the waypoint list
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
      # if more than one components are missing
      else:
          # put two of them in the beginning of the list and recalculate the waypoint list
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))

      # insert the components of the faulty product in the beginning of the task sequence 
      task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
      task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
      z=2
      while z < len(task_sequence):
          task_sequence.insert(z, AS)
          z += 3
      task_sequence.append(AS)

    # the robot is in the right side and it carries exactly one item (can happen only if it carries the last component for the last product)
    elif (BEAST[1] > 52.5) and (len(robot_items) == 1):
      C_storage = fetch_cloud()
      # checking if there is space in the buffers
      AS_storage = []
      for i in range(len(C_storage)):
        if C_storage[i]>0:
          AS_storage.extend(C_storage[i]*[components[i]])

      if C_storage[components.index(robot_items[0])]<3:
          
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
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
          QualityList.insert(0, QualityList.pop(Quality_List.index(find_component(components_not_stored[0]))))
        else:
          # put two of them in the beginning of the list and recalculate the waypoint list
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))

          # insert the components of the faulty product in the beginning of the task sequence
          task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
          task_sequence.insert(0,AS)

      # if there is no space in the buffers
      else :
          # if the component is not needed for the faulty product
          if robot_items[0] not in Quality_List:
            # create a temporary task sequence and find the fastest path to carry the component back to the storage station
            temp_task_sequence = [find_component(robot_items[0])]
            task_sequence.insert(0,find_component(robot_items[0]))
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
              # put in the beginning of the list and recalculate the waypoint list
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              
              
              
              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=2
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
                  
            # if more than one components are missing
            else:
              # add 2 of them in the beginning of the list and recalculate the waypoint list
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
              
              
              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=2
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
                  
              
          # if the component is needed for the assembly of the faulty component
          elif robot_items[0] in Quality_List:
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
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              
              # insert the components of the faulty product in the beginning of the task sequence
              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=1
              while z < len(task_sequence):
                task_sequence.insert(z, AS)
                z += 3
              task_sequence.append(AS)

            # if we are missing more than one components
            else:
              # create a temporary task sequence and find the fastest path to carry the component back to the storage station
              temp_task_sequence = [find_component(robot_items[0])]
              task_sequence.insert(0,find_component(robot_items[0]))

              # add 2 of them in the beginning of the list and recalculate the waypoint list
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
              
              task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=2
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
                  

    # If the robot is on the right side and it carries exactly 2 items
    elif (BEAST[1] > 52.5) and (len(robot_items) == 2):
      C_storage = fetch_cloud()
      # checking if there is space in the buffers
      AS_storage = []
      for i in range(len(C_storage)):
        if C_storage[i]>0:
          AS_storage.extend(C_storage[i]*[components[i]])

      # If there is space in the buffers for the first component
      if C_storage[components.index(robot_items[0])]<3:
        C_storage_check = list(C_storage)
        C_storage_check[components.index(robot_items[0])]+=1
        # and if there is space for the second component too
        if C_storage_check[components.index(robot_items[1])]<3:
            


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
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              else:
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List[0].insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList[0].insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList[0].insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))

              # insert the components of the faulty product in the beginning of the task sequence
              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              z=2
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
              task_sequence.insert(0,AS)

        # if there is no space for the second component
        else:
            
          if robot_items[0] not in Quality_List[0]:
              # create a temporary task sequence and find the fastest path to carry the component back to the storage station
              temp_task_sequence = [AS,find_component(robot_items[0])]
              task_sequence.insert(find_component(robot_items[0]))
            
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
                  
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  
                  
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
              # if more than one components are needed
              else:
                  b=[]
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
              
                          
      # if there is no space for the first component and there is space for the second one
      elif C_storage[components.index(robot_items[0])]>=3 and C_storage[components.index(robot_items[1])]<3:

          # if the component for which there is no space is not needed for the faulty product
          if robot_items[0] not in Quality_List[0]:
            # create a temporary task sequence and find the fastest path to carry the component back to its storage station
            temp_task_sequence = [AS,find_component(robot_items[0])]
            task_sequence.insert(0,find_component(robot_items[0]))
             
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
                
                Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                
                
                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                
                z=2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)


            # if 2 or more components are needed
            else:
                Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                
                task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                
                z=2
                while z < len(task_sequence):
                    task_sequence.insert(z, AS)
                    z += 3
                task_sequence.append(AS)
                  
              
          # if the component is needed for the assembly of the faulty component
          elif robot_items[0] in Quality_List:

              components_not_stored = []
              components_stored = []
              for component in Quality_List[0]:
                  if component in AS_storage:
                      components_stored.append(component)
                  else:
                      components_not_stored.append(component)

              if len(components_not_stored) == 1:
                  
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  
                  
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=1
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  

              else:
                  # create a temporary task sequence and find the fastest path to carry the component back to its storage station
                  temp_task_sequence = [find_component(robot_items[0])]
                  task_sequence.insert(0,find_component(robot_items[0]))
          
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
      elif C_storage[components.index(robot_items[0])]>=3 and C_storage[components.index(robot_items[1])]>=3:
          if robot_items[0] not in Quality_List and robot_items[1] not in Quality_List:
              temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
              task_sequence.insert(0,find_component(robot_items[0]))
              task_sequence.insert(0,find_component(robot_items[1]))

              components_not_stored = []
              components_stored = []
              for component in Quality_List:
                  if component in AS_storage:
                      components_stored.append(component)
                  else:
                      components_not_stored.append(component)
              
              if len(components_not_stored) == 1:
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  
                  task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  

              elif len(components_not_stored) == 2:
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
              

          elif robot_items[0] not in Quality_List[0] and robot_items[1] in Quality_List[0]:
              temp_task_sequence = [find_component(robot_items[0])]
              task_sequence.insert(0,find_component(robot_items[0]))

              components_not_stored = []
              components_stored = []
              for component in Quality_List:
                  if component in AS_storage:
                      components_stored.append(component)
                  else:
                      components_not_stored.append(component)
              if  len(components_not_stored) == 1:
                  Quality_List[0].insert(0, Quality_List[0].pop(Quality_List[0].index(components_not_stored[0])))
                  QualityList[0].insert(0, QualityList[0].pop(QualityList[0].index(find_component(components_not_stored[0]))))
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=1
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
              else:
                  temp_task_sequence = [find_component(robot_items[0])]
                  task_sequence.insert(0,find_component(robot_items[0]))
                  
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                  
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
          
          elif robot_items[0] in Quality_List and robot_items[1] not in Quality_List:
              temp_task_sequence = [find_component(robot_items[1])]
              task_sequence.insert(0,find_component(robot_items[1]))

              b=[]
              components_not_stored = []
              components_stored = []
              for component in Quality_List:
                  if component in AS_storage:
                      components_stored.append(component)
                  else:
                      components_not_stored.append(component)

              if  len(components_not_stored) == 1:
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  
                  
         
                  task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=1
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
              else:
                  
                  temp_task_sequence = [find_component(robot_items[0])]
                  task_sequence.insert(0,find_component(robot_items[0]))
                
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                  

                  task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
          
          elif robot_items[0] in Quality_List and robot_items[1] in Quality_List:
              components_not_stored = []
              components_stored = []
              for component in Quality_List:
                  if component in AS_storage:
                      components_stored.append(component)
                  else:
                      components_not_stored.append(component)
              if len(components_not_stored)==1:
                  
                  temp_task_sequence = [find_component(robot_items[0])]
                  task_sequence.insert(find_component(robot_items[0]))
                  

                  

                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  
                  
                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=1
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
              else:
                  temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
                  task_sequence.insert(0,find_component(robot_items[0]))
                  task_sequence.insert(0,find_component(robot_items[1]))
                 
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
                  Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
                  QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
                  

                  task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
                  task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
                  
                  z=2
                  while z < len(task_sequence):
                      task_sequence.insert(z, AS)
                      z += 3
                  task_sequence.append(AS)
                  
    elif  (BEAST[1] < 52.5) and (len(robot_items) == 0):
      C_storage = fetch_cloud()
      # checking if there is space in the buffers
      AS_storage = []
      for i in range(len(C_storage)):
        if C_storage[i]>0:
          AS_storage.extend(C_storage[i]*[components[i]])

      components_not_stored = []
      components_stored = []
      for component in Quality_List[0]:
          if component in AS_storage:
              components_stored.append(component)
          else:
              components_not_stored.append(component)

      if len(components_not_stored) ==1:
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))

      else:
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
          Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
          QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))


      task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
      task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
      
      z=2
      while z < len(task_sequence):
          task_sequence.insert(z, AS)
          z += 3
      task_sequence.append(AS)
     
    elif (BEAST[1] < 52.5) and (len(robot_items) == 1):
      C_storage = fetch_cloud()
      # checking if there is space in the buffers
      AS_storage = []
      for i in range(len(C_storage)):
        if C_storage[i]>0:
          AS_storage.extend(C_storage[i]*[components[i]])

      if robot_items[0] not in Quality_List:
          temp_task_sequence = [find_component(robot_items[0])]
          task_sequence.insert(0,find_component(robot_items[0]))
          
          components_not_stored = []
          components_stored = []
          for component in Quality_List[0]:
              if component in AS_storage:
                  components_stored.append(component)
              else:
                  components_not_stored.append(component)

          if len(components_not_stored) ==1:
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
          else:
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
          
          task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
          

      elif robot_items[0] in Quality_List:
          components_not_stored = []
          components_stored = []
          for component in Quality_List:
              if component in AS_storage:
                  components_stored.append(component)
              else:
                  components_not_stored.append(component)

          if len(components_not_stored) ==1:
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              
              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=1
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
              
          else:

              temp_task_sequence = [find_component(robot_items[0])]
              task_sequence.insert(find_component(robot_items[0]))
     
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))

              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=2
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
             

    elif (BEAST[1] < 52.5) and (len(robot_items) == 2):
      C_storage = fetch_cloud()
      # checking if there is space in the buffers
      AS_storage = []
      for i in range(len(C_storage)):
        if C_storage[i]>0:
          AS_storage.extend(C_storage[i]*[components[i]])
      if robot_items[0] not in Quality_List and robot_items[1] not in Quality_List:
          temp_task_sequence = [find_component(robot_items[0]),find_component(robot_items[1])]
          
          task_sequence.insert(0,find_component(robot_items[0]))
          task_sequence.insert(0,find_component(robot_items[1]))
              
          if len(components_not_stored) ==1:
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
          elif len(components_not_stored) >=2:
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[0])))
              Quality_List.insert(0, Quality_List.pop(Quality_List.index(components_not_stored[1])))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[0]))))
              QualityList.insert(0, QualityList.pop(QualityList.index(find_component(components_not_stored[1]))))
          
          task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          
          z=2
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
          
      elif robot_items[0] not in Quality_List and robot_items[1] in Quality_List:
          temp_task_sequence = [find_component(robot_items[0])]
          task_sequence.insert(find_component(robot_items[0]))
          
         
          task_sequence = [(QualityList[0])[i] for i in range(len(QualityList[0]))] + task_sequence
          task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
          
          z=1
          while z < len(task_sequence):
              task_sequence.insert(z, AS)
              z += 3
          task_sequence.append(AS)
          
      elif robot_items[0] in Quality_List:
          Quality_List_check = list(Quality_List[0])
          Quality_List_check.remove(robot_items[0])
          if robot_items[1] in Quality_List_check:
              
              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=2
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
              task_sequence.insert(0,AS)
              
      
          else:
              temp_task_sequence = [find_component(robot_items[1])]
              task_sequence.insert(find_component(robot_items[1]))

              task_sequence = [(QualityList)[i] for i in range(len(QualityList))] + task_sequence
              task_sequence = list(filter(lambda a: a[0] != 'AS', task_sequence))
              
              z=1
              while z < len(task_sequence):
                  task_sequence.insert(z, AS)
                  z += 3
              task_sequence.append(AS)
              
          
rp.spin()
