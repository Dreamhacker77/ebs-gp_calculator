# @Dreamhacker77
import boto3

# Prompt the user for AWS credentials
aws_access_key_id = input("Enter your AWS access key ID: ")
aws_secret_access_key = input("Enter your AWS secret access key: ")
aws_session_token = input("Enter your AWS session token (if applicable): ")

# Prompt the user for the AWS region
aws_region = input("Enter your AWS region: ")

# Create AWS session
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=aws_region
)

# Connect to the EC2 service
ec2 = session.client('ec2')

# Retrieve information about all GP2 volumes
volumes = ec2.describe_volumes(Filters=[{'Name': 'volume-type', 'Values': ['gp2']}])

# Calculate the total cost of GP2 volumes in USD
gp2_cost = sum([float(volume['Size']) * 0.1 for volume in volumes['Volumes']])
gp2_cost_usd = "${:,.2f}".format(gp2_cost)

# Calculate the estimated cost of upgrading to GP3 volumes in USD
gp3_cost = sum([float(volume['Size']) * 0.08 for volume in volumes['Volumes']])
gp3_cost_usd = "${:,.2f}".format(gp3_cost)

# Calculate the potential savings in USD
potential_savings = gp2_cost - gp3_cost
potential_savings_usd = "${:,.2f}".format(potential_savings)

# Print the TCO analysis results
print(f"Total cost of GP2 volumes: {gp2_cost_usd}")
print(f"Estimated cost of upgrading to GP3 volumes: {gp3_cost_usd}")
print(f"Potential savings: {potential_savings_usd}")
