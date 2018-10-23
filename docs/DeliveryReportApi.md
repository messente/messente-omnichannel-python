# omnichannel.DeliveryReportApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_delivery_report**](DeliveryReportApi.md#retrieve_delivery_report) | **GET** /omnimessage/{omnimessage_id}/status | Retrieves the delivery report for the Omnimessage


# **retrieve_delivery_report**
> DeliveryReportResponse retrieve_delivery_report(omnimessage_id)

Retrieves the delivery report for the Omnimessage

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
api_instance = omnichannel.DeliveryReportApi(omnichannel.ApiClient(configuration))
omnimessage_id = 'omnimessage_id_example' # str | UUID of the Omnimessage to for which the delivery report is to be retrieved

try:
    # Retrieves the delivery report for the Omnimessage
    api_response = api_instance.retrieve_delivery_report(omnimessage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryReportApi->retrieve_delivery_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omnimessage_id** | [**str**](.md)| UUID of the Omnimessage to for which the delivery report is to be retrieved | 

### Return type

[**DeliveryReportResponse**](DeliveryReportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

