import reflex as rx
import qrcode
import io
import base64

class State(rx.State):
    texto: str = ""
    qr_base64: str = ""

    def crear_qr(self):
        if not self.texto:
            return

        # Crear QR en memoria
        qr = qrcode.make(self.texto)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")

        # Convertir a base64
        img_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Guardar en el estado
        self.qr_base64 = f"data:image/png;base64,{img_base64}"

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
                State.qr_base64 != "",
                rx.image(
                    src=State.qr_base64,
                    width="200px",
                ),
            ),
            spacing="4",
        )
    )

app = rx.App()
app.add_page(index)
