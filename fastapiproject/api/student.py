
from pydantic import BaseModel
from models import *
from fastapi import APIRouter, HTTPException, Path
from tortoise.exceptions import DoesNotExist
student_api=APIRouter()
# @student_api.get("/")
# async def getAll_stu():
#     students=await Student.all()
    
#     return students
    
# @student_api.put("/")
# async def update_stu():
#     return {
#          "操作":"改学生"
#     }
# @student_api.post("/")
# async def add_stu():
#     return {
#         "操作":"增加学生"
#     }
# @student_api.delete("/{student_ID}")
# async def delete_stu(student_number:int):
#     return{
#         "操作":"删除一个学生"
#     }
# @student_api.get("/{student_ID}")
# async def get_a_stu(student_number:int):
#     return{
#         "操作":"查看一个学生"
#     }

#创建学生
class StudentCreate(BaseModel):
    id: int
    student_name: str
    student_ID: int
    group_id: int

@student_api.post("/")
async def create_student(student: StudentCreate):
    student_obj = await Student.create(
        student_name=student.student_name,
        student_ID=student.student_ID,
        group_id=student.group_id,
        id = student.id                   # 确保这里使用正确的字段名
    )
    return student_obj



#通过学生的 ID 获取有关学生的信息
@student_api.get("/{student_ID}")
async def read_student(student_ID: int):
    student = await Student.get(id=student_ID)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student



#移除学生
@student_api.delete("/{student_ID}")
async def delete_student(student_ID: int):
    student = await Student.get(id=student_ID)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    await student.delete()
    return {"message": "Student deleted"}



#获取学生名单
@student_api.get("/")
async def list_students():
    students = await Student.all()
    return students

#获取组的所有学生
@student_api.get("/{group_id}/students/")
async def read_group_students(group_id: int):
    try:
        # 查询特定组的所有学生
        students = await Student.filter(group=group_id).all()
        print(students)
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#添加学生到组
@student_api.put("/{student_ID}/group/{group_id}")
async def add_student_to_group(student_ID: int, group_id: int):
    student = await Student.get(id=student_ID)
    group = await Group.get(id=group_id)
    if not student or not group:
        raise HTTPException(status_code=404, detail="Student or Group not found")
    student.group = group
    await student.save()
    return {"message": "Student added to group"}


#将学生从A转到B
@student_api.put("/student/{student_ID}/group/{from_group_id}/to/{to_group_id}")
async def move_student_between_groups(student_ID: int, from_group_id: int, to_group_id: int):
    student = await Student.get(id=student_ID)
    to_group = await Group.get(id=to_group_id)
    if not student or not to_group:
        raise HTTPException(status_code=404, detail="Student or Group not found")
    student.group = to_group
    await student.save()
    return {"message": "Student moved to new group"}
#REMOVE
@student_api.delete("/{student_id}/group/{group_id}", response_model=dict)
async def remove_student_from_group(student_id: int = Path(..., description="The ID of the student"), group_id: int = Path(..., description="The ID of the group")):
    try:
        # 尝试获取学生
        student = await Student.get(id=student_id)
        # 尝试获取组
        group = await Group.get(id=group_id)
        
        # 检查学生是否属于该组
        if student.group_id != group.id:
            raise HTTPException(status_code=400, detail="Student is not in the specified group")
        
        # 从组中移除学生
        student.group_id = None  # 将外键设置为 None
        await student.save()
        
        return {"message": "Student removed from group"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Student or Group not found")
