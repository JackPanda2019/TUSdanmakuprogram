import moviepy.editor as mp
import openai
import time

# OpenAI API key
openai.api_key = "OPENAI_API_KEY"

# Load video and extract audio
video_path = "https://replit.com/@jackpanda1311/TUSdanmakuprogram?from=notifications#video/Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up%20(Official%20Music%20Video).mp4"
video = mp.VideoFileClip(video_path)
audio = video.audio

# Split audio into 5 second chunks
audio_chunks = []
start_time = 0
end_time = 5
while end_time <= audio.duration:
    audio_chunk = audio.subclip(start_time, end_time)
    audio_chunks.append(audio_chunk)
    start_time += 5
    end_time += 5

# Convert each audio chunk to text and get response from OpenAI API
for i, chunk in enumerate(audio_chunks):
    chunk_path = f"path/to/audio_chunk_{i}.wav"
    chunk.write_audiofile(chunk_path)
    with open(chunk_path, "rb") as f:
        transcript_text = openai.Audio.transcribe("whisper-1", f)["text"]
    response = get_completion("以下の文章を要約してください。:" + transcript_text)
    print(f"Response {i}: {response}")
    time.sleep(1)  # Wait 1 second to avoid API rate limit
