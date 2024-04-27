from abc import ABC, abstractmethod
import random

class PrediccionClima(ABC):
    @abstractmethod
    def llovera(self) -> bool:
        pass

class PrediccionClimaSimple(PrediccionClima):
    def llovera(self) -> bool:
        # Simulamos una predicción simple donde hay un 30% de posibilidad de lluvia
        return random.random() < 0.3

class PrediccionClimaAvanzada(PrediccionClima):
    def llovera(self) -> bool:
        # Simulamos una predicción avanzada donde hay un 60% de posibilidad de lluvia
        return random.random() < 0.6

class PronosticadorLluvia:
    def __init__(self, prediccion_clima: PrediccionClima):
        self.prediccion_clima = prediccion_clima

    def predecir(self) -> bool:
        return self.prediccion_clima.llovera()

# Ejemplo de uso
prediccion_simple = PrediccionClimaSimple()
pronosticador_simple = PronosticadorLluvia(prediccion_simple)
print("Predicción simple: ", pronosticador_simple.predecir())

prediccion_avanzada = PrediccionClimaAvanzada()
pronosticador_avanzado = PronosticadorLluvia(prediccion_avanzada)
print("Predicción avanzada: ", pronosticador_avanzado.predecir())
