class ManufacturerModel:
    manufacturer_id: int
    manufacturer_name: str

    def __init__(
        self,
        manufacturer_id: int,
        manufacturer_name: str,
    ):
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name

    def serialize(self):
        return {
            "manufacturer_id": self.manufacturer_id,
            "manufacturer_name": self.manufacturer_name,
        }
