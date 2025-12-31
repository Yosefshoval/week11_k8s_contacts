import uvicorn
from fastapi import FastAPI, HTTPException, status
from data_interactor import CrudContact, Contact


app = FastAPI()


@app.get('/')
def home():
    return {'message' : 'Hello From MongoDB Center!'}


@app.get('/contacts')
def get_all_contacts():
    try:
        contacts = CrudContact.get_all_contacts()
        if contacts is None:
            return {'message' : 'no contacts found'}
        
        return {'All contacts' : str(contacts)}

    except Exception as e:
        return {'message' : e}



@app.post('/contacts')
def create_contact(contact : Contact):
    try:
        new_id = CrudContact.create_new_contact(contact.model_dump())
        if isinstance(new_id, Exception):
            # return {'error message' : str(new_id)}
            raise HTTPException(status_code=404, detail=new_id)
        return {'message' : 'contact created successfully', 'id' : str(new_id)}
    except HTTPException as e:
        return {'message' : str(e)}




@app.put('/contacts/{c_id}', status_code=status.HTTP_200_OK)
def update_contact(c_id, contact : Contact):
    is_updated = CrudContact.update_contact(c_id, contact.model_dump())

    try:
        if isinstance(is_updated, Exception):
            raise HTTPException(status_code=404, detail=is_updated)
    except HTTPException as e:
        return {'message' : e}
    
    return {'message' : is_updated}




@app.delete('/contacts/{id}', status_code=status.HTTP_200_OK)
def delete_contact(c_id):

    is_deleted = CrudContact.delete_contact(c_id)

    try:
        if isinstance(is_deleted, Exception):
            raise HTTPException(status_code=500, detail=is_deleted)
    except HTTPException as e:
        return {'message' : e}

    return {'message' : is_deleted}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')