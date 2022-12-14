import secrets
import api
from typing import Optional

class VerySecureServer:
    def __init__(self, secret: Optional[str] = None):
        if secret is None:
            self._secret = secrets.token_hex(256)
        else:
            self._secret = secret

    def verify_token(self, request: api.VerifyTokenRequest) -> api.VerifyTokenResponse:
        try:
            s = request.token
            for i in range(len(self._secret)):
                if len(s) <= i:
                    return api.VerifyTokenResponse(False)
                elif s[i] != self._secret[i]:
                    return api.VerifyTokenResponse(False)
            return api.VerifyTokenResponse(True)
        except:
            return api.VerifyTokenResponse(False)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

