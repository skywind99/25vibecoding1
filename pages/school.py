import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 파일 경로 (로컬 파일 경로로 설정)
file_path = "학교기본정보_2025년4월30일기준.csv"

# CSV 파일 불러오기
data = pd.read_csv(file_path, encoding='cp949')

# 컬럼 정리
data.columns = data.columns.str.strip()

# 하남에 위치한 중학교 및 고등학교 필터링
harman_schools = data[(data['시도명'] == '경기도') & (data['학교명'].str.contains('하남'))]

# 지도 초기화 (하남 기준)
map_center = [37.5284, 127.1440]  # 하남의 위도, 경도
map = folium.Map(location=map_center, zoom_start=12)

# 마커 클러스터 생성
marker_cluster = MarkerCluster().add_to(map)

# 필터링된 하남의 중/고등학교에 대해 마커 추가
for _, school in harman_schools.iterrows():
    school_name = school['학교명']
    school_type = school['학교종류명']
    # 학급 수를 "학급 수" 컬럼에서 가져온다고 가정 (컬럼명을 실제 데이터에 맞게 수정해야 합니다)
    num_classes = school.get('학급 수', '정보 없음')  # '학급 수' 컬럼이 없는 경우 '정보 없음'으로 설정
    location = school.get('도로명우편번호', None)  # 주소 정보가 있을 경우 이를 사용
    
    # 도로명우편번호로 위도, 경도를 변환하는 지오코딩 필요 (현재는 예시로만 작성)
    # 실제로는 geocoding API를 사용해야 합니다.
    if location:  # 도로명우편번호 또는 다른 주소 정보가 있을 때만 마커 추가
        folium.Marker(
            location=[map_center[0], map_center[1]],  # 실제로는 지오코딩을 통해 위치값을 구해야 합니다.
            popup=f"{school_name} ({school_type})\n학급 수: {num_classes}",
        ).add_to(marker_cluster)

# Streamlit UI
st.title("하남에 위치한 학교 지도")
st.write("하남에 위치한 중학교 및 고등학교의 학급 수와 위치를 지도에 표시합니다.")

# folium 맵을 Streamlit에 표시
folium_static(map)
