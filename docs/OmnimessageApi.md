# omnichannel.OmnimessageApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scheduled_message**](OmnimessageApi.md#cancel_scheduled_message) | **DELETE** /omnimessage/{omnimessage_id} | Cancels a scheduled Omnimessage
[**send_omnimessage**](OmnimessageApi.md#send_omnimessage) | **POST** /omnimessage | Sends an Omnimessage


# **cancel_scheduled_message**
> cancel_scheduled_message(omnimessage_id)

Cancels a scheduled Omnimessage

### Example

* Basic Authentication (basicAuth): 
```python
from __future__ import print_function
import time
import omnichannel
from omnichannel.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = omnichannel.Configuration()
configuration.username = "<MESSENTE_API_USERNAME>"
configuration.password = "<MESSENTE_API_PASSWORD>"

# create an instance of the API class
api_instance = omnichannel.OmnimessageApi(omnichannel.ApiClient(configuration))
omnimessage_id = 'omnimessage_id_example' # str | UUID of the scheduled Omnimessage to be cancelled

try:
    # Cancels a scheduled Omnimessage
    api_instance.cancel_scheduled_message(omnimessage_id)
except ApiException as e:
    print("Exception when calling OmnimessageApi->cancel_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage_id** | [**str**](.md)| UUID of the scheduled Omnimessage to be cancelled | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_omnimessage**
> OmniMessageCreateSuccessResponse send_omnimessage(omnimessage)

Sends an Omnimessage

### Example

* Basic Authentication (basicAuth): 
```python
from __future__ import print_function
import time
import omnichannel
from omnichannel.rest import ApiException
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage** | [**Omnimessage**](Omnimessage.md)| Omnimessage to be sent | 

### Return type

[**OmniMessageCreateSuccessResponse**](OmniMessageCreateSuccessResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

