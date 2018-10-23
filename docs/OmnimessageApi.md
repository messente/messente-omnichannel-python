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

# Configure HTTP basic authorization: basicAuth
configuration = omnichannel.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = omnichannel.OmnimessageApi(omnichannel.ApiClient(configuration))
omnimessage = omnichannel.Omnimessage() # Omnimessage | Omnimessage to be sent

try:
    # Sends an Omnimessage
    api_response = api_instance.send_omnimessage(omnimessage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmnimessageApi->send_omnimessage: %s\n" % e)
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

