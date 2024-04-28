from fastapi import APIRouter, Depends, HTTPException
from .strategy import SoccerWeight, BasketWeight, VolleyWeight, SportsWeight
from enum import Enum


class Sports(Enum):
    SOCCER = "soccer"
    BASKET = "basket"
    VOLEY = "voley"


def get_weight(sports: Sports) -> SportsWeight:
    if sports == Sports.SOCCER:
        return SoccerWeight()
    elif sports == Sports.BASKET:
        return BasketWeight()
    elif sports == Sports.VOLEY:
        return VolleyWeight()
    else:
        raise HTTPException(status_code=400, detail="Invalid Sport")


router = APIRouter()


@router.get("/Type_Sport")
def Type_Sport(wheigth: int, height: int, sports: SportsWeight = Depends(get_weight)) -> dict:
    return sports.get_Type_Sport(wheigth=wheigth, height=height)

@router.get("/Classification_Sport")
def Classification_Sport(wheigth: int, height: int, sports: SportsWeight = Depends(get_weight)) -> dict:
    return sports.get_Clasification_Sport(wheigth=wheigth, height=height)
