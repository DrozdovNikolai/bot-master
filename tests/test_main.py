import pytest
from telegram import User, Update, Message, Chat
from telegram.ext import Application, ContextTypes
from krddevbot.__main__ import help_command

class MockUpdate:
    def __init__(self):
        self.message = MockMessage()

class MockMessage:
    def __init__(self):
        self.text = "ping"
        self.chat_id = 12345
        self.message_id = 1
        self.chat = MockChat()
    
    async def reply_text(self, text, parse_mode=None):
        pass

class MockChat:
    def __init__(self):
        self.id = 12345

class MockContext:
    def __init__(self):
        self.bot = None
        self.job_queue = None

@pytest.mark.asyncio
async def test_help_command():
    update = MockUpdate()
    context = MockContext()
    await help_command(update, context)
    assert update.message.text == "ping"

