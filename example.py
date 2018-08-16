from pprint import pprint

from omnichannel import OmnimessageApi, Viber, SMS, Omnimessage, Configuration, ApiClient
from omnichannel.rest import ApiException


# API information from https://dashboard.messente.com/api-settings
configuration = Configuration()
configuration.username = "<MESSENTE_API_USERNAME>"
configuration.password = "<MESSENTE_API_PASSWORD>"

# create an instance of the API class
api_instance = OmnimessageApi(ApiClient(configuration))

viber = Viber(
    sender="<sender name (optional)>",
    text="hello python",
)

sms = SMS(
    sender="<sender name (optional)>",
    text="hello python",
)

# the order of items in scenarios means that sending via Viber will be attempted first,
# and in case of Viber failure, the message will be delivered via SMS
omnimessage = Omnimessage(
    messages=(viber, sms),
    to="<recipient_phone_number>",
)  # Omnimessage | Omnimessage object that is to be sent

try:
    # Sends an Omnimessage
    response = api_instance.send_omnimessage(omnimessage)
    print(
        "Successfully sent Omnimessage with id: %s that consists of the following messages:" % response.omnimessage_id
    )
    for message in response.messages:
        pprint(message)
except ApiException as e:
    print("Exception when calling OmnimessageApi->create_omnimessage: %s\n" % e)
