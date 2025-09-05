# Enviando E-mails SMTP com Python
import os
import pathlib
import smtplib

from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / "aula185.html"  # Caminho do arquivo HTML


# Dados do remetente e destinatário
remetente = os.getenv("FROM_EMAIL", "")
destinatario = remetente  # Para este exemplo, enviaremos para o próprio remetente

# Configurações do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Porta para TLS
smtp_username = os.getenv("FROM_EMAIL", "")
smtp_password = os.getenv("EMAIL_PASSWORD", "")

# meMensagem de texto
with open(CAMINHO_HTML, "r") as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome="Helena")

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart["From"] = remetente
mime_multipart["To"] = destinatario
mime_multipart["Subject"] = "Este é o asunto  do e-mail"

corpo_email = MIMEText(texto_email, "html", "utf-8")
mime_multipart.attach(corpo_email)

# Enviando o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()  # Inicia a conexão TLS
    server.login(smtp_username, smtp_password)  # Faz o login no servidor SMTP
    server.send_message(mime_multipart)  # Envia o e-mail
    print("E-mail enviado com sucesso!")
