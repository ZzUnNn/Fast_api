from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import *
group_api=APIRouter()
# @group_api.get("/")
# async def getAll_grp():
#     return {
#         "操作":"查看所有组"
#     }
# @group_api.put("/")
# async def update_grp():
#     return {
#          "操作":"更新组"
#     }
# @group_api.post("/")
# async def add_grp():
#     return {
#         "操作":"增加组"
#     }
# @group_api.delete("/{group_number}")
# async def delete_grp(group_number:int):
#     return{
#         "操作":"删除一个组"
#     }
# @group_api.get("/{group_number}")
# async def get_a_grp(group_number:int):
#     return{
#         "操作":"查看一个组"
#     }




#创建群组
class GroupCreate(BaseModel):
    id:int
    group_member: str
    group_id:int
    
@group_api.post("/")
async def create_group(group: GroupCreate):
    group_obj = await Group.create(
        group_member=group.group_member,
        group_id=group.group_id,
        id=group.id  # 确保这里使用正确的字段名
    )
    return group_obj
#按 ID 获取有关组的信息
@group_api.get("/{id}")
async def read_group(id: int):
    group = await Group.get(id=id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"id": group.id, "group_member": group.group_member}

#删除组
@group_api.delete("/{id}")
async def delete_group(id: int):
    group = await Group.get(id=id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    await group.delete()
    return {"message": "Group deleted"}
#获取组列表
@group_api.get("/")
async def list_groups():
    groups = await Group.all()
    return [{"id": group.id, "group_member": group.group_member} for group in groups]