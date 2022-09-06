from aws_cdk import (
    Stack,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_s3_notifications,
     aws_iam as iam,
     Aws
)
from constructs import Construct

class Smarts3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create bucket
        input_bucket = _s3.Bucket(self, "smart_s3_bucket", versioned=True,  block_public_access=_s3.BlockPublicAccess.BLOCK_ALL)
        output_bucket = _s3.Bucket(self, "smart_s3_bucket_output", versioned=True, block_public_access=_s3.BlockPublicAccess.BLOCK_ALL)


        # create lambda function
        function = _lambda.Function(self, "transform_data_file",
                                    runtime=_lambda.Runtime.PYTHON_3_9,
                                    handler="lambda_handler.main",
                                    environment={'destination_bucket':output_bucket.bucket_name},
                                    code=_lambda.Code.from_asset("./lambda")
                                    )
        
        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # add notificaiton for OBJECT_CREATED_PUT
        input_bucket.add_event_notification(_s3.EventType.OBJECT_CREATED_PUT, notification)

        # granting permissions for the lambda functino son the s3 buckets. 
        input_bucket.grant_read(function)
        output_bucket.grant_read_write(function)

