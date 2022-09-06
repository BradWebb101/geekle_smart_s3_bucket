#!/usr/bin/env python3
import os

import aws_cdk as cdk

from smarts3_bucket.smarts3_bucket_stack import Smarts3BucketStack


app = cdk.App()

Smarts3BucketStack(app, "Smarts3BucketStack",

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
    
    )


app.synth()
