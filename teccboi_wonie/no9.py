## https://youtu.be/umOQNlQMoDc
## 실습: 핸드폰 문자보내기

## 라이브러리: 다른 개발자가 자기 패키지를 공개해놓은것.
## API

## +17637629786
## ACac21061323b47757d9eadc96a5f966e5
## 비밀번호

from twilio.rest import Client

account_sid = 'ACac21061323b47757d9eadc96a5f966e5'
auth_token = '비밀번호'     # 비밀번호 바꿀것

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="테스트테스트",
                     from_='+17637629786',
                     to='+821012341234'     # 번호 바꿀것
                 )

print(message.sid)

## pip3 install 패키지
## pip에 3을 안붙여줘서 헤맸음.
## https://dojang.io/mod/page/view.php?id=2443
## https://docs.microsoft.com/ko-kr/windows/python/web-frameworks