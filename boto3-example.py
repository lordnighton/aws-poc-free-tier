import boto3

s3 = boto3.client('s3')
# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
    
# s3.create_bucket(Bucket='my-bucket-lordnighton')