from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Bom Dia!!!

Projeto CI/CD PB JUN - 2025

Felipe Moneda Gilioli
"}
