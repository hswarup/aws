# Get the python code to list all the S3 buckets and list the files in them 
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets) 

 # Iterate through each bucket and list all files in them 
for bucket in buckets: 

    # Get a list of all objects in the bucket 
    objects = s3.list_objects(Bucket=bucket)

    # Print out the object list 
    print("Object List for Bucket %s:" % bucket) 

    for obj in objects['Contents']: 

        print(obj['Key'])
