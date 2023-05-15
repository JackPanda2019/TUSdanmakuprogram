
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
      var subtitles = {generated_text_json};
      var subtitleHistory = [];
      var index = 0;
      var subtitleElement = document.getElementById('subtitleElement');
      var subtitleHistoryElement = document.getElementById('subtitleHistoryElement');
      subtitleElement.innerText = subtitles[index++];
      subtitleHistory.push(subtitleElement.innerText);
      setInterval(function() {{
        if (index < subtitles.length) {{
          subtitleElement.innerText = subtitles[index++];
          subtitleHistory.push(subtitleElement.innerText);
          subtitleHistoryElement.innerText = subtitleHistory.join('\\n');
        }}
      }}, 5000);

      subtitleHistoryElement.innerText = subtitleHistory.join('\\n');
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
  <h2>Subtitles History:</h2>
  <p id="subtitleHistoryElement"></p>
</body>
</html>