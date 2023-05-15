import openai

openai.api_key = "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"

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


audio_file = open("test.mp4", "rb")
transcript_text = openai.Audio.transcribe(
    "whisper-1",
    audio_file,
    prompt="句読点ごとで改行してください"
)["text"]
print(transcript_text)

prompt = f"以下の文章は動画を文章化したものなので、動画の弾幕の形で評価して、弾幕の要求はネットスラングをつけて、できれば短くい。それで20個の日本語の弾幕を出力してください: {transcript_text}"
response = get_completion(prompt)
print(response)

# ChatGPTで生成した文章
generated_text = response.split("\n")  # 改行で文章を分割

# HTMLコード
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Video with Chat Subtitles</title>
  <style>
    #subtitle {{
      white-space: pre-line;
      font-size: 24px;
      margin-top: 20px;
    }}
  </style>
  <script>
    function showSubtitles() {{
      var subtitles = {generated_text};
      var index = 0;
      var subtitleElement = document.getElementById('subtitleElement');
      subtitleElement.innerText = subtitles[index++];
      setInterval(function() {{
        if (index < subtitles.length) {{
          subtitleElement.innerText = subtitles[index++];
        }}
      }}, 5000);  // 5秒ごとに次のサブタイトルを表示
    }}
  </script>
</head>
<body onload="showSubtitles()">
  <video controls>
    <source src="test.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <h1>Generated Subtitles:</h1>
  <p id="subtitleElement"></p>
</body>
</html>
"""

# HTMLコードを保存
with open("index.html", "w") as file:
    file.write(html_code)