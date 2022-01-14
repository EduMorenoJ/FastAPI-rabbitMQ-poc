# FAST API with Rabbit MQ

This is an example of using FAST API with Rabbit MQ for resolving all the backend achitecture for a given UI. The given UI is the wireframe.png image on this repo. The exersise consist on desing and implement an API to comunicate the frontend part with the backend and a component in charge of persist all the needed data on the database. Lets call this last component "persistor". It will be our component listening on a Rabbit queue, waiting to start loading data on the database (mongodb)

The data folder will simulate a datalake where the persistor will read the data and send it to the database. The API provide an endpoint which send a message to the persistor to start loading the data on the database.

So the API would provide this endpoint explained above, all the CRUD endpoints and some more that you think that they will be neccesary for the front. In this example, not all of them are implemented, just a few to ilustrate how FAST API works. 

## Quick start


```bash
docker-compose up --build
```

Esperar a que el sistema se termine de levantar por completo. Se veran algunos fallos de conexion del persistor hasta que consiga conectar con rabbit. Este metodo de reintentos es muy mejorable y lo he dejado asi por ser una demo. Otra cosa mejorable seria el separar los requirements.txt para que cada microservicio solo instale los que necesite. Tambien securizar la API que no he tenido tiempo, pero con FastAPI es bastante sencillo. 

Para acceder a la API ir a [localhost:8080/docs](http://localhost:8080/docs) veremos un swagger totalmente funcional y con toda la documentacion de la API.

