## Override 
  
<br>
<br>


- 클래스 A를 선언하고, 함수 get 에서 문자 'A'를 프린트 한다.

```python
class A:
  def get(self):
    print('A')
```

<br>
<br>
<br>
<br>

- 클래스 B를 선언하고 클래스 A를 상속 받는다.

```python
class B(A):
  def get(self):
    print('B')
    super().get()
```


<br>
<br>
<br>
<br>

- 클래스 C를 선언하고 클래스 A를 상속 받는다.
```python
class C(A):
  def get(self):
    print('C')
    super().get()
```


<br>
<br>
<br>
<br>

- 클래스 D를 선언하고 클래스 B와 C를 순차적으로 상속 받는다.
```python
class D(B, C):
  def get(self):
    print('D')
    super().get()
```


<br>
<br>
<br>
<br>

- 클래스 D를 d에 할당하고, 클래스 D의 함수 get을 실행한다.
```python
d = D()
d.get()
```


<br>
<br>
<br>
<br>

결과
```python
# Class D 에서 먼저 print('D')
D

# Class D 에서 super().get() 으로 상속받은 Class B의 함수 get 실행 print('B')
B

# Class B 에서 super()는 Class C 가 된다. 그 이유는 D를 호출할 때 method를 탐색하는 순서가
# D -> B -> C -> A 가 되기 때문이다. # D.mro()
# B의 super().get() 은 탐색에 의해 Class C에 있는 함수 get을 호출하고, 'C' 를 출력한다.
C

# Class C의 super().get() 은 상속받은 Class A의 함수 get을 호출하고, 'A'를 출력한다. 
A
```



