from pathlib import Path
from openai import OpenAI

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Olá, eu sou um bot de texto para fala, o que eu estou dizendo agora foi gerado por um texto e com a ajuda da OpenAI."
)

response.stream_to_file(speech_file_path)