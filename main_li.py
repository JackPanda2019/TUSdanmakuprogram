<!DOCTYPE html>
<html>
<head>
  <title>Video with Chat Subtitles</title>
  <style>
    #subtitle {
      white-space: pre-line;
      font-size: 24px;
      margin-top: 20px;
    }
  </style>
  <script>
    function showSubtitles() {
      var subtitles = `{{ generated_text }}`;
      var index = 0;
      var subtitleElement = document.getElementById('subtitle');
      subtitleElement.innerText = subtitles[index++];
      setInterval(function() {
        if (index < subtitles.length) {
          subtitleElement.innerText = subtitles[index++];
        }
      }, 5000);  // 每隔5秒显示下一个字幕
    }
  </script>
</head>
<body onload="showSubtitles()">
  <video controls>
    <source src="video/トランプ大統領誕生　「米国第一」宣言.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <h1>Generated Subtitles:</h1>
  <p id="subtitle"></p>
</body>
</html>
