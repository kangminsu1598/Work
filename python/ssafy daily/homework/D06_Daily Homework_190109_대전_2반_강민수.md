### Daily Homework_190109_대전 2반 강민수

### 1. 배웠던 내장 함수 중 5개만 나열

* abs(), max(), dict(), map(), zip()

### 2. 다음 중 틀린 것은

(1). 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다. **(X)**

> 튜플 형태 (a, b)로 출력된다.

### 3. 함수의 인자 기본값 설정을 활용하여 곱셈의 결과를 반환하는 my_mul 함수 만들기

```python
def my_mul(a,b=0):
    if b:
        return a*b
    else:
        return a
```

