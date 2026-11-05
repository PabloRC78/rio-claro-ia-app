import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="chatapi", auth_level=func.AuthLevel.ANONYMOUS)
def chatapi(req: func.HttpRequest) -> func.HttpResponse:

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    if req.method == "OPTIONS":
        return func.HttpResponse(
            status_code=200,
            headers=headers
        )

    try:
        req_body = req.get_json()

        pregunta = req_body.get("pregunta", "")

        return func.HttpResponse(
            json.dumps({
                "respuesta": f"Recibí tu pregunta: {pregunta}"
            }),
            mimetype="application/json",
            status_code=200,
            headers=headers
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({
                "error": str(e)
            }),
            mimetype="application/json",
            status_code=500,
            headers=headers
        )


    