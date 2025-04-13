#!/usr/bin/env python
import os
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from meeting_minutes.crews.meeting_minutes_crew.meeting_minutes_crew import MeetingMinutesCrew
from meeting_minutes.crews.gmailcrew.gmailcrew import GmailCrew
from openai import OpenAI
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path
import agentops


class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating transcription")

        SCRIPT_DIR = Path(__file__).parent
        audio_path = str(SCRIPT_DIR / "EarningsCall.wav")

        # client = OpenAI()
        # audio_file = AudioSegment.from_file(audio_path, format="wav")

        # chunk_length_ms = 60000
        # chunks = make_chunks(audio_file, chunk_length_ms)

        full_transcript = "Good afternoon, everyone, and welcome to FinTech Plus Sync's 2nd quarter 2023 earnings call. I'm John Doe, CEO of FinTech Plus. We've had a stellar Q2 with a revenue of $125 million, a 25% increase year over year. Our gross profit margin stands at a solid 58%, due in part to cost efficiencies gained from our scalable business model. Our EBITDA has surged to $37.5 million, translating to a remarkable 30% EBITDA margin. Our net income for the quarter rose to $16 million, which is a noteworthy increase from $10 million in Q2 2022. Our total addressable market has grown substantially, thanks to the expansion of our high-yield savings product line and the new RoboAdvisor platform. We've been diversifying our asset-backed securities portfolio, investing heavily incollateralized debt obligations and residential mortgage-backed securities. We've also invested $25 million in AAA-rated corporate bonds, enhancing our risk-adjusted returns. As for our balance sheet, total assets reached $1.5 billion with total liabilities at $900 million, leaving us with a solid equity base of $600 million. Our debt to equity ratio stands at 1.5, a healthy figure considering our expansionary phase. We continue to see substantial organic user growth, with customer acquisition cost dropping by 15% and lifetime value growing by 25%. Our LTVCAC ratio is at an impressive 3.5x. In terms of risk management, we have a value-at-risk model in place with a99% confidence level indicating that our maximum loss will not exceed 5 million in the next trading day. We've adopted a conservative approach to managing our leverage and have a healthy tier one capital ratio of 12.5%. Our forecast for the coming quarter is positive. We expect revenue to be around 135 million and 8% quarter over quarter growth driven primarily by our cutting edge blockchain solutions and AI driven predictive analytics. We're also excited about the upcoming IPO of our FinTech subsidiary Pay Plus, which we expect to raise 200 million. Significantly bolstering our liquidity and paving the way for aggressive growth strategies. We thank our shareholders for their continued faith in us and we look forward to an even more successful Q3. Thank you so much."

        # for i, chunk in enumerate(chunks):
        #     print(f"Transcribing chunk {i}")
        #     chunk_path = f"chunk{i}.wav"
        #     chunk.export(chunk_path, format="wav")

        #     with open(chunk_path, "rb") as audio_file:
        #         transcription = client.audio.transcriptions.create(
        #             model="whisper-1",
        #             file=audio_file
        #         )
        #         full_transcript += transcription.text

        # print(full_transcript)
        self.state.transcript = full_transcript

    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        print("Generating meeting minutes")

        inputs = {
            "transcript": self.state.transcript
        }
        
        crew = MeetingMinutesCrew()
        minutes = crew.crew().kickoff(inputs)
        self.state.meeting_minutes = minutes # type: ignore

        print("Meeting minutes generated")

    @listen(generate_meeting_minutes)
    def create_draft_meeting_minutes(self):
        print(f"Meeting minutes: {self.state.meeting_minutes}")
        # print("Creating Draft Meeting Minutes")

        crew = GmailCrew()

        inputs = {
            "body": "This is a test email"
        }

        draft_crew = crew.crew().kickoff(inputs)
        # print(f"Draft Crew: {draft_crew}")
        


def kickoff():
    session = agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"), skip_auto_end_session=True)
    meeting_minutes_flow = MeetingMinutesFlow()
    meeting_minutes_flow.kickoff()

    session.end_session() # type: ignore

if __name__ == "__main__":
    kickoff()
