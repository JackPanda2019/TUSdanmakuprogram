import openai

openai.api_key = "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"


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=
    temperature,  # this is the degree of randomness of the model's output
  )
  return response.choices[0].message["content"]

with open("video/Rick Astley - Never Gonna Give You Up (Official Music Video).mp4", "rb") as f:
  transcript_text = openai.Audio.transcribe("whisper-1", f)["text"]

print(transcript_text)