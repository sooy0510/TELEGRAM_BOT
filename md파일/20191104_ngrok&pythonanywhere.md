# 1. ngrok

### 1.1 ngrok 설치

- `C:\USERS\student` 경로에 넣어주기

  > ![1572859048110](images/1572859048110.png)

<br>

<br>

### 1.2 ngrok 실행

```bash
# cmd

C:\Users\student> ngrok http 5000
```

<br>

- 서버가 실행된다

> ![1572859236979](images/1572859236979.png)

<br>

<br>

### 1.3 WebHook 설정

- telegram bot이 ngrok 서버를 거치도록 설정

> https://api.telegram.org/bot[chat_id]:[token]/setWebhook?url=db3ead36.ngrok.io/[chat_id]:[token]

> ![1572859579182](images/1572859579182.png)

<br>

- webhook 설정 완료

> ![1572859812187](images/1572859812187.png)



<br>

<br>

### 1.4 ngrok 서버 배포

#### Python anywhere 

- 회원가입

- web

  - create > Flask > python -7 클릭

    > ![1572860103393](images/1572860103393.png)

- Decouple 설치

  ```bash
  $ pip install python-decouple --user
  ```

  > ![1572860474364](images/1572860474364.png)

<br>

- `flask_app`& `.env` 옮기기

  - 기존 `flask_app.py`와 `.env`를 복붙해준다

  > ![1572860669530](images/1572860669530.png)

  

<br>

<br>

<br>

# Python Anywhere 서버로 변경

> 기존 ngrok 서버 url을 없애고 새로운 server url로 연결

<br>

### 1.1 ngrok으로 되어있는 기존 WebHook삭제

- ngrok 서버 url 삭제

  > https://api.telegram.org/bot[chat_id]:[token]/deleteWebhook 

  > ![1572860840986](images/1572860840986.png)

<br>

- 기존 WebHook이 삭제되었다

  > ![1572860907224](images/1572860907224.png)

<br>

<br>

### 1.2 Webhook 재설정

- python anywhere로 Webhook을 재설정해준다

  > ![1572861084048](images/1572861084048.png)

  <br>

  ```
  https://api.telegram.org/bot[chat_id]:[token]/setWebhook?url=sooy.pythonanywhere.com/[chat_id]:[token]
  ```

  <br>

- Webhook이 재설정되었다

  > ![1572861180265](images/1572861180265.png)

<br>

- 잘 도는지 확인

  > ![1572861237129](images/1572861237129.png)

  

