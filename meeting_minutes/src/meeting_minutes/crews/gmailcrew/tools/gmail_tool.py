from typing import Type

from crewai.tools import BaseTool
from litellm import add_message
from meeting_minutes.crews.gmailcrew.tools.gmail_utility import authenticate_gmail, create_draft, create_message
from pydantic import BaseModel, Field

class GmailToolInput(BaseModel):
    """Input schema for GmailTool."""

    body: str = "This is a test email"

# @record_tool("This is used for gmail tool")
class GmailTool(BaseTool):
    name: str = "GmailToll"
    description: str = (
        "Send an email to the client with the meeting minutes using the provide body: {body}"
    )
    args_schema: Type[BaseModel] = GmailToolInput

    def _run(self, body: str) -> str:
        try:
            service = authenticate_gmail()

            sender = "davidmaignan@gmail.com"
            to = "davidmaignan@gmail.com"
            subject = "Meeting Minutes"
            message_body = body

            message = create_message(sender, to, subject, message_body)
            draft = create_draft(service, "me",message)
            return f"Email sent successfully: {draft['id']}" # type: ignore
        except Exception as e:
            return f"Error sending email: {e}"
