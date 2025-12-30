from db_connection import get_collection
from pydantic import BaseModel, Field
from typing import Optional, Annotated
from bson import ObjectId


class Contact(BaseModel):

    id : str = Field(..., alias='_id')
    first_name : str = Field(..., max_length=50)
    last_name : str = Field(..., max_length=50)
    phone_number : str = Field(..., max_length=20)

    def to_dict(self):
        return {'id': self.id, 'first name:' : self.first_name, 'last name': self.last_name, 'phonr number:' : self.phone_number}



def search_contact(id : str):
    collection = get_collection()
    try:
        document = collection.find_one({'_id' : ObjectId(id)})
        return document
    except Exception as e:
        return e



def search_phone(phone_number : str):
    collection = get_collection()
    try:
        document = collection.find_one({'phone_number' : phone_number})
        return document is not None
    except Exception as e:
        return e




def create_contact(contact_data: dict):
    collection = get_collection()
    try:
        if search_contact:
            return ({'message' : f'contact with phone number {contact_data["phone_number"]} already exists'})

        new_id = collection.insert_one(contact_data)
        return new_id.inserted_id

    except Exception as e:
        return e




def get_all_contacts():
    collection = get_collection()
    try:
        documents = collection.find()
        if documents:
            documents_list = [doc for doc in documents]
            return documents_list
        return ({'message' : 'no contacts found'})
    except Exception as e:
        return e


def update_contact(id : str, contact_data : dict):
    collection = get_collection()
    try:
        if search_contact:
            return ({'message' : f'contact with phone number {contact_data["phone_number"]} already exists'})

        if search_contact(id):
            collection.update_one({'_id' : ObjectId(id)}, {'$set' : contact_data})
            return ({'message' : 'contact updated successfully'})
        
        return ({'message' : 'contact not found'})
    except Exception as e:
        return e
    



def delete_contact(id : str):
    collection = get_collection()
    try:
        if search_contact(id):
            collection.delete_one({'_id' : ObjectId(id)})
            return ({'message' : 'contact deleted successfully'})
        
        return ({'message' : 'contact not found'})
    except Exception as e:
        return e
