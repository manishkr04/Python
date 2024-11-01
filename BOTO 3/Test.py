
# using boto3 mudule to interact with aws and create s3 Bucket
import boto3
import json
from datetime import datetime

client = boto3.client('ec2')

#response = client.create_bucket(
#    Bucket = 'abhi-demo-boto3-yt-121',
#    #CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
#)

# to get acl of S3 Bucket
#   response = client.get_bucket_acl(
#       Bucket='abhi-demo-boto3-yt-12',
#   )
#   owner = response['Owner']
#   print(owner)





#    # Fetch all running EC2 instances
#    response = client.describe_instances(Filters=[
#        {
#            'Name': 'instance-state-name',  # Corrected the filter name
#            'Values': ['running'],
#        },
#    ])
#    # Function to convert datetime objects to strings
#    def convert_datetime(obj):
#        if isinstance(obj, datetime):
#            return obj.isoformat()  # Convert datetime to ISO format
#        raise TypeError("Type not serializable")
#    
#    # Open a text file in write mode
#    with open('running_instances_details.txt', 'w') as file:
#        # Convert the response to a JSON-formatted string and write to file
#        file.write(json.dumps(response, default=convert_datetime, indent=4))
#    
#    print("Details of running instances have been saved to running_instances_details.txt")





#Fetch all the details of Snapshots
snapshot_response = client.describe_snapshots(OwnerIds=['self'])

# Function to convert datetime objects to strings
def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO format
    raise TypeError("Type not serializable")


# Open a text file in write mode
with open('running_snapshot_details.txt', 'w') as file:
    # Convert the response to a JSON-formatted string and write to file
    file.write(json.dumps(snapshot_response, default=convert_datetime, indent=4))

print("Details of running instances have been saved to running_instances_details.txt")


