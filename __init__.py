import random
import os
from pathlib import Path
import re
import nonebot
from typing import Type
from nonebot.typing import T_State
from nonebot import on_command, on_regex
from nonebot.params import CommandArg, ArgStr
from nonebot.adapters.onebot.v11.event import Event
from nonebot.adapters.onebot.v11 import Bot,Message, MessageEvent
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, GROUP

__zx_plugin_name__ = "每日发癫"
__plugin_usage__ = """
usage：
    每日发癫魔楞语句
    指令：
        每日发癫（参数）
""".strip()
__plugin_des__ = "每日发癫"
__plugin_cmd__ = ["每日发癫/阿咪"]
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["每日发癫", "阿咪"],
}
__plugin_block_limit__ = {"rst": "每日发癫！"}

aya = on_regex("^(每日发癫|阿咪)$", priority=5, block=True)
aya = on_command("每日发癫", aliases={"每日发癫"}, priority=5, block=True)

try:
    import ujson as json
except ModuleNotFoundError:
    import json

global_config = nonebot.get_driver().config
if not hasattr(global_config, "aya_path"):
    aya_PATH = os.path.join(os.path.dirname(__file__), "resource")
else:
    aya_PATH = global_config.aya_path
    

@aya.handle()
async def _(bot: Bot, event: MessageEvent,arg: Message = CommandArg()):
    isaya = re.search(r'每日发癫|阿咪]', event.get_plaintext())
    msg = arg.extract_plain_text().strip()
    cost = str(msg)
    # json数据存放路径
    filePath = Path(aya_PATH) / "post.json"
    # 将json对象加载到数组
    with open(filePath, "r", encoding="utf-8") as f:
        ayanami = json.load(f).get("post")
    # 随机选取数组中的一个对象
    randomPost = random.choice(ayanami).replace("阿咪", cost)
    await aya.finish(randomPost)
