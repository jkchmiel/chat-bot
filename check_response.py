import json
from helpers import ResponseGenerator


if __name__ == "__main__":

    ## API.ai json output needed to be put in request.json file
    with open("sample/request.json") as input_file:
        req = json.load(input_file)

    print(ResponseGenerator.generate_response(req))
