from fastapi.routing import APIRouter

from service_client.web.api import docs, echo, event, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(event.router, prefix="/event", tags=["event"])
