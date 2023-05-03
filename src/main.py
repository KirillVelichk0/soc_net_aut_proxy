from fastapi.responses import JSONResponse, FileResponse, Response
from application import app
from GroupsMaster import RegistrateOrLoginModel, VerifyModel
from GRPCClient import grpc_client
client = grpc_client
main_app = app

@app.get("/")
async def root():
    return FileResponse('public/test.html')

@app.post("/registration", response_class=JSONResponse)
async def TryRegistrate(request: RegistrateOrLoginModel):
    try:
        print("Im here")
        result = await client.TryRegistr(request.email, request.password)
        return JSONResponse({"result": result[0], "isOk": result[1]})
    except Exception as ex:
        return JSONResponse({"error": str(ex)}, status_code=401)
    

@app.post('/registration_verification', response_class=JSONResponse)
async def TryVerifyReg(request: VerifyModel):
    try:
        result = await client.TryVerifyRegistr(request.random_data_token)
        return JSONResponse({"response_message": result})
    except Exception as ex:
        return JSONResponse({"error": str(ex)}, status_code=401)
    

@app.post("/login", response_class=JSONResponse)
async def TryLogin(request: RegistrateOrLoginModel):
    try:
        print("Im here")
        result = await client.LoginWithPassword(request.email, request.password)
        return JSONResponse({"jwtToken": result[0], "user_id": result[1]})
    except Exception as ex:
        return JSONResponse({"error": str(ex)}, status_code=401)

        
