# Voice API
## Docker Deploy
```docker run --name voice-api -d -e data_api="data-api" -p 5000:5000 team-connected/voice-api```

### Environment Flags
| Flag | Description |
| ------------- | ------------- |
| data_api| The hostname or IP to the Data-API|


## API Design
Implemented will be marked with :heavy_check_mark:

### Voice API
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
|  | POST | http://[hostname]/api/v1/voice/ | Post a voice JSON for processing |


### Fields
#### Voice
* **id**: Unique number per request
* **patient_id**: ID of the patient
* **device_type**: The type of device, eg: blood pressure monitor, thermometer, scale
* **value**: Measuring value
* **unit**: Measuring unit
* **raw_text**: Unproccessed text from the app
* **nurse_id**: ID of the nurse