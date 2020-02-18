import json
import os
import boto3
access = ''
secret = ''
gw = boto3.client('apigateway',aws_access_key_id = access,aws_secret_access_key=secret,region_name='us-east-1')
s3 = boto3.client('s3')


export_responce = gw.get_export(
    restApiId='0rgv5qefe8',
    stageName='test',
    exportType='swagger',
    accepts='application/json'
)


# export_responce = gw.get_export(
#     restApiId=os.environ['apiid'],
#     stageName=os.environ['stagename'],
#     exportType='swagger',
#     accepts='application/json'
# )

# print(type(export_responce['body']))
# print(dir(export_responce['body']))
# print(export_responce['body'].read())
a = export_responce['body'].read().decode('utf-8')
# b = a.decode('utf8')
# for i in export_responce['body'].read():
#     print(i)
# print(b)
c = json.loads(a)


print(c)
# exported_stream=(export_responce['body'].read())
# print ("before json body", exported_stream)
# json_body=(export_responce['body'].read()).decode('utf8')
#
# json_body = json.loads(str((export_responce['body'].read())))
# print("after json body")
#
# print("exact location ", json_body)