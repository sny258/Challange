For getting meta data of an instance within AWS:

option 1:

- First create an EC2 instance
- SSH/RDP in that EC2 instance 
- use the command for linux: curl http://169.254.169.254/latest/meta-data/ | jq  (this will list all the metadata items in Json)
- Or use the command for windows: Invoke-RestMethod -uri "http://169.254.169.254/latest/meta-data/" | ConvertTo-Json (will list the metadata items in Json)

- to find the specific metadata item: curl http://169.254.169.254/latest/meta-data/<metadata item>

- OR we can utilize the sample scripts metadata.py (for metadata of an instance by running python script by logging into instance) and metadatakey.py (for metadata item information)



option 2:

- First create an EC2 instance
- SSH/RDP in that EC2 instance
- Open AWS CLI in machine by providing Access Key ID and Secret Access Key (can be generated from AWS portal)
- use aws configure to login and use AWS CLI
- install python and boto3 module
- create the python script metadataBoto3.py (which will use boto3 to obtain instance details)
- by running the python script we can get the instance details as json output

