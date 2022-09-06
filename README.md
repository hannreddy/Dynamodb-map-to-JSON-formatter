# Dynamodb map to JSON formatter
Python Utility for converting dynamoDB MAP to JSON data

Recently I got a chance to work with DynamoDB and understood the challenge in converting the JSON payload to DynamoDB accepted MAP format and vice versa.
DynamoDB needs adding of value type to the JSON data for storing in a Attribute of type MAP.
So formatting to DynamoDB accepted format and also reformatting DynamoDB MAP data to JSON data is a regular activity.

I have written a utility to do dynamoDB MAP to JSON data conversion.

Please refer to the [AWS documentation for understanding the conversion format](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#client).

## Code for calling the utility class
```
  from ddb_map_to_json import ddb_map_to_json

  test1 = ddb_map_to_json(data1)
  print(test1.format_data())
```

My other utility to convert JSON data to DynamoDB MAP format is available [here](https://github.com/hannreddy/json-to-dynomodb-map-formatter-utility).
