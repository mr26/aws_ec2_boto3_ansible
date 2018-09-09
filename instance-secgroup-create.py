#!/usr/bin/python

import boto3
import time

ec2 = boto3.resource('ec2')

sec_group = ec2.create_security_group(
                Description='ex-sec3',
                GroupName='sec-grp3',
                )

time.sleep(30)

ec2 = boto3.client('ec2')

inb_rule = ec2.authorize_security_group_ingress(
                GroupName='sec-grp3',
                IpPermissions=[
                        {'IpProtocol': 'tcp',
                         'FromPort': 22,
                         'ToPort': 22,
                         'IpRanges': [{'CidrIp': '0.0.0.0/0'}] },

                        {'IpProtocol': 'tcp',
                         'FromPort': 80,
                         'ToPort': 80,
                         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
                         ]
        )

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
	
	ImageId='ami-6871a115',
	InstanceType='t1.micro',
	KeyName='key-pair',
	MaxCount=1,
	MinCount=1,
	Monitoring={ 'Enabled': True }, 
	
	Placement={
		'AvailabilityZone': 'us-east-1a',
		},

	SecurityGroups=['sec-grp3'],

	TagSpecifications=[
		{
			'ResourceType': 'instance',
			'Tags': [
			   {
				'Key': 'infra',
				'Value': 'Apache Group'
			   },
		]
	 },
	],


	)




