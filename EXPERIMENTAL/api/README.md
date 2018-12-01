# Charles API
Sometimes, we want to make a device, but it doesn't have enough processing power and memory to run Charles all by itself. For that, we need to host Charles on a server, and use an API to send information back and forth between the two devices.

That's what this folder allows us to do.

## Using the API
An example JSON request sent to the Charles server might look like this:
```
{
  "device":{
    "type":"your_device_type",
    "name":"your_device_name"
  },
  "api_key":"your_api_key",
  "request":"your_request_string"
}
```

Charles response would then be:

```
{
  "response":{
    "status":"success/error",
    "utterance":"This is what Charles says back after you give that request"
  }
}
```

