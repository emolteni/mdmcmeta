from pydantic import BaseModel
from datetime import datetime

class MetadataCreate(BaseModel):  # class classname(class from which it inherits)
    filename: str
    username: str
    width: int
    height: int
    n_channels: int
    date: datetime
    size: int

class MetadataGet(MetadataCreate):
    id: int
# so the class MetadataGet has all the inherited variables from MetadataCreate
# plus the "id" var defined here
