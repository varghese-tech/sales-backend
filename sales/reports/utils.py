def response_create_ok(message="Created Successfully",data={}):
    response = {
        "message":message,
        "status":201,
        "data":data
    }
    return response

def response_get_ok(data, message="Fetched Successfully"):
    response = {
        "message":message,
        "status":200,
        "data":data
    }
    return response

def bad_response(message="Request Failed", error={}):
    response = {
        "message":message,
        "status":500,
        "error":error
    }
    return response