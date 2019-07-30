# AWS PoC based on a free tier ONLY

## Technological stack
- Play with EC2 and auto-scaling groups (if possible)
  - EC2 on Linux (use an AMI)
  - User data on startup
  - Public IP for EC2 instance (cattle)
- IAM (user groups)
- All configuration should be versioned (CouldFormation vs Terraform)
- CloudWatch
- SNS
  - Notify an `Admin` group as soon as the auto-scaling group down
- Lambda
  - Something very simple (less than `5` minutes in time)
- VPC / Availability Zones (fault tolerance) / Internet Gateway / Subnets / Route Tables / ELB / NACL
- Security groups (on a layer of EC2)
- Automated tests (containers /w Selenoid ?)
- S3 (+Glacier ?)
- RDS (or even DynamoDB)

## Tech task
- Develop a Dropbox analogue
  - The web application with a simplest storefront EVER
