### test domain command

```
$ aws es create-elasticsearch-domain --domain-name testing --elasticsearch-version 6.5 --elasticsearch-cluster-config InstanceType=m4.large.elasticsearch,InstanceCount=1 --ebs-options EBSEnabled=true,VolumeType=standard,VolumeSize=10 --access-policies '{"Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::123456789012:root" }, "Action":"es:*", "Resource": "arn:aws:es:us-east-1:123456789012:domain/testing/*" } ] }' --vpc-options SubnetIds=subnet-1a2a3a4a,SecurityGroupIds=sg-2a3a4a5a
```
$ aws configure

AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: us-west-2
Default output format [None]: json
 (initially default, later the above)

`$ pip3 install awscli --upgrade --user`

# Use pip to install the AWS CLI.
`$ pip3 install awscli --upgrade --user`
`$ pip install --upgrade pip`

`$ aws --version`
(o/p - aws-cli/1.16.155 Python/3.5.2 Linux/4.4.0-1077-aws botocore/1.12.145)

`$ pip3 install awscli --upgrade --user`

#You can verify which folder pip installed the AWS CLI to by running the following command.
`$ which aws`
(o/p - /home/ubuntu/.local/bin/aws)
