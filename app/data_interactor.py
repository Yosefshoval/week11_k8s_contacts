from db_connection import get_collection
from pydantic import BaseModel, Field
from bson import ObjectId


class Contact(BaseModel):

    id : str = None
    first_name : str = Field(..., max_length=50)
    last_name : str = Field(..., max_length=50)
    phone_number : str = Field(..., max_length=20)

    def to_dict(self):
        return {'id': self.id, 'first_name:' : self.first_name, 'last_name': self.last_name, 'phone_number:' : self.phone_number}




class CrudContact:

    @staticmethod
    def search_contact_by_id(id : str):
        collection = get_collection()
        try:
            document = collection.find_one({'_id' : ObjectId(id)})
            return document
        except Exception as e:
            return e


    @staticmethod
    def search_phone(phone_number : str):
        collection = get_collection()
        try:
            document = collection.find_one({'phone_number' : phone_number})
            return document is not None
        except Exception as e:
            return e


    @staticmethod
    def get_all_contacts():
        collection = get_collection()
        try:
            documents = collection.find()
            if documents:
                documents_list = [doc for doc in documents]
                return documents_list
            return None
        
        except Exception as e:
            return e


    @staticmethod
    def create_new_contact(contact_data: dict):

        try:
            collection = get_collection()
            phone_exists = CrudContact.search_phone(contact_data['phone_number'])
            if phone_exists:
                raise ValueError(f'contact with phone number {contact_data["phone_number"]} already exists')

            del contact_data['id']
            new_id = collection.insert_one(contact_data)
            return new_id.inserted_id

        except Exception as e:
            return e


    @staticmethod
    def update_contact(id : str, contact_data : dict):
    
        try:
            collection = get_collection()

            phone_exists = CrudContact.search_phone(contact_data['phone_number'])
            
            if phone_exists:
                raise ValueError(f'contact with phone number {contact_data["phone_number"]} already exists')

            if CrudContact.search_contact_by_id(id):
                collection.update_one({'_id' : ObjectId(id)}, {'$set' : contact_data})
                return ({'message' : 'contact with id {id} updated successfully'})
            
            raise ValueError(f'contact with id {id} not found')
        
        except Exception as e:
            return e
        

    @staticmethod
    def delete_contact(id : str):
        collection = get_collection()
        try:
            if CrudContact.search_contact_by_id(id):
                collection.delete_one({'_id' : ObjectId(id)})
                return {'message' : 'contact deleted successfully'}
            
            return f'contact with id {id} not found'
        
        except Exception as e:
            return e
