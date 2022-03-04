"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from Bonten import ALIVE_NAME
from Bonten.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

PHOTO ="https://te.legra.ph/file/eddaf02a24644be224b2a.mp4"
@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit(PHOTO , " `Currently Alive, my  master!` ****\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot created by:` [Bonten Network](https://t.me/Bonten_community)\n"
                     f"`My  owner`: {DEFAULTUSER}\n\n")
