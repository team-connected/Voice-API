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
* **raw_text**: Unproccessed text from the app
* **nurse_id**: ID of the nurse

##### Example JSON
```
{
  "id": "65dfe4v6b1efv4d5",
  "patient_id": "6249861651986545198",
  "raw_text": "registreer temperatuur is 37.2 graden celcius",
  "nurse_id": "65498610265"
}
```
