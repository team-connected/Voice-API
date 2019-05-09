# Voice API
## Docker Deploy
```docker run --name voice-api -d -e data_api="data-api" -p 6000:6000 team-connected/voice-api```

### Environment Flags
| Flag | Description |
| ------------- | ------------- |
| data_api | The hostname or IP to the Data-API |


## API Design
Implemented will be marked with :heavy_check_mark:

### Voice API
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
|  | POST | http://[hostname]/api/v1/voice/ | Post a voice JSON for processing |


### Fields
#### Voice
* **_id**: Unique number per request
* **metric_id**: Metric ID
* **patient_id**: ID of the patient
* **nurse_id**: ID of the nurse
* **raw_text**: Unproccessed text from the app

##### Example JSON
```
{
  "_id": "65dfe4v6b1efv4d5",
  "metric_id": "5448413116465165445",
  "patient_id": "6249861651986545198",
  "nurse_id": "65498610265564685465165"
  "raw_text": "registreer temperatuur is 37.2 graden celcius"
}
```
