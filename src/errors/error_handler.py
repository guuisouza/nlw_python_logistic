from src.views.http_types.http_response import HttpResponse
# Exception -> Todos os erros serão tratados como objetos vindo dessa classe Exception

def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
