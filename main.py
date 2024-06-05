import time
from jwt_handler import encodeJWT, decodeJWT, refreshJWT

user = {"email":"tlbkvs@gmail.com",
"username":"katana", "id":1}

#получаем токины
jwt_token = encodeJWT(user) # {'access_token':vhbgkj,'refresh_token':hhifjk}

#проходит время
time.sleep(6)

#прилетает декодированный токен, еслт время не истекло, если время жизни токена истекло
приоетает пустой dict
decode = decodeJWT(jwt_token['access_token'])

#обновление старые токены, на новые
new_jwt_token = refreshJWT(jwt_token['access_token'])

new_jwt_token = refreshJWT(jwt_token['refresh_token'])

