# 选课
from tortoise.models import Model
from tortoise import fields


class Food(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="菜名")
    unit_price = fields.FloatField(description="单价")
    category = fields.ForeignKeyField("models.Category", related_name="food")

    # 一对多的关系
    # clas = fields.ForeignKeyField("models.Clas", related_name="students")

    # 多对多的关系
    # courses = fields.ManyToManyField("models.Course", related_name="students")

class Category(Model):
    id = fields.IntField(pk=True)
    category_name = fields.CharField(max_length=32, description="类别名称")


class Batching(Model):
    pass


class Order(Model):
    id = fields.IntField(pk=True)
    Customer = fields.ForeignKeyField("models.Customer", related_name="order")
    order_date = fields.DatetimeField(description="下单时间")
    receive_information = fields.CharField(max_length=64, description="收货信息")
    amount = fields.FloatField(description="总金额")


class OrderDetail(Model):
    id = fields.IntField(pk=True)
    order = fields.ForeignKeyField("models.Order", related_name="order_detail")
    food = fields.ForeignKeyField("models.Food", related_name="food")   
    food_num = fields.IntField(max_length=4, description="菜品数量")


class Customer(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    total_consumption_amount = fields.FloatField(description="消费总金额")
    consumption_frequency = fields.IntField(description="购买次数")
    preference = fields.CharField(max_length=32, description="偏好")
    customer_type = fields.CharField(max_length=32, description="客户类型")
