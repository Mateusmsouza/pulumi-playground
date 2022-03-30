"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

ubuntu = aws.ec2.get_ami(
     most_recent=True,
     filters=[
         aws.ec2.GetAmiFilterArgs(
             name="name",
             values=["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],
         ),
         aws.ec2.GetAmiFilterArgs(
             name="virtualization-type",
             values=["hvm"],
         ),
     ],
     owners=["099720109477"])
web = aws.ec2.Instance("web",
     ami=ubuntu.id,
     instance_type="t3.micro",
     tags={
         "Name": "HelloWorld",
     })
