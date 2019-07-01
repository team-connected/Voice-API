# Voice API
## Docker Deploy
```docker run --name voice-api -d -e data_api="data-api" -p 8000:8000 teamconnected/voice-api```

### Environment Flags
| Flag | Description | Example |
| ------------- | ------------- | ------------- |
| data_api | The hostname or IP to the Data-API | Example: http://umc-api.maartenmol.nl:5000 |


## API Design
Implemented will be marked with :heavy_check_mark:

### Voice API
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
| :heavy_check_mark: | POST | http://[hostname]/api/v1/voice/ | Post a voice JSON for processing |


### Fields
#### Voice
* **_id**: Unique number per request
* **metric_id**: Metric ID
* **raw_text**: Unproccessed text from the app

##### Example JSON
```
{
  "_id": "65dfe4v6b1efv4d5",
  "metric_id": "5448413116465165445",
  "raw_text": "registreer temperatuur is 37.2 graden celcius"
}
```

## API Examples
``` 
curl -i -H "Content-Type: application/json" -X POST -d '{"metric_id": "c06923f2c9504e95917b5aa0a0bcc74d",
"raw_text": "registreer bloeddruk is 120 over 80"}' http://voice-api-url:8000/api/v1/voice/
```
