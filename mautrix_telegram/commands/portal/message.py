# mautrix-telegram - A Matrix-Telegram puppeting bridge
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from mautrix.types import EventID

from ... import portal as po
from ...types import TelegramID
from .. import command_handler, CommandEvent, SECTION_CREATING_PORTALS
from .util import user_has_power_level, get_initial_state
from telethon import functions


@command_handler(help_section=SECTION_CREATING_PORTALS,
                 help_args="",
                 help_text="This will delete all messages and media in this chat from your Telegram cloud. Other members of the group will still have them.")
async def clear_history(evt: CommandEvent) -> EventID:
    portal = po.Portal.get_by_mxid(evt.room_id)
    if not portal:
        return await evt.reply("This is not a portal room.")

    await evt.sender.client(functions.messages.DeleteHistoryRequest(portal.peer,0,revoke=True))
    return await evt.reply("Successfully clear all messages")
