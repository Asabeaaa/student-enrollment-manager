from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
import os
from dotenv import load_dotenv

# load env
BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
load_dotenv(os.path.join(BASE_DIR, '.env'))


# authentication for affinity lexis api
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token")  # use token authentication


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key != os.getenv("REQUEST_API_KEY"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is incorrect"
        )
