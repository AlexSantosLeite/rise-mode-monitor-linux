# Rise Mode Aura Ice - Linux Hardware Monitor 🐧🌡️

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hardware](https://img.shields.io/badge/Hardware-Rise%20Mode%20Aura%20Ice-red.svg)](#)

Este projeto implementa o **Protocolo Mimicry** via engenharia reversa para permitir que os Water Coolers da linha **Rise Mode Aura Ice** exibam temperaturas de hardware (CPU/GPU) nativamente no Linux. Ideal para setups de alta performance, como o **Ryzen 7 9800X3D**.

---

## 🛠️ Funcionalidades

- **Monitoramento em Tempo Real:** Leitura precisa via `psutil`.
- **Protocolo Mimicry:** Bypass no protocolo proprietário para atualização da tela LCD.
- **Service-Ready:** Configuração completa para rodar como daemon do sistema (`systemd`).
- **Suporte a Distros Atômicas:** Guia específico para Bazzite, SteamOS e Fedora Silverblue.

## 📂 Estrutura do Projeto

* `aura-monitor.py`: Script principal de monitoramento.
* `aura-monitor.service`: Arquivo de unidade do Systemd para automação.
* `99-aura-cooler.rules`: Regra de Udev para permissões de barramento USB.

---

## 🚀 Instalação (Ubuntu, Debian, Fedora Workstation)

### 1. Dependências de Sistema
# bash
# Debian / Ubuntu / Mint
sudo apt update && sudo apt install python3-pip libusb-1.0-0-dev libudev-dev -y

# Fedora Workstation
sudo dnf install python3-devel libusb1-devel systemd-devel -y

### 2.Configuração do Ambiente

git clone [https://github.com/AlexSantosLeite/rise-mode-monitor-linux.git](https://github.com/AlexSantosLeite/rise-mode-monitor-linux.git)
cd rise-mode-monitor-linux
python3 -m venv venv
source venv/bin/activate
pip install pyusb psutil

### 3.Permissões USB (Udev)

sudo cp 99-aura-cooler.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger

🏗️ Guia para Distros Atômicas (Bazzite / SteamOS / Silverblue)
Sistemas imutáveis possuem restrições de execução na /var/home e políticas rígidas de SELinux.

1. Layering de Bibliotecas
No Host (fora de containers):

# Reinicie o sistema após o comando acima
rpm-ostree install libusb1-devel python3-pip

### 2. Permissões e Segurança (SELinux)
Caso o serviço retorne erro 203/EXEC, é necessário rotular o script para o kernel:

chmod +x aura-monitor.py
sudo chcon -t bin_t aura-monitor.py

3. Ajuste do Serviço
Edite o arquivo aura-monitor.service e certifique-se de que os caminhos apontam para /var/home/SEU_USUARIO/... (caminho absoluto).

⚙️ Automação (Início com o Sistema)
Para que o monitoramento inicie sozinho no boot:

1. Edite o arquivo aura-monitor.service com seus paths locais.

2. Mova para a pasta do sistema:

sudo cp aura-monitor.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now aura-monitor.service

Comandos Úteis do "SOC"
Verificar Status: sudo systemctl status aura-monitor.service

Logs em tempo real: sudo journalctl -u aura-monitor.service -f

🤝 Contribuições
Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request com melhorias no protocolo ou suporte a novos modelos de Water Cooler.

Desenvolvido por Alex Santos Leite 🛡️

---

### O que eu melhorei pra você:
1.  **Badges:** Dá um ar de projeto sério e bem mantido.
2.  **Seção de Distros Atômicas:** Agora o seu "sofrimento" de hoje virou documentação oficial para outros usuários de Bazzite.
3.  **Comandos do SOC:** Como você trabalha com monitoramento, usar termos como "Logs em tempo real" e "SOC" deixa o projeto com a sua cara.
4.  **Organização:** Separei bem o que é dependência de sistema do que é configuração do Python.
5.  
