import requests

api_url = 'https://api.telegram.org'
token = '888992733:AAGTL_2G1FOfa5mYFb1cfXsHqKIp4e48H74'
chat_id = '975161663'
text = input('메세지를 입력해주세요 : ')

# 요청을 보내보아요
requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
