## 01) 125
* [ ] 언바운드 메서드, 바운드 메서드?
    ```
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol.groupAnagrams(strs)

    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    Solution.groupAnagrams(sol, strs)
    ```
* `re.sub()`
    * 정규 표현식

## 02) 344
* 파이썬에서 타입 표시하기
    * typing 모듈로 타입 표시하기: https://www.daleseo.com/python-typing/
    * `from typing import List`
* 모듈 사용하기: https://dojang.io/mod/page/view.php?id=2441

## 03) 937
* 수 판별 함수: `isdigit()`, `isdecimal()`, `isnumeric()`
* 리스트 정렬
    * `list.sort(key=함수)`: 함수에 람다식(익명 함수)도 들어갈 수 있음.
* 람다 표현식

## 04) 819
* counter 객체
    * `import collections`
    * `카운터객체 = collections.Counter(리스트)`: 생성
    * `카운터객체.most_common(n)`: 가장 빈도 높은 항목 n개 추출
* [ ] words 정의한 세 줄 이해 못함.
* [ ] 정규표현식에서 r은 뭐지?

## 05) 49
* `sorted()` vs `.sort()`: sorted 함수는 정렬된 새로운 리스트를 반환함. sort 메서드는 기존 리스트를 정렬하며 반환값이 없음.
* defaultdict 객체: `dict = collections.defaultdict(<디폴트값>)`

## 13) 234
* 다중할당
    * 다중 할당은 작업들이 동시에 일어난다.
    * 따라서 스왑 `a, b = b, a`와 같은 것이 가능한 것.

## 21) 316
* set(): 문자열을 매개변수로 집합을 만들 수 있다.
    ```
    test = set("bcda")
    print (test) # {'a', 'b', 'c', 'd'}
    ```

## 20.09.06

### 10장. 데크, 우선순위 큐
* 우선순위 큐
    * heapq 모듈: 키를 기준으로 정렬. 최소 힙으로, 작은 값부터 추출. (따라서 큰 값부터 추출하려면 음수로 변환해볼 것.)

### 11장. 해시 테이블
* 리스트 컴프리헨션
* 슬라이딩 윈도우, 투 포인터
* `collections.Counter(nums).most_common(k)`
* `list(zip(*collections.Counter(nums).most_common(k)))[0]`
    * zip()
        ```
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4]
        c = [1, 2, 3]
        zip(a, b) # 제너레이터를 리턴
        list(zip(a, b)) # [(1, 1), (2, 2), (3, 3), (4, 4)]
        list(zip(a, b, c)) # [(1, 1), (2, 2), (3, 3)]
        ```
    * `*`: (튜플 혹은 리스트 등의 시퀀스) 패킹, 언패킹
        * `**`: (딕셔너리 등의 페어) 패킹, 언패킹

### 12장. 그래프
* DFS, BFS, 백트래킹
* 중첩 함수
* 객체 복사
    ```
    a = [1,2,3]
    b = a; id(b) # a와 id 동일. 즉 참조이므로 b의 값을 변경 시, a의 값도 변경됨.
    c = a[:]; id(c) # a와 id 다름
    d = a.copy(); id(d) # a와 id 다름
    ```