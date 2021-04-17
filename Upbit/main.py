import jwt
import uuid

payload = {
	'access_key': '',
	'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, '시크릿 키')
authorization_token = 'Bearer {}'.format(jwt_token)
