# -*- coding: utf-8 -*-
"""221110.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OLWXbD_jJRwq9OlbsySg-K_bk69NX3UE

#### lambda 함수
- 간단한 함수인 경우 def, inline function 명령어 없이 간단히 정의해 사용
"""

def add (a, b):
  return a+b

f = lambda a, b: a+b # a, b는 인풋되는 파라미터, : 뒤에 a+b는 return되는 아웃풋
print (add(3, 5))
print (f(3, 5))

# def return_length(s):
#   return len(s)

strings = ['yoon', 'kim', 'jessica', 'jeong']
strings
# strings.sort(key=lambda s:len(s)) # strings.sort(정렬기준)
# strings.sort(len(strings)) 라고 하면 
# len은 int 타입이기 때문에 len(strings)의 리스트의 원소 개수인 4가 나옴
# sort의 정렬기준이 4가 될 수는 없다

"""#### 파이썬에 이미 정의되어 있는 함수들을 사용

##### math 함수
"""

import math

# 절대값
print (abs(-3))
# 반올림 없나?!
print (round(3.5))

# 올림
print (math.ceil(3.5))
# 내림
print (math.floor(3.3))

# sin
print (math.sin(1))
# cos
print (math.cos(1))

"""##### random 함수"""

# 로또 숫자 만들기
import random
random.sample(range(1, 46), 6)
# random.sample(몇개중에, 몇개를 뽑아라)

"""##### 딕셔너리 활용"""

from collections import defaultdict
from collections import OrderedDict
# 
D = defaultdict(int)
D2 = OrderedDict()
D2['z'] = 26
D2['a'] = 1
D2['c'] = 3
D2['d'] = 5
D2['j'] = 14
D2['b'] = 2
D2

"""##### list 복습?! 뭐여갑자기"""

# 짝수만 출력하기
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in mylist:
  if i % 2 == 0:
    print (i)

# 출력만 하는게 아니고 list로 따로 저장하기
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for i in mylist:
  if i % 2 == 0:
   even.append(i)

print (even)

#list comprehension으로
even = [i for i in mylist if i%2 == 0]
print (even)
# 5의약수= [i for i in range(1, 101) if i % 5 == 0]
# [데이터 넣을 변수∨넣을 데이터. for문 활용할거니까 for문 ∨ 조건]

# list comprehension 응용
plus2 = [i + 2 for i in mylist if i%2 == 0]
print (plus2)

"""# 패키지

## 1. 패키지와 모듈, 함수의 관계도
- 함수들이 뭉쳐진 하나의 .py 파일 안에 이루어진 것을 모듈이라고 함 ???
- 여러개의 모듈을 그룹화 하면 패키지
- 패키지를 라이브러리라고도 부름
- 모듈: 영어사전, 중국어사전..
- 패키지: 교보문고 A구역, B구역..

## 2. 모듈 import 하기

### import하는법
"""

import pandas
# pandas라는 모듈을 불러오겠다?? 패키지야 모듈이야 ㅡㅡ

"""## 3. 패키지에서 import 하기
- 패키지는 모듈의 그룹
- 파일 1, 2, 3을 직박구리 폴더에 넣어놨다고 가정
...???
"""

# pandas 패키지에서 DataFrame이라는 모듈 불러오기
from pandas import DataFrame

pandas.DataFrame()
# pandas에 dataframe 사용하겠다

"""## 4. 별칭 지어주기
- pandas 너무 길면 pd라고 줄여 부를 수도 있다 (이름 맘대로 붙여도 되긴 함)
"""

import pandas as pd

# pandas.DataFrame()
pd.DataFrame()

"""## 5. 자주 사용할 패키지, 모델
- numpy: 과학계산을 위한 패키지
- pandas: 데이터 분석을 할 때 
- matplotlib: 시각화
- seaborn: 시각화 (matplotlib 사용을 도와주는)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# Numpy

## 1. 넘파이란?!

- numerical PythonFuncType
- numerical computiong 컴퓨터가 실수값을 효과적으로 계산할 수 있도록 하는 연구분야
- arithmetic 벡터연산 ?? 벡터가 먼디요..
- 행렬 계산??
- py의 list와 비슷한 개념을 numpy에서는 numpy array라고 부른다. 파이썬 리스트처럼 여러 데이터를 한번에 다룰 수 있지만 모든 데이터가 동일한 data type을 사용해야
- c나 java에서 쓰는 array와 비슷. .... 놓쳐따 ㅠㅠ
- numpy array는 한번 생성하면 크기 변경 안된다 c랑 비슷하넹
- numpy array의 크기를 변경하는 경우 복사가 된다?! 먼말이여

## 2. numpy basic

### 2.1 numpy array Creation
"""

