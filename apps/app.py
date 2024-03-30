import uvicorn
from fastapi import FastAPI,APIRouter
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from models import *
from pydantic import BaseModel
from datetime import datetime

foot_table = APIRouter()
customer = APIRouter()
order = APIRouter()

class FoodIn(BaseModel):
    name: str
    unit_price: float
    category_id: int


class OrderIn(BaseModel):
    order_date:datetime = datetime.now()
    receive_information:str

class OrderDeatil(BaseModel):
    food_num: int = 0
    food:FoodIn
    order:OrderIn

@foot_table.get("/",tags=["获取菜单表"])
async def get_foot_table():
    food_table = await Food.all() 
    return food_table

@foot_table.post("/",tags=["新增菜品"])
async def update_foot_table(food_in:FoodIn):
    food = await Food(name=food_in.name, unit_price=food_in.unit_price, category_id=food_in.category_id)
    await food.save() 
    return food

@order.get("/",tags=["查看订单"])
async def get_order_table():
    order_table = await Order.all() 
    return order_table


@order.post("/",tags=["新增订单"])
async def add_order(order:OrderIn):
    amount = 0
    customer_id = 0
    order_table = await Order.create(order_date=order.order_date,
                                     receive_information=order.receive_information,
                                     amount=amount,
                                     Customer_id=customer_id)
    return order_table