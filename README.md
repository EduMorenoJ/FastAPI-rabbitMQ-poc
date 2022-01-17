# FAST API with Rabbit MQ

This is an example of using FAST API with Rabbit MQ for resolving all the backend architecture for a given UI. The given UI is the wireframe.png image on this repo. The exercise consists of designing and implementing an API to communicate the frontend part with the backend and a component in charge of persisting all the needed data on the database. Let's call this last component "persistor". It will be our component listening on a Rabbit queue, waiting to start loading data on the database (mongodb)

The data folder will simulate a datalake where the persistor will read the data and send it to the database. The API provides an endpoint that sends a message to the persistor to start reading the data from the datalake and loading the data on the database.

The API would provide this endpoint explained above, all the CRUD endpoints, and some more that you think will be necessary for the front. In this example, not all of them are implemented, just a few to illustrate how FAST API works. 

## Quick start

```bash
docker-compose up --build
```

Wait until the system is completely up and go to [localhost:8080/docs](http://localhost:8080/docs) to see our API swagger.

