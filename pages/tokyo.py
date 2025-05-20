import streamlit as st
import folium
from streamlit_folium import folium_static

# 도쿄 여행지 데이터 (위도, 경도, 사진 URL)
tourist_spots = [
    {"name": "도쿄 타워", "lat": 35.6586, "lon": 139.7454, "photo_url": "https://example.com/tokyo_tower.jpg", "description": "도쿄의 상징적인 랜드마크"},
    {"name": "아사쿠사", "lat": 35.7148, "lon": 139.7967, "photo_url": "https://example.com/asakusa.jpg", "description": "역사적인 사찰인 센소지와 유명한 쇼핑거리"},
    {"name": "신주쿠 교엔", "lat": 35.6852, "lon": 139.7103, "photo_url": "https://example.com/shinjuku_gyoen.jpg", "description": "도쿄의 아름다운 정원"},
    {"name": "하라주쿠", "lat": 35.6714, "lon": 139.7021, "photo_url": "https://example.com/harajuku.jpg", "description": "젊은이들의 패션 중심지"},
    {"name": "우에노 공원", "lat": 35.7138, "lon": 139.7773, "photo_url": "https://example.com/ueno_park.jpg", "description": "동물원과 박물관이 있는 큰 공원"},
    {"name": "오다이바", "lat": 35.6192, "lon": 139.7767, "photo_url": "https://example.com/odaiba.jpg", "description": "미래적이고 쇼핑과 놀이가 어우러진 해양 도시"},
    {"name": "도쿄 디즈니랜드", "lat": 35.6329, "lon": 139.8804, "photo_url": "https://example.com/disneyland.jpg", "description": "세계적으로 유명한 테마파크"}
]

# 도쿄의 중심 위치 설정
map_center = [35.6762, 139.6503]
m = folium.Map(location=map_center, zoom_start=12)

# 각 여행지에 마커 추가
for spot in tourist_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"""
        <b>{spot['name']}</b><br>
        <img src="{spot['photo_url']}" width="200" height="150"><br>
        {spot['description']}
        """,
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Streamlit에서 folium 지도 렌더링
st.write("### 도쿄 유명 여행지들")
folium_static(m)
