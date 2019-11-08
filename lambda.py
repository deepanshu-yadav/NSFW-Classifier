import boto3
import json
import numpy as np
import base64, os, boto3, ast, json 




endpoint = 'myprojectcapstone'
 
def format_response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            }
        }
 

            
        
def lambda_handler(event, context):
    try :
        body = json.loads(event['body'])
        image = base64.b64decode(body['data'].replace('data:image/png;base64,', ''))
        
        try :
            runtime = boto3.Session().client(service_name='sagemaker-runtime', region_name='us-east-2')
            response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='application/x-image', Body=image)
            print(response)
            
            try:
                probs = response['Body'].read()
                probs = json.loads(probs)
                #probs = ast.literal_eval(probs)
                #pred = probs.index(max(probs))
                pred = np.argmax( np.array( probs ) )
                if pred == 0:
                    resp = 'Animated Nsfw'
                elif pred == 1:
                    resp = 'Conatins Nudity'
                elif pred == 2:
                    resp = 'Contains Porn'
                elif pred == 4: 
                    resp = 'Conatins semi Nudity'
                else :
                    resp = 'Safe For viewing'
                return format_response(resp, 200)               
            except:
                return format_response('Ouch! Something went wrong with loading json data from endpoint'+response['Body'].read() , 200)            
        except :
            return format_response('Ouch! Something went wrong with endpoint' , 200)        
    except :
        return format_response('Ouch! Something went wrong with decoding' , 200)
       
    


