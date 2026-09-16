# main.py
# 간단한 HTML 파일 생성 예시

# 1. 제목, 요약, 이미지 주소를 변수로 준비한다
title = "[머니네비] 한화오션, 사흘 새 2조원 수주"
summary = "한화오션이 단기간에 대형 수주를 기록하며 국내 증시와 기자재 가치사슬에 큰 영향을 준다."
image_url = "https://example.com/hanwha_ocean.png"  # 실제 기사 썸네일 주소로 교체한다

# 2. HTML 템플릿 문자열을 만든다
html_template = f"""
<h2>{title}</h2>
<p>{summary}</p>
<img src="{image_url}" alt="썸네일 이미지" style="display:block; margin:auto;">
"""

# 3. 결과를 파일로 저장한다
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("output.html 파일을 생성한다!")
