import logging
import time
import azure.functions as func
import uuid
import json


def main(request: func.HttpRequest, message: func.Out[str], queueMessage: func.Out[str]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    start = time.time()

    req_body = request.get_json()
    subtitle = req_body.get("subtitle")

    #time.sleep(5) # Simulating 5 seconds of cpu-intensive processing
    end = time.time()
    processingTime = end - start

    rowKey = str(uuid.uuid4())

    data = {
        "Name": "Message from Ann",
        "PartitionKey": "message",
        "RowKey": rowKey
    }

    message.set(json.dumps(data))

    queueMessage.set("I am a message")

    return func.HttpResponse(
        f"Processing took {str(processingTime)} seconds. Translation is: {subtitle}",
        status_code=200
    )
