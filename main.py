import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from apps.app import foot_table,order,customer

app = FastAPI()

app.include_router(foot_table, prefix="/food", tags=["菜单"])
app.include_router(order, prefix="/order", tags=["订单"])
app.include_router(customer, prefix="/customer", tags=["客户"])

# fastapi一旦运行，register_tortoise已经执行，实现监控
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8010, reload=True, workers=1)
