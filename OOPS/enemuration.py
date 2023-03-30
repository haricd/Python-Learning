from enum import Enum
import json

class Color(Enum):
    RED = 2
    BLACK = 5
    YELLOW = 7

print(Color.RED.name, Color.RED.value)
print(Color(7))

#################################################


class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'


response = '''{
    "status":"fulfilled"
}'''

data = json.loads(response)
status = data['status']

try:
    if ResponseStatus(status) is ResponseStatus.FULFILLED:
        print('The request completed successfully')
except ValueError as error:
    print(error)

