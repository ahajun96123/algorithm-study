# algorithm-study
studying algorithm

알고리즘 공부와 정리를 위한 repo

백준허브 크롬 확장 프로그램 사용(22.03.03)

#
<h3><i>입출력 팁</i></h3>
C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline()을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.<br>
<b><i>빠른 입출력이 필요 없어도 계속 써서 손에 익히자!</i></b><br>
<sub>출처 : 백준 15552</sub>
<br><br>python에서 eof 문제는 while, try, except를 사용해서 풀기

<br><br><br>
어려웠던 것<br>
2981. 공통 나머지인 수 구하기. 수학적 사고를 요구함.
2004. 조합수에서 뒤 0이 개수 구하기. 10의 인수인 2와 5의 개수를 구해야됨. 다른 방법은 시간초과 뜸.
