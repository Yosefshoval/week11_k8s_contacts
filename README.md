# week11_k8s_contacts

## This project is API-DB connecting, using mongoDB image and my FastAPI server.
## The program can show, store, update and delete contacts, as you can use this functionality by http requests.

There are 4 Endpoints:

***Get All Contacts:***
required: Nothing

***Create New Contact:***
required: Body like this: ```{"first_name": "string", "last_name": "string",  "phone_number": "string"}```.

***Update Contact:***
required: Path parameter: ```id=string```, Body like this: ```{"first_name": "string", "last_name": "string",  "phone_number": "string"}```.

***Delete Contact:***
required: Path parameter: ```id=string```.


---
To be able to run the program, follow these steps step by step:

1: **If you haven't already minikube runing, press the command below in your terminal:**
```
minikube start
```

2: **Apply the whole .yaml files -> two pods and two services:**
```
kubectl apply -f .
```

3: **Expose the API service (so that you can get the API in your browser):**
```
minikube service api-service
```
**Also you can get only the URL:**
```
minikube service api-service --url
```

Then go to your brouser and open the ip indicated in the output. Try the endpoints!!



