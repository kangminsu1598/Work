## # 1 자료형

## 1-1 숫자형

### 1) 숫자형이란?

* 숫자 형태로 이루어진 자료형

| 항목   | 사용 예                 |
| ------ | ----------------------- |
| 정수   | 123, -345, 0            |
| 실수   | 123.45, -1234.5, 3.4e10 |
| 8진수  | 0o34, 0o25              |
| 16진수 | 0x2A, 0xFF              |

이제 이런 숫자들을 파이썬에서는 어떻게 만들고 사용하는지 자세히 알아보자.

### 2) 숫자형은 어떻게 만들고 사용할까?

#### 정수형

* 양의 정수와 음의 정수, 숫자 0

```
>>> a = 123
>>> a = -178
>>> a = 0
```

#### 실수형

* 파이썬에서 실수형(Floating-point)은 소수점이 포함된 숫자를 말한다.
* "컴퓨터식 지수 표현 방식"

```
>>> a = 4.24E10
>>> a = 4.24e-10
```

#### 8진수와 16진수

8진수(Octal) 표현법 : 0o 또는 0O로 시작

```
>>> a = 0o177
```

16진수(Hexadecimal) 표현법: 0x로 시작하면 된다.

```
>>> a = 0x8ff
>>> b = 0xABC
```

### 3) 숫자형을 활용하기 위한 연산자

#### 사칙연산

```
>>> a = 3
>>> b = 4
>>> a + b
7
>>> a * b
12
>>> a / b
0.75
```

#### x의 y제곱을 나타내는 `**` 연산자

* `x ** y`처럼 사용되었을 때 x의 y제곱값을 리턴한다.

```python
>>> a = 3
>>> b = 4
>>> a ** b
81
```

#### 나눗셈 후 나머지를 반환하는 `%` 연산자

* `%`는 나눗셈의 나머지 값을 반환하는 연산자이다.

```
>>> 7 % 3
1
>>> 3 % 7
3
```

#### 나눗셈 후 몫을 반환하는 `//` 연산자

```
>>> 7 / 4
1.75
```

```
>>> 7 // 4
1
```



## 1-2 문자열 자료형

### 1) 문자열이란?

* 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합

```python
"Life is too short, You need Python"
"a"
"123"
```

* 따옴표로 둘러싸여 있으면 모두 문자열이라고 보면 된다.


### 2) 문자열은 어떻게 만들고 사용할까?

#### 문자열을 만드는 방법

* 큰따옴표로 양쪽 둘러싸기

```
"Hello World"
```

* 작은따옴표로 양쪽 둘러싸기

```
'Python is fun'
```

* 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기

```
"""Life is too short, You need python"""
```

* 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기

```
'''Life is too short, You need python'''
```

#### 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

