from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError
# Exception -> Todos os erros serão tratados como objetos vindo dessa classe Exception

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # enviar para um log
        # enviar um email de notificacao
        return HttpResponse(
            status_code=error.statuscode,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
            }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )