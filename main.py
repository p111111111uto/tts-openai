from pathlib import Path
from openai import OpenAI

client=OpenAI(api_key="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")

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="echo",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
