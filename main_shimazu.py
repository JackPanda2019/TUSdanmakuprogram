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
      var subtitles = ['1. アメリカを再び偉大にする！', '2. トランプ大統領、就任宣誓！', '3. アメリカ第一主義！', '4. 外国からの侵略を防ぎ、アメリカの雇用を守る！', '5. アメリカのために、貿易、税金、移民、外交政策を決定！', '6. アメリカの労働者と家族のために！', '7. 神よ、アメリカを祝福してください！', '8. アメリカ第一！', '9. トランプ大統領、アメリカを再び偉大にする！', '10. アメリカのために、全力を尽くす！', '11. アメリカのために、全てを犠牲にする！', '12. アメリカのために、戦う！', '13. アメリカのために、勝利する！', '14. アメリカのために、生きる！', '15. アメリカのために、死ぬ！', '16. アメリカのために、全てを捧げる！', '17. アメリカのために、全てをやる！', '18. アメリカのために、全てを与える！', '19. アメリカのために、全てを取り戻す！', '20. アメリカのために、全てを築く！'];
      var subtitleHistory = [];
      var index = 0;
      var subtitleElement = document.getElementById('subtitleElement');
      var subtitleHistoryElement = document.getElementById('subtitleHistoryElement');
      subtitleElement.innerText = subtitles[index++];
      subtitleHistory.push(subtitleElement.innerText);
      setInterval(function() {
        if (index < subtitles.length) {
          subtitleElement.innerText = subtitles[index++];
          subtitleHistory.push(subtitleElement.innerText);
          subtitleHistoryElement.innerText = subtitleHistory.join('\n');
        }
      }, 5000);

      subtitleHistoryElement.innerText = subtitleHistory.join('\n');
    }
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