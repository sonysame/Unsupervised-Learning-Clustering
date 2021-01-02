# Unsupervised-Learning-Clustering

비지도학습 - 클러스터링(Clustering), 차원압축(Dimensionality Reduction), 이상감지(Anomaly Detection)

입력데이터 X를 사용하지만, 클래스 데이터 T는 사용하지 않는다.<br/>
#### 클러스터링: 클래스 정보 없이, 입력 데이터가 비슷한 것끼리 클래스로 나누는 것

지도 학습 문제는 클래스가 있는 데이터였고, 미지의 x에 대한 클래스를 예측하는 것이 목적이었다<br/>

클러스터링의 대표적인 알고리즘 -> **K-means 기법, 가우시안 혼합 모델**

## K-means 기법
### Step 0: 변수의 준비와 초기화
Mu: 클러스터의 중심 벡터, R: 각 데이터의 클래스 지시 변수
![image](https://user-images.githubusercontent.com/24853452/103458098-2d6c7a00-4d48-11eb-88e2-060f4a6d0b06.png) {:.alignleft}

### Step 1: R의 갱신
각 데이터 점을 가장 중심이 가까운 클러스터에 넣어 R을 갱신
![image](https://user-images.githubusercontent.com/24853452/103458101-36f5e200-4d48-11eb-9890-832b408f528e.png) {:.
