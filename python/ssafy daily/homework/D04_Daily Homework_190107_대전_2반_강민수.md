### Daily Homework_190107_대전 2반 강민수

### 1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 3개만 작성하세요.

* ```python
  False, True, None
  ```



### 2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. 따라서 아래의 값을 비교하기 위해 작성해야 하는 코드를 작성하세요

```python
a = 0.1 * 3
b = 0.3

print(a)  # 0.30000000000000004
print(b)  # 0.3

# 방법 1
abs(a - b) # True

# 방법 2
import math
math.isclose(a, b) # True
```



### 3. "안녕, 철수야"를 String interpolation을 사용하여 출력하세요.

```python
name = "철수"
print(f'"안녕, {name}야"')
```



### 4. 다음 중 형변환시 오류가 발생하는 것은?

* 5) int('3.5')



### 5. 변경할 수 있는 것과 변경 불가능한 것을 분류하시오.

* 변경할 수 있는 것 : list, set, dictionary
* 변경 불가능한 것 : string, tuple, range

