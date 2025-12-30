from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import os


load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_DB = os.getenv('MONGO_DB')



class Contact(BaseModel):

    id : Optional[str] = Field(..., alias='_id')
    first_name : str = Field(..., max_length=50)
    last_name : str = Field(..., max_length=50)
    phone_number : str = Field(..., max_length=20)

    def to_dict(self):
        return {'id': self.id, 'first name:' : self.first_name, 'last name': self.last_name, 'phonr number:' : self.phone_number}









def create_contact(contact_data: dict):
    pass


def get_all_contacts():
    pass

def update_contact(id : str, contact_data : dict):
    pass

def delete_contact(id : str):
    pass

