[초보자를 위한 파이썬 300제](https://wikidocs.net/book/922)를 공부한 내용.

## 파이썬 시작하기

* print()
    * print("a", "b") : 출력 결과 'a b'.
    * print("a", "b", sep = "/") : sep 옵션. 출력 결과 'a/b'.
    * print("a", end = "") : end 옵션. 마지막의 개행을 변경.

## 변수

* 형변환
    * int()
    * str()
    * float()

## 문자열

* 오프셋 인덱스
    * var[\<index>]
    * var[\<start>:\<end>]
    * var[\<start>:\<end>:\<stride>] : stride는 보폭.

    ```
    str = "0123456789"
    print (str[:4]) # 0123
    print (str[-4:]) # 6789
    print (str[::2]) # 02468
    print (str[::-1]) # 9876543210
    ```

* 문자열 메서드
    * .replace(\<old\>, \<new\>) : <u>문자열은 수정 불가능하므로, 새로운 문자열을 반환.</u>
    * .split(\<sep\>) : 배열을 반환. 인덱스로 접근 가능.
    * .strip() : 문자열의 앞뒤 공백 제거.
    * .rstrip() : 오른쪽의 공백만 제거.
    * .upper()
    * .lower()
    * .capitalize()
    * .startswith() : 여러개일 경우, .startswith(("xls", "xlsx"))
    * .endswith()

* 문자열은 더하기와 곱하기가 가능.

* print () 포맷팅
    * print ("이름: %s" % name) : % 포맷
    * print ("이름 : {}".format(name)) : .format()
    * print (f"이름: {name}") : f-스트링

## 리스트

* 리스트란? 순서가 있고 <u>수정 가능</u>한 자료구조.

* 리스트 생성: list = ["a", "b", "c"]

* 요소 추가
    * list.append("d")
    * list.insert(4, "e")

* 요소 삭제
    * del list[4]
    * del list[-2:]

* 리스트도 더하기 가능.

* 리스트도 인덱싱 가능.

* 정수형 리스트
    * max(list), min(list)
    * sum(list)

* 요소 개수: len(list)

* 리스트를 문자열로: "\<sep\>".join(list)

* 문자열을 리스트로: string.split("\<sep\>")

* 리스트 정렬: list.sort()

## 튜플

* 튜플이란? 순서가 있고 수정이 불가능한 자료구조.

* 튜플 생성
    * var = ()
    * var = ("a", "b", "c")
    * var = 1, 2, 3

* 튜플과 리스트
    * list()
    * tuple()
    * 서로 형변환이 가능.

* 튜플 언패킹
    ```
    var = ("apple", "banaba", "cake")
    # a, b = var # 언패킹 오류
    a, b, c = var # a에는 apple이 들어감.
    ```

* range()
    * list(range(99)[2::2])
    * tuple(range(2, 98, 2))

## 딕셔너리

* 언패킹
    * https://python.bakyeono.net/chapter-5-5.html
    * https://studydevseung.tistory.com/27
    * 여러 값은 *로 묶음.
    * 불필요한 값은 '_(언더바)'로 처리 추천.
    * ex) _, *valid_score, _ = scores

* 요소 접근(인덱싱): dict[\<key>]

* 요소 추가: dict[\<new key>] = \<new value>

* 요소 삭제: del dict[\<key>]

* key들을 리스트로: list(dict.keys())

* valu들의 합: sum(dict.values())

* 딕셔너리 병합(업데이트): dict.update(\<new dict>)

* 키와 밸류(두 리스트나 튜플)을 딕셔너리로: dict(zip(keys, vals))

## 분기문(조건문)

* if True: 무조건 실행

* 입력받기: input(), input("표시할 내용")

* 요소가 리스트에 있는지: if x in list

## 반복문

* range()
    * range(\<stop>)
    * range(\<start>, \<stop>)
    * range(\<start>, \<stop>, \<범위>)

* 리스트에서의 반복문
    * 인덱스로의 접근
    ```
    apart = [ [101, 102], [201, 202], [301, 302] ]
    for i in range(len(apart)):
        for j in range(len(apart[i])):
            print(apart[i][j], "호")
    ```
    * 리스트로의 접근
    ```
    apart = [ [101, 102], [201, 202], [301, 302] ]
    for i in apart:
        for j in i:
            print(j, "호")
    ```