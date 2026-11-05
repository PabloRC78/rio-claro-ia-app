import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="chatapi", auth_level=func.AuthLevel.ANONYMOUS)
def chatapi(req: func.HttpRequest) -> func.HttpResponse:

    try:
        req_body = req.get_json()
        pregunta = req_body.get("pregunta", "")

        return func.HttpResponse(
            json.dumps({
                "respuesta": f"Recibí tu pregunta: {pregunta}"
            }),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({
                "error": str(e)
            }),
            mimetype="application/json",
            status_code=500
        )
    