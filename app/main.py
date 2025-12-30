import uvicorn
from fastapi import FastAPI, HTTPException, status
import data_interactor as data_i


app = FastAPI()


@app.get('/')
def home():
    return {'message' : 'Hello From MongoDB Center!'}




@app.get('/contacts')
def get_all_contacts():
    try:
        contacts = data_i.get_all_contacts()
        if contacts:
            return {'All contacts' : str(contacts)}
        return {'message' : 'No contacts found'}

    except:
        pass
    



@app.post('/contacts', response_model=data_i.Contact)
def create_contact(contact : data_i.Contact):
    new_id = data_i.create_new_contact(contact.to_dict())

    if isinstance(new_id, Exception):
        raise HTTPException(status_code=404, detail=new_id)
    
    return {'message' : 'contact created successfully', 'new_id' : new_id}




@app.put('/contacts/{c_id}', status_code=status.HTTP_200_OK)
def update_contact(c_id, contact : data_i.Contact):
    is_updated = data_i.update_contact(c_id, contact)

    if isinstance(is_updated, Exception):
        raise HTTPException(status_code=404, detail=is_updated)
    return {'message' : is_updated}




@app.delete('/contacts/{id}', status_code=status.HTTP_200_OK)
def delete_contact(c_id):

    is_deleted = data_i.delete_contact(c_id)

    if isinstance(is_deleted, Exception):
        raise HTTPException(status_code=500, detail={'message' : is_deleted})

    return {'message' : is_deleted}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')