# numpy 라이브러리를 불러옴
import numpy as np

# 파이썬 리스트 선언
data = [1, 2, 3, 4, 5]
data, type(data)

# 파이썬 2차원 리스트 (행렬) 선언 
# 리스트 안에 리스트가 있는 걸 행렬이라고 부른다(!?)
data2 = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
    ]
data2

# 파이썬 리스트를 array로 변환
arr1 = np.array(data)
print (arr1)
arr1
type(arr1)
arr1.shape # (몇, 몇)짜리인지 좌표값 표시

# 2차원 리스트를 np.array로 
arr2 = np.array(data2)
print(arr2)
print (type(arr2))
arr2.shape

print (arr2.ndim) # 차원
print (arr2.shape) # 행, 열의 크기 (좌표값?)
print (arr2.size) # 행x열. 총 개수가 되겠군여
print (arr2.dtype) # 원소의 타입, integer, 64bits
print (arr2.itemsize) # 원소의 사이즈 (bytes). 64bits니까 8byte
print (arr2.nbytes) # array가 차지하는 메모리 공간. 원소의 사이즈 x 원소의 개수

"""- 리스트를 만들지 않고 np array 만드는 법 (????)
- 일단 크기는 지정하고(크기는 못바꾸니까) 원소는 0으로 넣고, 원소는 나중에 넣기
"""

np.zeros(5)

np.ones(3)

np.ones((2, 2))

np.arange(10)

np.arange(10, 100)

"""### 2.3 Array Operation

- 넘파이 어레이를 쓰는 가장 큰 이유는 벡터처럼 사용할 수 있기 때문
"""

# v1 = (1, 2, 3),  v2 = (4, 5, 6)인 벡터 생성하기
v1 = np.array((1, 2, 3))
v2 = np.array((4, 5, 6))
type(v1)

# 리스트로 더하기 연산해보기
t1 = (1, 2, 3)
t2 = (4, 5)
type (t1)
t1 + t2

# vector 더하기
v1 + v2

# vector 빼기
v1 - v2

"""### 2.4 Broadcast
- 서로 크기가 다른 넘파이 어레이를 연산할 때 자동으로 연산을 전파해주는 기능??
"""

arr1 = np.array( [[1, 2, 3], [4, 5, 6]])
arr1.shape

arr2 = np.array([7, 8, 9])
arr2.shape

arr1 + arr2
# [123 + 789]
# [456 + 789]

arr1 * arr2
# [123 * 789]
# [456 * 789]
# [17 28 39]
# [47 58 69]

"""### 2.5 Universal Functions
- numpy array는 하나의 함수를 모든 원소에 자동을로 적용해주는 유니버설 펑션이라는 기능을 제공한다. 이 덕분에 모든 원소에 대해 같은 작업을 처리할 때 빠른 속도를 낼 수 있다
"""

arr1 = np.array([1, 2, 3])
arr1 = arr1 / 1
arr1.dtype

# 모든 원소를 역수를 취하려면?
1 / arr1

# 모든 원소에 2를 더하기
arr1 + 2

"""## 2.6 Indexing"""

arr1 = np.arange(10)
arr1

# 첫번째 원소
arr1[0]

# 마지막 원소
arr1[-1]

arr2 = np.array([[1,2,3,4], [5,6,7,8], [9,10, 11, 12]])
arr2

# arr2의 (2,3)좌표에 있는 원소
arr2[1,2]

# arr2의 세번째 컬럼(3, 7, 11)ㅏ
arr2[:,2] # arr2[a:b] 에서 a 생략하면 모든, 2는 세번째

# arr2의 두번째 row
arr2[1, :]

"""### 2.7 Masking"""

mask = np.array([1,0,0,1,1,0,0])
mask

data =np.random.randn(7,4) # 난수 생성. 정규분포 폭 안에서.. 머라고...? 7*4 사이즈로 뽑아라
# 넘파이 라이브러리 안에 랜덤 모듈 안에 randn이라는 함수
data

