### About

Django API exposing an endpoint to manage shoes with a VueJs frontend to consume the API.

#### Fashion-related resource: Shoes.

#### Calculated Attribute: gross_price.

### Version
1.0

### How set up and run?

1. Configure project.
```console
git@github.com:azengard/automation-team-store-challenge.git
cd automation-team-store-challenge
git checkout develop
cp .env-sample .env
```

2. Run Project using Docker-Compose (Fast way)
* Develop
```console
docker-compose up
```

* Production
```console
docker-compose -f docker-compose-prod.yml
```

After the containers are up and running you can access the project at [http://localhost:8000/](http://localhost:8000/)

With the containers running you also may access some additional API documentations!

* [Redoc](http://localhost:8000/docs/redoc/)
* [Swagger](http://localhost:8000/docs/swagger/)
* [Yaml API Doc](http://localhost:8000/docs/swagger.yaml)
* [Json API Doc](http://localhost:8000/docs/swagger.json)

3. Run project locally
```console
python -m venv .dafiti-test
source .dafiti-test/bin/activate
cd backend
pip install poetry
poetry install
```

**Important!** make sure postgres container are up.
```console
python manage.py migrate
python manage.py runserver
```

4. Run project tests
**Important!** make sure postgres container are up and you inside backend folder.
```console
pytest
```

### Docker services?

####Backend
* Django application, serve de API and communicate with database.
```console
docker-compose up backend
```

####Frontend
* Vue application, this container is only used for development, that way you don't need to reload your application to see every change.
```console
docker-compose up frontend
```

####NGINX
* Used to serve the Frontend application and handle the requests redirects to Backend.
```console
docker-compose up nginx
```

####Postgres
* A robust and secure database.
```console
docker-compose up postgres
```

### API

#### Attributes:
- name: CharField, max_length=150
- brand: CharField, max_length=100 
- ref: CharField, max_length=15
- material: CharField, max_length=100
- color: CharField, max_length=100
- description: TextField
- size: IntegerField
- quantity: IntegerField
- weight: FloatField
- net_price: DecimalField
- tax: DecimalField
- gross_price = DecimalField **Calculated field** ((net_price * tax)/100) + net_price 

#### Endpoints

**Basepath: http://localhost:8000/api/v1**

### **- GET (list) - /shoes/**
* Retrieve all Shoes items.

*Example:*
```console
curl http://localhost:8000/api/v1/shoes/
```

Query filter params:
- name
- brand

*Example:*
```console
curl http://localhost:8000/api/v1/shoes/?name=<name>
```

*Success Response Code:* **200 - OK**


### **- POST - /shoes/**
* Create a new Shoe item.

*Example:*
```console
curl -X POST "http://localhost:8000/api/v1/shoes/" -d "{  \"name\": \"string\",  \"brand\": \"string\",  
\"ref\": \"string\",  \"material\": \"string\",  \"color\": \"string\",  \"description\": \"string\",  
\"size\": 0,  \"quantity\": 0,  \"weight\": 0,  \"net_price\": 0,  \"tax\": 0}"
```

*Success Response Code:* **201 - CREATED**


### **- GET (detail) - /shoes/{id}/**
* Get a Shoe

*Example:*
```console
curl "http://localhost:8000/api/v1/shoes/{id}/"
```

*Success Response Code:* **200 - OK**


### **- PATCH - /shoes/{id}/**
* Partial updates a Shoe item.

*Example:*
```console
curl -X PATCH "http://localhost:8000/api/v1/shoes/{id}/" -d "{  \"name\": \"string\",  \"brand\": \"string\",  
\"ref\": \"string\",  \"material\": \"string\",  \"color\": \"string\",  \"description\": \"string\",  
\"size\": 0,  \"quantity\": 0,  \"weight\": 0,  \"net_price\": 0,  \"tax\": 0}"
```

*Success Response Code:* **200 - OK**


### **- PUT - /shoes/{id}/**
* Update a Shoe item.

*Example:*
```console
curl -X PUT "http://localhost:8000/api/v1/shoes/{id}/" -d "{  \"name\": \"New Name\" }"
```

*Success Response Code:* **200 - OK**


### **- DELETE - /shoes/{id}/**
* Delete a Shoe item.

*Example:*
```console
curl -X DELETE "http://localhost:8000/api/v1/shoes/{id}/"
```

*Success Response Code:* **204 - NO CONTENT**


### **- POST - /shoes/csv/**
* Upload a CSV Shoe list to bulk create Shoes items.

*Example:*
```console
curl -F file=@{file_path} "http://localhost:8000/api/v1/shoes/csv"
```
**Tip** You can use the test csv file! backend/apps/core/tests/shoes.csv

*Success Response Code:* **201 - CREATED**
