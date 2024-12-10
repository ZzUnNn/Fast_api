from tortoise.models import Model
from tortoise import fields


class Student (Model):
    id=fields.IntField(pk=True)
    student_name=fields.CharField(max_length=32,description="学生名字")
    student_ID=fields.IntField(description="学号")
    
    group=fields.ForeignKeyField("models.Group",related_name="students")# 一对多

class Group(Model):
    id=fields.IntField(pk=True)
    group_member = fields.CharField(max_length=255, null=False)
    group_id=fields.IntField(description="组号")
    

