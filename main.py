
import streamlit as st
import folium
from folium import plugins
from streamlit_folium import folium_static

# Streamlit 앱 제목
st.title("천문관측이 가능한 곳 지도")

# 지도 기본 위치 설정 (예: 서울)
map_center = [37.5665, 126.9780]  # 서울의 위도와 경도
m = folium.Map(location=map_center, zoom_start=10)

# 천문관측이 가능한 곳 리스트
observatories = [
    {"name": "국립관상대", "lat": 37.5820, "lon": 126.9770, "description": "서울에 위치한 천문학 연구 및 교육기관"},
    {"name": "경기도립과학관", "lat": 37.2847, "lon": 127.1280, "description": "경기도 용인에 위치한 천문학 및 과학 교육 기관"},
    {"name": "정확산 천문대", "lat": 34.9815, "lon": 126.7444, "description": "전라남도 나주에 위치한 천문대, 어두운 하늘에서 별 관측"},
    {"name": "한라산 천문대", "lat": 33.3617, "lon": 126.5283, "description": "제주도의 한라산 정상에 위치한 천문대"},
    {"name": "기상청 제주도 천문대", "lat": 33.3600, "lon": 126.5100, "description": "기상청 운영 천문대, 제주도 천문학 연구 및 관측"},
    {"name": "파주 천문대", "lat": 37.7554, "lon": 126.7445, "description": "경기도 파주에 위치한 천문대, 다양한 천문학 프로그램 제공"},
    {"name": "서울시립과학관", "lat": 37.5512, "lon": 126.9882, "description": "서울시립과학관, 대중을 위한 천문 관측 프로그램 제공"}
]

# 천문관측 장소 마커 추가
for observatory in observatories:
    folium.Marker(
        location=[observatory["lat"], observatory["lon"]],
        popup=f"<b>{observatory['name']}</b><br>{observatory['description']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Streamlit에서 folium 지도 렌더링
st.write("### 천문관측이 가능한 장소들")
folium_static(m)
