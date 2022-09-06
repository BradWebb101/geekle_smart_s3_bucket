import aws_cdk as core
import aws_cdk.assertions as assertions

from smarts3_bucket.smarts3_bucket_stack import Smarts3BucketStack

# example tests. To run these tests, uncomment this file along with the example
# resource in smarts3_bucket/smarts3_bucket_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Smarts3BucketStack(app, "smarts3-bucket")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
