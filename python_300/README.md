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

