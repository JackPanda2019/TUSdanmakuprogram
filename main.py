import openai
import json

openai.api_key = "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"

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.7):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

audio_file = open("video/トランプ大統領誕生　「米国第一」宣言.mp4", "rb")
transcript_text = openai.Audio.transcribe(
    "whisper-1",
    audio_file,
    prompt="句読点ごとで改行してください"
)["text"]
print(transcript_text)

prompt = f"今は、自分が日本人として想像して、以下の文章は動画を文章化したものなので、弾幕の形で評価したい、弾幕の要求は日本語で、若者の立場でネットスラングを使用する、できれば違う弾幕書いて、絵文字を適当に使う、反対の弾幕も適当に作る。日本人の立場で考える、簡潔な言葉で書く。50個の弾幕を出力してください: {transcript_text}"

prompt2 = f"现在想象你是一个中国人，以下的文章是视频提取而成的，对于这个视频，你需要用弹幕的形式评论，弹幕的要求是：使用中文，可以添加表情，用网络用语，年轻人的口气，尽可能短和简洁，站在中国人的立场思考，可以有负面的评论。请给我五十个弹幕: {transcript_text}"

prompt3 = f"今は、自分がアメリカ人として想像して、以下の文章は動画を文章化したものなので、弾幕の形で評価したい、弾幕の要求は英語で、若者の立場でネットスラングを使用する、できれば違う弾幕書いて、絵文字を適当に使う、反対の弾幕も適当に作る。アメリカ人の立場で考える、簡潔な言葉で書く。50個の弾幕を出力してください: {transcript_text}"

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
      <source src="トランプ大統領誕生　「米国第一」宣言.mp4" type="video/mp4">
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
  