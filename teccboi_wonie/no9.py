## https://youtu.be/umOQNlQMoDc
## 실습: 핸드폰 문자보내기

## 라이브러리: 다른 개발자가 자기 패키지를 공개해놓은것.
## API

## +17637629786
## ACac21061323b47757d9eadc96a5f966e5
## 6ece33fe6afd6f5251c550919dcfa690

from twilio.rest import Client

account_sid = 'ACac21061323b47757d9eadc96a5f966e5'
auth_token = '6ece33fe6afd6f5251c550919dcfa690'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17637629786',
                     to='+821065651094'
                 )

print(message.sid)