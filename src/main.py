from fastapi import FastAPI

from src.metadata import metadata


def create_app() -> FastAPI:
    """Create FastAPI application with configuration."""
    app = FastAPI(
        title=metadata.TITLE,
        description=metadata.DESCRIPTION,
        version=metadata.VERSION,
        openapi_tags=metadata.TAGS_METADATA,
    )

    # TODO: Add routers here
    # app.include_router(dishes_router, prefix="/api/v1")
    # app.include_router(orders_router, prefix="/api/v1")

    return app


app = create_app()


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Tastehub API is running!"}
    