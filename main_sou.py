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

audio_file= open("test.mp4", "rb")
transcript_text = openai.Audio.transcribe("whisper-1",audio_file)["text"]
#transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript_text)
prompt = f"以下の文章は動画を文章化したものなので、動画の弾幕の形で評価して、弾幕の要求はネットスラングをつけて、できれば短くい。それで20個の日本語の弾幕を出力してください: {transcript_text}"
response = get_completion(prompt)
print(response)

subtitles_generator = SubtitlesGenerator(response)
print(subtitles_generator)

subtitles_clips = []
for (start, end), text in subtitles_generator:
    text_clip = (TextClip(text, fontsize=30, color="white", size=video.size)
                 .set_duration(end - start)
                 .set_start(start))
    subtitles_clips.append(text_clip)

subtitles = concatenate_videoclips(subtitles_clips)
video_with_subtitles = CompositeVideoClip([video, subtitles])
video_with_subtitles.write_videofile("out.mp4")