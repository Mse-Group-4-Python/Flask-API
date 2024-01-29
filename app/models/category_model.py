class CategoryModel:
    category_id: int
    category_name: str

    def __init__(
        self,
        category_id: int,
        category_name: str,
    ):
        self.category_id = category_id
        self.category_name = category_name

    def serialize(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
        }
        pass