masked_data = (mask == 1)
masked_data

data[masked_data, :]

data[mask == 0, :]

# fansy indexing의 또다른 방법 
data[data[:, 0] <0, 0]

data < 0

# 2ckdnjs data에서 첫번째 컬럼에 0보다 작은 원소들을 0으로 치환
data[data<0] = 0
data

mat1 = np.random.randn(5, 3)
mat1

# mat1에 절대값 씌우기
np.abs(mat1)

# mat1의 제곱근 구하기
comp1 = np.array(mat1, dtype=complex)
print (np.sqrt(comp1))

# amt1의 지수값 구하지
np.exp(mat1)

# mat1의 로그값 구하기 자연로그
np.log(mat1)

# 상용로그
np.log10(mat1)

# 결측치 (존재하지 않는 값)이 있는지 없는지 알아보기
np.isnan(mat1)

# 함수 안에 함수 가능

np.isnan(np.log(mat1))

# 무한대수가 있는가 (결측치로 봄)
np.isinf(mat1)

mat2 = np.random.randn(5, 3)
mat2

# 행렬간의 비교연산도 가능
np.maximum(mat1, mat2)

"""### 2.9 Reshaping array"""

# 하나씩 적어서 행렬을 만드는 법
x = np.array( [ [1,2,3],
               [4,5,6], 
               [7,8,9]])
x

# 1부터 9까지 수를, 3*3크기의 행렬로 만들어
x1 = np.arange(1, 10).reshape(3,3) 
x1

# 행렬끼리 비교
x == x1

# 1, 2, 3이 들어가있는 행렬을 3*1로 다시 그리겠다
x2 = np.array([1, 2,3]).reshape(3,1)
x2

"""### 2.10 concatenation of array 아니 이걸 왜 한국어로 안 주시는데요 연쇄가 영어로 뭔지 다 아는거임?!!!??

### 5.1 pandas란?

### 5.2 pandas의 기본 자료구조
"""

import pandas as pd
import numpy as np
print (pd.__version__) # pandas 버전 확인

"""- DataFrame은 2차원 테이블이고 테이블의 한 줄(행 or 열)을 시리즈라고 합니다"""

s = pd.Series([1,3,5, np.nan, 6, 8])
s

# 2021 01 01부터 6일간의 널짜 범위를 생성
dates = pd.date_range('20210101', periods=6)
dates

# 6*4 행렬에 -1에서 1 사이의 랜덤한 숫자를 가지는 원소를 넣고
# index열은 dates, 컬럼은 순서대로 abcd로 하는 DataFrame
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df

"""### 5.3 DataFrame 기초 method"""

#맨 위 다섯줄을 보여주는 head()
df.head()

# 원하는 줄수만큼 볼 수도 있음
df.head(3)

# 끝부분도 볼 수 있음
df.tail(2)

df.index

df.columns

df.values

df.info()

df.describe()
# 간단한 통계값
# 평균
# 표준편차
# 최소값
# 상위25%
# 중위값
# 상위75%
# 최대값

df.sort_values(by='A', ascending=False).head(3)
# A 기준으로 상위 3개값인데, 정렬은 내림차순 (ascending:  ##내림차순)

"""### 5.4 dataFrame indexing"""

df['A']
# 컬럼으로 가져올 수 있다. 파이썬은 컬럼을 인덱스로 생각함
# df['2021-01-01'] 이런거 에러남

# 특정 날짜를 통한 인덱싱
df.loc['2021-01-01']

# 슬라이싱을 이용하면 row 단위로 잘라짐
# 위에서부터 3줄을 잘라옴
df[:3]

# 안좋은 코드래
# df에 이미 dates가 있는데 다시 dates를 볼 필요 없으니까
df.loc[dates[0]]

# 지금은 a, c 두개지만 많아지면..? 
df.loc[:,['A','C']]

# bad
df.loc['2021-01-02',['A','B']]

df.loc['2021-01-01', 'C']

# 안좋은 코드 끝?!

df['A'] >0

df.loc[:,'A'] >0

df[df['A']>0]

df[df['A']>0]['B']

# 데이터프레임 안에 있는 값을 바꾸는 것도 가능
df[df<0] = 0
df