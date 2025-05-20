import streamlit as st
import pandas as pd
import plotly.express as px

# GitHub raw URL
file_url = "https://raw.githubusercontent.com/skywind99/25vibecoding1/main/pages/202504_202504_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%85%E1%85%A7%E1%86%BC%E1%84%87%E1%85%A7%E1%86%AF%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB%E1%84%92%E1%85%AA%E1%86%BC_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%80%E1%85%A1%E1%86%AB.csv"

# CSV 파일 로드
data_1 = pd.read_csv(file_url, encoding='ISO-8859-1')

# 실제 데이터의 컬럼 수 확인
st.write("파일의 컬럼명:", data_1.columns)

# 데이터 확인
st.write("파일의 일부 데이터:", data_1.head())

# 컬럼명 변경을 시도하기 전에 컬럼 수 확인
# data_1.columns = ['적절한 컬럼명 나열']

# 필요한 컬럼만 추출하여 시각화 (이 부분은 데이터를 기반으로 맞춤화 필요)
# data_1_filtered = data_1[['지역', '2025년04월_0~9', '2025년04월_10~19', ...]]

# 숫자 데이터로 변환
# data_1_filtered = data_1_filtered.apply(pd.to_numeric, errors='coerce')

# Plotly로 연령대별 인구 분포 시각화
# fig = px.bar(data_1_filtered, x='지역', y=['2025년04월_0~9', ...], title="연령대별 인구 분포", barmode='stack')

# st.plotly_chart(fig)
