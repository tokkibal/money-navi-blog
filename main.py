# main.py
# 구글 트렌드 기반 최신 기사 3개 + 해시태그 10개 포함 HTML 생성
# 실제 데이터 수집은 pytrends, requests, BeautifulSoup 등을 활용해야 함
# 여기서는 구조 예시로 작성

from collections import Counter
import re

# 예시 데이터 (실제로는 pytrends/크롤링으로 가져옴)
titles = [
    "[머니네비] 글로벌 방산 협력 확대 속에서 '팔란티어'가 AI 전략으로 투자자 관심을 모은다",
    "[머니네비] 조선업 가치사슬 재평가 움직임, 사흘 새 2조원 수주한 '한화오션'이 중심에 선다",
    "[머니네비] 생성형 AI 경쟁 구도 흔드는 '앤트로픽', 대규모 투자 유치로 시장 판도 바꾼다"
]

summaries = [
    "팔란티어가 방산 분야에서 AI 협력을 확대하며 글로벌 투자자들의 주목을 받는다. 데이터 기반 국방 전략이 새로운 성장 동력으로 부각된다.",
    "한화오션이 단기간에 대형 수주를 기록하며 국내 증시와 기자재 가치사슬에 큰 영향을 준다. 조선업 전반의 재평가 움직임이 나타난다.",
    "앤트로픽이 대규모 투자를 유치하며 생성형 AI 시장 경쟁 구도를 흔든다. 투자자들은 차세대 AI 기업의 성장 가능성을 주목한다."
]

image_urls = [
    "https://example.com/palantir.png",
    "https://example.com/hanwha_ocean.png",
    "https://example.com/anthropic.png"
]

sources = ["블룸버그", "연합뉴스", "로이터"]

# 해시태그 자동 생성 함수
def generate_hashtags(text):
    words = re.findall(r"[가-힣A-Za-z0-9]+", text)
    common = [w for w in words if len(w) > 2]
    counter = Counter(common)
    top10 = [f"#{w}" for w, _ in counter.most_common(10)]
    return top10

# HTML 생성
html_template = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>머니네비 최신 이슈</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h2 { color: #2c3e50; }
        p { margin: 10px 0; }
        img { max-width: 600px; display:block; margin:auto; }
        .source { font-size:12px; text-align:center; color:#555; }
        .hashtags { font-size:13px; color:#0073e6; margin-top:10px; }
        hr { margin:30px 0; }
    </style>
</head>
<body>
"""

for i in range(3):
    hashtags = generate_hashtags(titles[i] + " " + summaries[i])
    html_template += f"""
    <h2>{titles[i]}</h2>
    <p>{summaries[i]}</p>
    <img src="{image_urls[i]}" alt="썸네일 이미지">
    <p class="source">출처: {sources[i]}</p>
    <p class="hashtags">{' '.join(hashtags)}</p>
    <hr>
    """

html_template += """
</body>
</html>
"""

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("output.html 파일 생성 완료!")
