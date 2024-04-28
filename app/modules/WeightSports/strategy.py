from abc import ABC, abstractmethod

class SportsWeight(ABC):
    @abstractmethod
    def get_type_Sport(self, weight: float, height: float) -> dict:
        pass

    @abstractmethod
    def get_Classification_Sport(self, weight: float, height: float) -> dict:
        pass

class SoccerWeight(SportsWeight):
    def get_type_Sport(self, weight: float, height: float) -> dict:
        return {"weight": weight, "height": height}

    def get_Classification_Sport(self, weight: float, height: float) -> dict:
        category = ""
        if weight < 60:
            category = "Categoría A"
        elif weight > 70:
            category = "Categoría B"
        else:
            category = "Categoría Intermedia"

        if height < 170:
            height_category = "Baja"
        elif height > 179:
            height_category = "Alta"
        else:
            height_category = "Intermedia"

        return {"weight": weight, "height": height, "weight_category": category, "height_category": height_category}

class BasketWeight(SportsWeight):
    def get_type_Sport(self, weight: float, height: float) -> dict:
        return {"weight": weight, "height": height}

    def get_Classification_Sport(self, weight: float, height: float) -> dict:
        category = ""
        if weight < 90:
            category = "Categoría A"
        elif weight > 120:
            category = "Categoría B"
        else:
            category = "Categoría Intermedia"

        if height < 195:
            height_category = "Baja"
        elif height > 220:
            height_category = "Alta"
        else:
            height_category = "Intermedia"

        return {"weight": weight, "height": height, "weight_category": category, "height_category": height_category}

class VolleyWeight(SportsWeight):
    def get_type_Sport(self, weight: float, height: float) -> dict:
        return {"weight": weight, "height": height}

    def get_Classification_Sport(self, weight: float, height: float) -> dict:
        category = ""
        if weight < 70:
            category = "Categoría A"
        elif weight > 90:
            category = "Categoría B"
        else:
            category = "Categoría Intermedia"

        if height < 180:
            height_category = "Baja"
        elif height > 194:
            height_category = "Alta"
        else:
            height_category = "Intermedia"

        return {"weight": weight, "height": height, "weight_category": category, "height_category": height_category}