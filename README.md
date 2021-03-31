# MiddleSchool-3-2-Scatter-plot

## 프로젝트 동기
2021년 3월 31일 수학 3-2 문제를 푸는 강민서는 이 지긋지긋한 계산에 빡이 쳤다. 그래서 그냥 이걸 계산하는 라이브러리를 만들고자 이 프로젝트를 시작하게 되었다.

## 모듈 임포트하기 
``` python
>>> from Statistical_math.Calculate import Calculate

>>> cal = Calculate()
```


# 평균 구하기
``` python
>>> print(cal.mean([1,2,3,4,5,6]))
3.5
```
# 중앙값 구하기
``` python
>>> print(cal.median([4, 3, 2, 3, 4, 5, 6]))
3
```
# 편차 구하기
```python 
>>> print(cal.deviation([1,2,3,4,5,6]))
[-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
```

# 분산 구하기
```python 

>>> print(cal.dispersion([1,2,3,4,5,6]))
2.9166666666666665
```