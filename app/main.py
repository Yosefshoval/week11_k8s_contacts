import uvicorn
from fastapi import FastAPI, HTTPException, status
import data_interactor as data_i


app = FastAPI()


def get_cursor():
    pass


@app.get('/')
def home():
    if isinstance(cursor, Exception):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message' : f'failed to connect to database., {cursor}'}
            )
    
    return {'message' : 'Hello From inside the container!!'}




@app.get('/contacts', response_model=list[data_i.Contact])
def get_all_contacts():
    cursor, connector = get_cursor()
    contacts = data_i.get_all_contacts()
    return {'All contacts' : contacts}




@app.post('/contacts', response_model=data_i.Contact)
def create_contact(contact : data_i.Contact):
    new_id = data_i.create_new_contact(contact)

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