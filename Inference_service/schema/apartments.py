" Schema for Apartments dataset"

from pydantic import BaseModel

class Apartments(BaseModel):
    
    """ 
Apartment Schema 


"""

    area: int
    constraction_year: int
    bedrooms: int
    garden_area: int
    balcony_present: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int


