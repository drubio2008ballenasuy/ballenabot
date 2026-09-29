import os
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configurar logging para ver el estado en Render
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TOKEN = "1264699838:AAHdDTIKFEBqz281xKi55oYalIvO_mGc5z8"

# Mini servidor web para satisfacer el requisito de Render en servicios web
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Ballenas UY Bot is alive!")

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

async def reglas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "Reglas de la Comunidad Ballenas UY\n\n"
        "Por favor, mantengamos el respeto, compartamos información verídica sobre avistamientos "
        "y evitemos spam.\n\n"
        "Lee el reglamento completo aquí:\n"
        "https://sites.google.com/view/bfauy/inicio"
    )
    await update.message.reply_text(texto)

async def normativa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "Normativa y Protección\n\n"
        "Conoce las leyes y pautas vigentes para la navegación responsable y la observación "
        "de la ballena franca austral:\n\n"
        "https://sites.google.com/view/bfauy/inicio"
    )
    await update.message.reply_text(texto)

async def ballenafranca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "La Ballena Franca Austral\n\n"
        "La Ballena Franca Austral (Eubalaena australis) es un visitante ilustre de nuestras costas. "
        "Se caracteriza por sus callosidades únicas en la cabeza y su comportamiento pacífico.\n\n"
        "Descubre más sobre su historia, comportamiento y cómo las estudiamos en nuestro sitio web:\n"
        "https://sites.google.com/view/bfauy/inicio"
    )
    await update.message.reply_text(texto)

async def fotoidentificacion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "Catalogo de Fotoidentificacion\n\n"
        "A traves de los patrones unicos de las callosidades en la cabeza de cada ejemplar, "
        "realizamos el seguimiento individual de las ballenas francas que visitan la zona.\n\n"
        "Conoce mas sobre este proyecto de identificacion y registro en nuestra web:\n"
        "https://sites.google.com/view/bfauy/inicio"
    )
    await update.message.reply_text(texto)

def main():
    # Iniciar el servidor web en segundo plano para cumplir con Render
    t = threading.Thread(target=run_http_server, daemon=True)
    t.start()

    # Construir la aplicación del bot
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("reglas", reglas))
    application.add_handler(CommandHandler("normativa", normativa))
    application.add_handler(CommandHandler("ballenafranca", ballenafranca))
    application.add_handler(CommandHandler("fotoidentificacion", fotoidentificacion))

    print("El bot esta en marcha y esperando comandos!")
    application.run_polling()

if __name__ == "__main__":
    main()
