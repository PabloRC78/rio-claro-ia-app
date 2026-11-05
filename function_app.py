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
            "",
            status_code=200,
            headers=headers
        )

    try:

        req_body = req.get_json()
        pregunta = req_body.get("pregunta", "").lower()

        if "rc001" in pregunta:

            respuesta = """
Factura RC001
Proveedor: Quimicos del Bajio SA de CV
RFC: QBA180920AA1
Fecha: 15/09/2026
Subtotal: 10775
IVA: 1724
Total: 12499
"""

        elif "rc002" in pregunta:

            respuesta = """
Factura RC002
Proveedor: Limpieza Integral del Centro SA
RFC: LIC120124AB9
Fecha: 22/09/2026
Subtotal: 8650
IVA: 1384
Total: 10034
"""

        elif "rc003" in pregunta:

            respuesta = """
Factura RC003
Proveedor: Distribuciones Quimicas Nacionales
RFC: DQN090311GH2
Fecha: 05/10/2026
Subtotal: 14200
IVA: 2272
Total: 16472
"""

        elif "devolucion" in pregunta:

            respuesta = """
Política de devoluciones:
Las devoluciones pueden solicitarse hasta 30 días después de la entrega.
"""

        elif "facturacion" in pregunta:

            respuesta = """
Política de facturación:
La factura debe solicitarse el mismo mes de la compra.
"""

        elif "credito" in pregunta:

            respuesta = """
Política de crédito:
Clientes con más de 12 meses pueden solicitar crédito.
"""

        elif "envio" in pregunta:

            respuesta = """
Envíos:
Pedidos mayores a $5000 tienen envío gratuito.
"""

        elif "horario" in pregunta:

            respuesta = """
Horarios:
Lunes a Viernes de 8:00 a 18:00 horas.
Sábado de 9:00 a 14:00 horas.
"""

        elif "cliente" in pregunta:

            respuesta = """
Clientes registrados:

Hotel Sol Real
Escuela Moderna
Restaurante El Patio
Hotel Plaza Dorada
Mini Super Garcia
Hospital San Miguel
"""

        elif "catalogo" in pregunta or "producto" in pregunta:

            respuesta = """
Catálogo de productos:

Cloro Líquido Estándar
Blanqueador Concentrado
Desinfectante Multiusos
Jabón Líquido para Trastes
"""

        elif "queja" in pregunta:

            respuesta = """
Quejas registradas:

Q001 - Hotel Sol Real - Entrega tardía
Q002 - Restaurante El Patio - Producto equivocado
Q003 - Escuela Moderna - Factura incorrecta
Q004 - Hotel Plaza Dorada - Pedido incompleto
"""

        else:

            respuesta = """
Puedo responder consultas sobre:

- Factura RC001
- Factura RC002
- Factura RC003
- Clientes
- Catálogo de productos
- Quejas
- Devoluciones
- Facturación
- Crédito
- Envíos
- Horarios
"""

        return func.HttpResponse(
            json.dumps({"respuesta": respuesta}),
            mimetype="application/json",
            status_code=200,
            headers=headers
        )

    except Exception as e:

        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500,
            headers=headers
        )