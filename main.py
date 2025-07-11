from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_verify_token(token: str = Depends(oauth2_scheme)):
    if token != "crset-super-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )
    return {"user": "joao"}

@app.get("/leads")
def get_leads(user: dict = Depends(fake_verify_token)):
    return [{"name": "Leonor"}, {"name": "Sónia"}, {"name": "Mike"}]

@app.get("/")
def root():
    return {"message": "API ativa"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
