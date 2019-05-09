## Bring up the elasticsearch server (ELK)
```
docker-compose up
```

## Check the status of the docker instances 
```
docker-compose ps
```

## Check the existing volumes

The data is in `elastic_search_esdata1` volume
```
docker volume ls
```

Access the kibana interface at `http://0.0.0.0:5601`

## Docker instance administrivia

### Start
```
docker-compose start
```

### Stop
```
docker-compose stop
```

### Delete the image
```
docker-compose rm
```
