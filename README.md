# 📡 Comunicação Cliente-Servidor em Python

Este projeto demonstra uma implementação básica de comunicação **cliente-servidor usando sockets TCP** com Python. Ele permite o envio e recebimento de mensagens entre dois dispositivos que podem estar em redes diferentes, após configurado o redirecionamento de portas e IPs públicos.

## 🔧 Arquivos

- `servidor.py` – Inicia um servidor TCP que aguarda conexões na porta especificada. Após conexão, ele recebe mensagens do cliente e envia uma resposta de confirmação.
- `cliente.py` – Conecta-se ao servidor remoto via TCP, envia mensagens interativas e exibe as respostas recebidas.

## 🌐 Funcionalidade

- Comunicação bidirecional via socket.
- Compatível com redes diferentes (LAN/WAN), desde que configurado com IP público e redirecionamento de portas.
- Interação contínua com troca de mensagens até que o cliente envie `"sair"`.

## 🚀 Como executar

**Servidor:**
```bash
python servidor.py
```

**Cliente:**
```bash
python cliente.py
```

> Obs: Altere os valores de `host` e `port` nos scripts conforme sua rede e necessidade.

## 🔒 Segurança

Esta é uma implementação básica sem criptografia. Para uso em produção ou em redes públicas, recomenda-se o uso de `SSL/TLS` para proteção dos dados transmitidos.
