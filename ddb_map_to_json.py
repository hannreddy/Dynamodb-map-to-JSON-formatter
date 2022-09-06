__author__ = "Hanumanth Reddy Aredla"
__version__ = "1.0"
__maintainer__ = "Hanumanth Reddy Aredla"
__email__ = "hann.reddy@gmail.com"


class ddb_map_to_json:
    """
    DynamoDB needs extra formatting to JSON data to be stored in a Attribute of type MAP.
    So formatting to DynamoDB accepted format and also reformatting DynamoDB MAP data to JSON data is a regular activity.

    I have handled both the formattings. Utility to convert JSON to DynamoDB accepted data is available at:
    https://github.com/hannreddy/json-to-dynomodb-map-formatter-utility

    This utility is used to convert any DynamoDB MAP payload to normal JSON data by removing extra specs from the payload.

    Please refer to AWS documentation for understanding the dynamodb format.
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#client
    """

    def __init__(self, input_payload):
        self.formatted_payload = {}
        self.input_payload = input_payload

    def format_data(self):
        """
        Processing the data
            Input: DynamoDB MAP object
            Output: JSON object
        """
        self.formatted_payload = ""
        for key in self.input_payload:
            if key == "M":
                self.formatted_payload = self.map_formatter(self.input_payload[key])
            elif key == "L":
                self.formatted_payload = self.list_formatter(self.input_payload[key])
            elif key == "S":
                self.formatted_payload = self.input_payload[key]
            elif key == "N":
                self.formatted_payload = self.input_payload[key]
            elif key == "BOOL":
                self.formatted_payload = self.input_payload[key]
        return self.formatted_payload

    def map_formatter(self, data):
        temp_dict = {}
        for key in data:
            if key == "M":
                return self.map_formatter(data[key])
            elif key == "L":
                return self.list_formatter(data[key])
            elif key == "S":
                return data[key]
            elif key == "N":
                if float(data[key]).is_integer():
                    return int(float(data[key]))
                else:
                    return float(data[key])
            elif key == "BOOL":
                return bool(data[key])
            else:
                temp_dict[key] = self.map_formatter(data[key])
        return temp_dict

    def list_formatter(self, data):
        temp_list = []
        for item in data:
            if type(item) == dict:
                temp_list.append(self.map_formatter(item))
            elif type(item) == list:
                temp_list.append(self.list_formatter(item))
        return temp_list