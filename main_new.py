import openai
import json

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

# 将生成的文本转换为JSON字符串
generated_text_json = json.dumps(generated_text)

# 修改生成的文本字符串中的反斜杠
generated_text_json = generated_text_json.replace("\\", "\\\\")

# HTML代码

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
    body {{
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
    }}
    #video-container {{
      width: 60%;
      margin-left: 20px;
    }}
    #subtitle-container {{
      width: 35%;
      margin-right: 20px;
      text-align: left;
    }}
    video {{
      width: 100%;
    }}
    #subtitle-history-container {{
      height: 200px;
      overflow: auto;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      display: flex;
      flex-direction: column-reverse;
    }}
  </style>
  <script>
    function showSubtitles() {{
      var subtitles = JSON.parse(`{generated_text_json}`);
      var subtitleHistoryElement = document.getElementById('subtitleHistoryElement');

      setInterval(function() {{
        if (subtitles.length > 0) {{
          var subtitle = subtitles.shift();
          subtitleHistoryElement.innerHTML += '<p>' + subtitle + '</p>';
          subtitleHistoryElement.scrollTop = subtitleHistoryElement.scrollHeight;
        }}
      }}, 1000);
    }}
  </script>
</head>
<body onload="showSubtitles()">
  <div id="video-container">
    <video controls>
      <source src="static/トランプ大統領誕生　「米国第一」宣言.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div id="subtitle-container">
    <h1>Generated Comments:</h1>
    <div id="subtitle-history-container">
      <p id="subtitleHistoryElement"></p>
    </div>
  </div>
</body>
</html>
"""

# HTML代码保存到文件
with open("index.html", "w") as file:
    file.write(html_code)