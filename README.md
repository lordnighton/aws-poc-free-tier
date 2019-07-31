# AWS PoC based on a free tier ONLY

## Technological stack
- Play with EC2 and auto-scaling groups (if possible)
  - EC2 on Linux (use a Linux AMI for `t2.micro` free tier)
  - User data on startup (probably something that checks out a repo?)
  - Public IP-s for EC2 instances (cattle)
- IAM (user groups)
- All configuration-related chunks of code should be versioned (CouldFormation vs Terraform)
- CloudWatch
- SNS
  - Notify an `Admin` group as soon as the something has happened (e.g. auto-scaling group down or a certain event triggered)
- Lambda
  - Something very simple (less than `5` minutes in time)
- VPC / Availability Zones (fault tolerance) / Internet Gateway / Subnets / Route Tables / ELB / NACL
- Security groups (on a layer of EC2)
- Automated tests (containers /w Selenoid ?)
- S3 (+Glacier ?)
- python (Boto3 / Lambda ?)

## Tech task
- Develop a **Dropbox** (https://www.dropbox.com) analogue
  - The web application with a simplest storefront EVER (see the wireframe below)
  ![An example of a storefront](https://github.com/lordnighton/aws-poc-free-tier/blob/master/Untitled%20Diagram.png)
  - Using this storefront you should be able to upload the images AND then store them in S3 bucket (or even multiple buckets, depends on your choice)
  - As soon a new image is uploaded to your web site, the group of `Admin`-s should obtain the notification (SNS service) via whatever channel you prefer (both SMS and emails will work)
  - The lambda function written in `python` should calculate a size of an S3 bucket which is used for storing uploaded images AND send out this number to `Manager`-s group
  - There should be at least one EC2 instance in your auto-scaling group :-) 
    - AMI / Linux / user data
