class InstrumentModel:
    id: int
    instrument_name: str
    manufacturer_id: str
    category_id: str
    description: str
    color : str
    tags: str
    
    def __init__(self, id: int,instrument_name: str, manufacturer_id: str,  category_id: int, description: str, color: str, tags: str):
        self.id = id,
        self.instrument_name = instrument_name
        self.manufacturer_id = manufacturer_id
        self.category_id = category_id
        self.description = description
        self.color = color
        self.tags = tags
    
    def serialize(self):
        return {
            'instrument_name': self.instrument_name,
            'manufacturer_id' : self.manufacturer_id,
            'category_id' : self.category_id,
            'description' : self.description,
            'color' : self.color,
            'tags' : self.tags.split(','),
            'id': self.id[0]
        }