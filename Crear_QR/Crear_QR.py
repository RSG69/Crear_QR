import reflex as rx
import qrcode
import os
import time

QR_PATH = "assets/qr.png"

# ------------------------
# Funciones
# ------------------------
def generar_qr(texto: str):
    qr = qrcode.make(texto)
    qr.save(QR_PATH)

def eliminar_qr():
    if os.path.exists(QR_PATH):
        os.remove(QR_PATH)

# ------------------------
# State
# ------------------------
class State(rx.State):
    texto: str = ""
    qr_version: int = 0

    def crear_qr(self):
        # 1️⃣ borrar QR anterior
        eliminar_qr()

        # 2️⃣ generar nuevo QR
        if self.texto:
            generar_qr(self.texto)

            # 3️⃣ forzar recarga de imagen
            self.qr_version += 1

# ------------------------
# UI
# ------------------------
def index():
    return rx.center(
        rx.vstack(
            rx.heading("Generador de Código QR"),
            rx.input(
                placeholder="Escribe el texto o URL",
                value=State.texto,
                on_change=State.set_texto,
                width="300px",
            ),
            rx.button(
                "Generar QR",
                on_click=State.crear_qr,
            ),
            rx.cond(
                os.path.exists(QR_PATH),
                rx.image(
                    src=f"/qr.png?v={State.qr_version}",
                    width="200px",
                ),
            ),
            spacing="4",
        )
    )

# ------------------------
# App
# ------------------------
app = rx.App()
app.add_page(index)
