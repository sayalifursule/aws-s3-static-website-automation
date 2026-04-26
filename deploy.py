import boto3
import os
import json
from botocore.exceptions import ClientError

# CONFIG
bucket_name = "sayali-demo-site-2026-001"   # ⚠️ change if needed (must be unique)
region = "ap-south-1"

# Create S3 client
s3 = boto3.client('s3')

# 1️⃣ Create bucket (skip if exists)
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print("✅ Bucket created")

except ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        print("⚠️ Bucket already exists, continuing...")
    else:
        raise e


# 2️⃣ Disable public access block
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

print("✅ Public access enabled")


# 3️⃣ Upload index.html (from same folder)
file_name = "index.html"

if not os.path.exists(file_name):
    print("❌ ERROR: index.html not found in this folder")
    exit()

s3.upload_file(
    file_name,
    bucket_name,
    file_name,
    ExtraArgs={'ContentType': 'text/html'}
)

print("✅ File uploaded")


# 4️⃣ Enable static website hosting
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'}
    }
)

print("✅ Website hosting enabled")


# 5️⃣ Add public bucket policy
policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": f"arn:aws:s3:::{bucket_name}/*"
    }]
}

s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(policy)
)

print("✅ Bucket policy added")


# 6️⃣ Final URL
website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"

print("\n🎉 SUCCESS! Your website is live:")
print(website_url)