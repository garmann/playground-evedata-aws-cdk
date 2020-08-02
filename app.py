#!/usr/bin/env python3

from aws_cdk import core

from playground_evedata_aws_cdk.playground_evedata_aws_cdk_stack import PlaygroundEvedataAwsCdkStack

env = core.Environment(region='eu-central-1')
                       #, account='x')

app = core.App()
PlaygroundEvedataAwsCdkStack(app, "playground-evedata-aws-cdk", env=env)

app.synth()
