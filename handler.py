import json


def getTrack(event, context):
    body = {
        "message": "Hola desde python y serverless!",
        "input": event
    }
    print('aca')
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

if __name__ == "__main__":
    getTrack('', '')