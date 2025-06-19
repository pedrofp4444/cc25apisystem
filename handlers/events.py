from fastapi import Request

async def get_events(request: Request):
    return {
        "eventos": [
            {"nome": "Festival de Verão", "data": "2025-07-20"},
            {"nome": "Feira de Livros", "data": "2025-08-12"}
        ]
    }
