#All inforamtion
'''import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
print(Myec2)'''
 
#Instances information in JSON
'''import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
 print(pythonins)'''
 
#Instance Id
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
 for pythonins in Myec2['Reservations']:
  for printout in pythonins['Instances']:
   print(printout['InstanceId'])