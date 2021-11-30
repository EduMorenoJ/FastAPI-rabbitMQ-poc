# CARTO TEST

## Descripcion de los componentes del sistema

El sistema ha sido diseñado como un sistema distribuido para permitir su escalabilidad en caso de mayor demanda del mismo. Consta de distintos servicios:

- API -> desarrollada con el framework FastApi y utilizando asyncio para obtener un mayor rendimiento. He indicado que endpoints podria necesitar el frontend como indicaba en la prueba. Serian necesarios los siguientes endpoints:

        Paystats:
            
            - Aparte de los CRUD basicos
            - Obtener paystats para un postal_code_id
            - Obtener el amount total por cada postal_code
            - Obtener el total amount en un time series
            - Obtener el total amount ordenado por edad y género

        Postalcode:

            - Aparte de los CRUD basicos
            - Obtener el geosjon equibalente para su wkb.

    Son los primeros endpoints que se me vienen a la mente al ver la imagen. Seguramente, haran falta mas y siempre serian adaptables a las necesidades del frontend. Solo he desarrollado algunos como indicaba la prueba, si es necesario puedo desarrollarlos todos sin ningun problema.

    En la API he desarrollado algunos test tambien a modo de ejemplo aunque faltarian muchos mas test unitarios aparte de los de integración. Siempre intento cobertura del 100%. Para los test me gusta mucho el framework pytest facilita mucho el desarrollo de los mismo con los fixtures, parametrize y demas decoradores increiblemente utiles.

- Persistor -> Este microservicio lo desarrolle pensando que si tenia que preparar el sistema para recibir y cargar en la base de datps mas csv's. Aunque al final no fuera necesario, lo he dejado puesto que puede servir de ejemplo como componente en un sistema que necesita cargar un gran volumen de datos cuando se le requiera. En este servicio se podria incluir la validacion de los datos antes de cargarlos. El persistor, simula leer de un datalake y se le invocaría mediante la misma api indicandole la ruta al fichero. Por tanto para cargar los datos, en la misma API, hay un tercer grupo de endpoints en el que se selecciona la entidad a cargar en la base de datos. La API manda un mensaje al persistor y este comenzaría a cargar los datos. Habria que validarlos previamente y comprobar la integridad de los mismos. Ahora mismo, si se carga dos veces el mismo archivo, se repetirían los datos puesto que no hay ningun tipo de validación.

- MongoDB -> Es la base de datos no relacional que he usado para persistir los datos

- RabbitMQ -> Es el sistema de paso de mensajes que he usado para comunicar la API con el persistor

El sistema, al estar dockerizado, seria facilmente desplegable en kubernetes, el cual nos permite una orquestacion y una escalabilidad de los contenedores a demanda. Ademas, enfocandolos de una manera serverless (el servicio solo se levanta cuando se le requiere) abarataría los costes deribados de tener un sistema on cloud. Para completar la infraestructura, seria necesario un sistema de centralizacion de logs y monitorizacion, loki y grafana son herramientas muy utiles para este proposito.

## Intrucciones

Para ejecutar el sistema basta con hacer:

```bash
docker-compose up --build
```

Esperar a que el sistema se termine de levantar por completo. Se veran algunos fallos de conexion del persistor hasta que consiga conectar con rabbit. Este metodo de reintentos es muy mejorable y lo he dejado asi por ser una demo.

Para acceder a la API ir a [localhost:8080/docs](http://localhost:8080/docs) veremos un swagger totalmente funcional y con toda la documentacion de la API.

FastAPI me parece el mejor framework para el desarrollo de APIS que hay en python actualmente. Es increiblemente sencillo la construción de modelos con sus validaciones y la integración con una base de datos, junto con los modelos de Pydantic.