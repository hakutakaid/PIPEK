#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
from config import LOG
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"

        logger_text = f"""
**{app.mention} Play Log**

**Chat ID:** `{message.chat.id}`
**Chat Name:** {message.chat.title}
**Chat Username:** {chatusername}

**User ID:** `{message.from_user.id}`
**Name:** {message.from_user.mention}
**Username:** @{message.from_user.username}

**Query:** {message.text.split(None, 1)[1]}
**Stream Type:** {streamtype}"""
        if message.chat.id != -1002446100872:
            try:
                await app.send_message(
                    chat_id=-1002446100872,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception:
                pass
        return
