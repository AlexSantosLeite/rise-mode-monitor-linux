# Rise Mode Aura 360mm - Linux Monitor Driver 🐧❄️

Este é um driver em espaço de usuário (User-space Driver) escrito em Python para habilitar o display de temperatura nos Water Coolers Rise Mode (modelos 360mm com chip `aa88:8666`) no Linux.

## 🔍 Engenharia Reversa
Diferente das soluções oficiais para Windows, este script foi desenvolvido do zero através da análise de protocolos USB HID:
- **ID do Dispositivo:** `aa88:8666`
- **Protocolo:** Baseado em XuanFang com assinatura `0x55 0xAA`.
- **Mapeamento:** Identificamos o **Offset 28** como o registrador de exibição para o sensor principal.
- **Técnica:** Implementação de "Staircase Mimicry" para manter o dispositivo ativo.

## 🛠️ Como usar no Bazzite/Fedora

1. **Permissões USB:** `sudo cp 99-aura-cooler.rules /etc/udev/rules.d/`
   `sudo udevadm control --reload-rules && sudo udevadm trigger`

2. **Instalação:**
   Copie o script para `~/.local/bin/aura-monitor.py` e dê permissão de execução.

3. **Automação:**
   Instale o arquivo `aura-monitor.service` em `/etc/systemd/system/` e ative com:
   `sudo systemctl enable --now aura-monitor.service`

## 📝 Requisitos
- Python 3
- Bibliotecas: `pyusb`, `psutil`

Desenvolvido como projeto de estudo para a área de Cybersecurity (SOC) e ADS.
