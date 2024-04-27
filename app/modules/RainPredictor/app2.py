from fastapi import APIRouter, Depends, HTTPException
from .EjercicioStrategy import PrediccionClimaSimple, PrediccionClimaAvanzada, PrediccionClima
from enum import Enum


class Predicciones(Enum):
    SIMPLE = "simple"
    AVANZADA = "avanzada"
    PRONOSTICO = "pronostico"


def get_pronostico(predicciones: Predicciones) -> PrediccionClima:
    if predicciones == Predicciones.SIMPLE:
        return PrediccionClimaSimple()
    elif predicciones == Predicciones.AVANZADA:
        return PrediccionClimaAvanzada()
    elif predicciones == Predicciones.PRONOSTICO:
        return PrediccionClima()
    else:
        raise HTTPException(status_code=400, detail="Prediccion Invalida")


router = APIRouter()


@router.get("/Predecir_Simple")
def PredecirSimple(predicciones: PrediccionClima = Depends(get_pronostico)) -> None:
    return predicciones.llovera


@router.get("/Predecir_Avanzada")
def PredecirAvanzada(predicciones: PrediccionClima = Depends(get_pronostico)) -> None:
    return predicciones.llovera


@router.get("/Predecir_General")
def predecir(predicciones: PrediccionClima = Depends(get_pronostico)) -> None:
    return predicciones.llovera
