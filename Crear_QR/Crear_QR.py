import reflex as rx
import qrcode
import os

QR_PATH = "assets/qr.png"

def generar_qr(texto: str):
    qr = qrcode.make(texto)
    qr.save(QR_PATH)

class State(rx.State):
    texto: str = ""

    def crear_qr(self):
        if self.texto:
            generar_qr(self.texto)

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
                rx.image(src="/qr.png", width="200px"),
            ),
            spacing="4",
        )
    )

app = rx.App()
app.add_page(index)