**1) 문자열에 작은따옴표 (') 포함시키기**

* 문자열을 큰따옴표(")로 둘러싼다.

```
>>> food = "Python's favorite food is perl"
```

```
>>> food
"Python's favorite food is perl"
```

**2) 문자열에 큰따옴표 (") 포함시키기**

* 작은따옴표(')로 둘러싼다.

```
>>> say = '"Python is very easy." he says.'
```

**3) \(백슬래시)를 이용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기**

* `\`(백슬래시) 뒤의 작은따옴표(')나 큰따옴표(")는 문자 ('), (") 그 자체를 뜻한다.
* '', "" 신경쓰지 말고 `\`를 활용하자!

```
>>> food = 'Python\'s favorite food is perl'
>>> say = "\"Python is very easy.\" he says."
```

#### 여러 줄인 문자열을 변수에 대입하고 싶을 때

**1) 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기**

```
>>> multiline = "Life is too short\nYou need python"
```

**2) 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용**

* 추천! 가독성이 좋다!

```
>>> multiline='''
... Life is too short
... You need python
... '''
```

**[이스케이프 코드란?]**

* 주로 출력물을 보기 좋게 정렬하는 용도로 이용된다. 
* 활용빈도가 높은 것은 `\n`, `\t`, `\\`, `\'`, `\"`이다.

| 코드   | 설명               |
| ------ | ------------------ |
| `\n`   | 개행 (줄바꿈)      |
| `\t`   | 수평 탭            |
| `\\`   | 문자 "`\`"         |
| `\'`   | 단일 인용부호(`'`) |
| `\"`   | 이중 인용부호(`"`) |
| `\r`   | 캐리지 리턴        |
| `\f`   | 폼 피드            |
| `\a`   | 벨 소리            |
| `\b`   | 백 스페이스        |
| `\000` | 널문자             |



### 3) 문자열 연산하기

* 파이썬에서는 **문자열을 더하거나 곱할 수 있다.**  (**파이썬의 장점**)

#### 문자열 더해서 연결하기(Concatenation)

```
>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'
```

위 소스 코드에서 세 번째 줄을 보자. 복잡하게 생각하지 말고 눈에 보이는 대로 생각해 보자. "Python"이라는 head 변수와 " is fun!"이라는 tail 변수를 더한 것이다. 결과는 'Python is fun!'이다. 즉, head와 tail 변수가 +에 의해 합쳐진 것이다.

직접 실행해 보고 결과값이 제시한 것과 똑같이 나오는지 확인해 보자.

#### 문자열 곱하기

* `*`  : 문자열을 반복해라

```
>>> a = "python"
>>> a * 2
'pythonpython'
```

#### 문자열 곱하기 응용

```
# multistring.py

print("=" * 50)
print("My Program")
print("=" * 50)
```

```
C:\Users>cd C:\doit
C:\doit>python multistring.py
==================================================
My Program
==================================================
```

#### 문자열 길이 구하기

문자열의 길이는 다음과 같이 len 함수를 이용하면 구할 수 있다. len 함수는 print함수처럼 파이썬의 기본 내장함수이다.

```
>>> a = "Life is too short"
>>> len(a)
17
```



### 4) 문자열 인덱싱(indexing)과 슬라이싱(slicing)

#### 문자열 인덱싱이란?

```
>>> a = "Life is too short, You need Python"
```

```
>>> a = "Life is too short, You need Python"
>>> b = a[0] + a[1] + a[2] + a[3]
>>> b
'Life'
```

#### 문자열 슬라이싱이란?

```
>>> a = "Life is too short, You need Python"
>>> b = a[0] + a[1] + a[2] + a[3]
>>> b
'Life'
```

위의 방법처럼 단순하게 접근할 수도 있지만 파이썬에서는 더 좋은 방법을 제공한다. 바로 슬라이싱(Slicing) 이라는 기법이다.[1](https://wikidocs.net/13#fn:slicing)

위의 예는 슬라이싱 기법으로 다음과 같이 간단하게 처리할 수 있다.

```
>>> a = "Life is too short, You need Python"
>>> a[0:4]
'Life'
```



### 문자열을 슬라이싱하는 방법

```
>>> a[0:5]
'Life '
```

* 공백 문자 역시 L, i, f, e 같은 문자와 동일하게 취급된다.
* 'Life'와 'Life '는 완전히 다른 문자열이다.

```
>>> a[19:]
'You need Python'
```

```
>>> a[:17]
'Life is too short'
```

```
>>> a[:]
'Life is too short, You need Python'
```

* 마이너스(-) 기호를 사용할 수 있다.

```
>>> a[19:-7]
'You need'
```

*  a[19]에서부터 a[-8]까지를 슬라이싱 한다.

### 슬라이싱으로 문자열 나누기



```
>>> a = "20010331Rainy"
>>> year = a[:4]
>>> day = a[4:8]
>>> weather = a[8:]
>>> year
'2001'
>>> day
'0331'
>>> weather
'Rainy'
```

위의 예는 4와 8이란 숫자로 "20010331Rainy"라는 문자열을 세 부분으로 나누는 방법을 보여 준다.

지금까지 인덱싱과 슬라이싱에 대해서 살펴보았다. 인덱싱과 슬라이싱은 프로그래밍을 할때 매우 자주 사용되는 기법이니 꼭 반복해서 연습해 두자.





**["Pithon"이라는 문자열을 "Python"으로 바꾸려면?]**

* 문자열의 요소값은 바꿀 수 없다(immutable)

```
>>> a = "Pithon"
>>> a[1]
'i'
>>> a[1] = 'y'
```

```
>>> a = "Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1] + 'y' + a[2:]
'Python'
```

위의 예에서 볼 수 있듯이 슬라이싱을 이용하면 'Pithon'이라는 문자열을 'P' 부분과 'thon' 부분으로 나눌 수 있기 때문에 그 사이에 'y'라는 문자를 추가하여 'Python'이라는 새로운 문자열을 만들 수 있다.





### 5) 문자열 포매팅(formating)

* 문자열 포매팅이란 쉽게 말해 문자열 내에 어떤 값을 삽입하는 방법

#### format 함수를 이용한 포매팅

* 표현법 : `{}.format()`

**숫자 값을 가진 변수로 대입하기**

```
>>> number = 3
>>> "I eat {0} apples".format(number)
'I eat 3 apples'
```

**2개 이상의 값 넣기**

```
>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'
```

* .format(변수1, 변수2)

#### f 문자열 포매팅

* python 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다

* 문자열 시작 전에 f + '{변수1}{변수2}...'
* 표현식을 지원한다 {변수+연산가능}

```
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
```

```
>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
```

* 딕셔너리의 Value 값 표현: {변수명['key']}

```
>>> d = {'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
```

* 문자열 정렬 : 를 사용한다.

```
>>> f'{"hi":<10}'  # 왼쪽 정렬
'hi        '
>>> f'{"hi":>10}'  # 오른쪽 정렬
'        hi'
>>> f'{"hi":^10}'  # 가운데 정렬
'    hi    '
```

* 문자+정렬(^<>)을 사용해서 공백을 문자로 채울 수 있다.

```
>>> f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
'====hi===='
>>> f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
'hi!!!!!!!!'
```

* 소수점 단위도 조정 가능하다.

```
>>> y = 3.42134234
>>> f'{y:0.4f}'  # 소수점 4자리까지만 표현
'3.4213'
>>> f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
'    3.4213'
```

* f 문자열에서 '{}' 문자를 표시하려면 {{}}로 사용한다.

```
>>> f'{{ and }}'
'{ and }'
```



### 6) 문자열 메소드

#### 문자 개수 세기(count)

```
>>> a = "hobby"
>>> a.count('b')
2
```

* **문자열** 중 문자 b의 개수를 반환한다.

#### 위치 알려주기1(find)

```
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
```

* 'b'가 처음으로 나온 위치를 반환한다. 
* 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.

#### 위치 알려주기2 (index)

```
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found
```

* 맨 처음으로 나온 위치를 반환한다.
* 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다.

#### 문자열 삽입(join)

```
>>> ",".join('abcd')
'a,b,c,d'
```

abcd라는 문자열의 각각의 문자 사이에 ','를 삽입한다.

join 함수는 문자열 뿐만 아니라 앞으로 배우게 될 리스트나 튜플을 입력으로 사용할 수 있다. (리스트와 튜플은 곧 배우게 될 내용이니 여기서는 잠시 눈으로만 살펴보기로 하자.)

join 함수의 입력으로 리스트를 사용하는 예는 다음과 같다.

```
>>> ",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'
```

#### 소문자를 대문자로 바꾸기(upper)

```
>>> a = "hi"
>>> a.upper()
'HI'
```

upper() 함수는 소문자를 대문자로 바꾸어 준다. 만약 문자열이 이미 대문자라면 아무런 변화도 일어나지 않을 것이다.

#### 대문자를 소문자로 바꾸기(lower)

```
>>> a = "HI"
>>> a.lower()
'hi'
```

lower() 함수는 대문자를 소문자로 바꾸어 준다.

왼쪽 공백 지우기(lstrip)

```
>>> a = " hi "
>>> a.lstrip()
'hi '
```

문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. lstrip에서 l은 left를 의미한다.

#### 오른쪽 공백 지우기(rstrip)

```
>>> a= " hi "
>>> a.rstrip()
' hi'
```

문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. rstrip에서 r은 right를 의미한다.

#### 양쪽 공백 지우기(strip)

```
>>> a = " hi "
>>> a.strip()
'hi'
```

문자열 양쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.

#### 문자열 바꾸기(replace)

```
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'
```

replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 내의 특정한 값을 다른 값으로 치환해 준다.

#### 문자열 나누기(split)

```
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> a = "a:b:c:d"
>>> a.split(':')
['a', 'b', 'c', 'd']
```

`a.split()`처럼 괄호 안에 아무런 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터등)을 기준으로 문자열을 나누어 준다. 만약 `a.split(':')`처럼 괄호 안에 특정한 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다. `['Life', 'is', 'too', 'short']`나 `['a', 'b', 'c', 'd']`는 리스트라는 것인데 다음 절에서 자세히 알아볼 것이니 여기서는 너무 신경 쓰지 말도록 하자.

위에서 소개한 문자열 관련 함수들은 문자열 처리에서 사용 빈도가 매우 높은 것들이고 유용한 것들이다. 이 외에도 몇 가지가 더 있지만 자주 사용되는 것들은 아니다.

## 연습문제

*(연습문제 풀이 : https://wikidocs.net/17090#02-2)*


**[문제1] 문자열 나누기**

홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.


**[문제2] 문자열 인덱싱**

주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

```
>>> pin = "881120-1068234"
```


**[문제3] 문자열 바꾸기1**

다음과 같은 문자열이 있다.

```
a:b:c:d
```

문자열의 replace 함수를 이용하여 위 문자열을 다음과 같이 고치시오.

```
a#b#c#d
```


**[문제4] 문자열 바꾸기2**

다음과 같은 문자열이 있다.

```
a:b:c:d
```

문자열의 split와 join 함수를 이용하여 위 문자열을 다음과 같이 고치시오.

```
a#b#c#d
```

(힌트. 문자열을 ":"으로 split하면 리스트 자료형이 리턴된다. 리스트 자료형은 문자열과 마찬가지로 join이 가능하다.)

------

1. 인덱싱 기법과 슬라이싱 기법은 뒤에서 배울 자료형인 리스트나 튜플에서도 사용할 수 있다. [↩](https://wikidocs.net/13#fnref:slicing)