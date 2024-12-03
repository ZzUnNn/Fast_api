from tortoise import Tortoise
import asyncio

async def init():
    await Tortoise.init(
        db_url='mysql://root:1298808625@host:3306/fastapi',  # 替换为你的 MySQL 连接信息
        modules={'models': ['models']}  # 替换为你的模型路径
    )
    await Tortoise.generate_schemas()

# 运行初始化函数
asyncio.run(init())