import streamlit as st
import pandas as pd
import folium
from folium import plugins
import requests

# 파일 URL (GitHub에 저장된 파일)
file_url = "https://raw.githubusercontent.com/skywind99/25vibecoding1/main/pages/학교기본정보_2025년4월30일기준.csv"

# CSV 파일을 GitHub에서 읽어오기
@st.cache
def load_data():
    response = requests.get(file_url)
    data = pd.read_csv(pd.compat.StringIO(response.text), encoding='cp949')
    return data

# 데이터 로드
data = load_data()

# 데이터 확인
st.write(data.head())

# 학교 위치 데이터 추출
schools = data[['학교명', '도로명우편번호', '시도명']].dropna(subset=['도로명우편번호'])

# 서울을 중심으로 지도 초기화
map_center = [37.5665, 126.9780]  # 서울의 위도, 경도
map = folium.Map(location=map_center, zoom_start=12)

# 학교 위치를 지도에 표시 (위도/경도 변환은 외부 API로 처리 가능)
for _, row in schools.iterrows():
    # 실제로는 도로명우편번호나 다른 주소 정보를 이용해 위도/경도를 구해야 합니다.
    folium.Marker(
        location=[map_center[0], map_center[1]],  # 실제로는 geocoding을 통해 위도, 경도를 구할 수 있습니다.
        popup=row['학교명']
    ).add_to(map)

# Streamlit에서 folium 맵을 표시
st.write("### 학교 위치 지도")
folium.plugins.Fullscreen().add_to(map)  # 전체 화면 모드 기능 추가
folium_static(map)
