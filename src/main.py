from fastapi import FastAPI

import src.metadata as metadata


def create_app() -> FastAPI:
    app = FastAPI(
        title=metadata.TITLE,
        description=metadata.DESCRIPTION,
        version=metadata.VERSION,
        openapi_tags=metadata.TAGS_METADATA,
    )

    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Tastehub API is running!"}
