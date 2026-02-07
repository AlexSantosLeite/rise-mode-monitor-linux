import usb.core
import time
import os

def get_cpu_temp():
    try:
        # Lendo do k10temp (hwmon3) que confirmamos antes
        with open("/sys/class/hwmon/hwmon3/temp1_input", "r") as f:
            return int(int(f.read()) / 1000)
    except:
        return 0

dev = usb.core.find(idVendor=0xaa88, idProduct=0x8666)

if dev:
    try:
        if dev.is_kernel_driver_active(0): dev.detach_kernel_driver(0)
        dev.set_configuration()

        print("🚀 [SOC DEPLOY] Iniciando Monitoramento com Protocolo Mimicry...")
        print("A tela deve atualizar do 28 para a temperatura real agora.")

        while True:
            temp = get_cpu_temp()
            
            # 1. Criamos a "Escada" exata que a tela aceitou no staircase.py
            payload = bytearray([i for i in range(64)])
            
            # 2. Mantemos a assinatura XuanFang
            payload[0] = 0x55
            payload[1] = 0xaa
            
            # 3. Injetamos a Temperatura no Offset 28 (o lugar do '28')
            # Também injetamos no Byte 0, por segurança
            payload[0] = temp
            payload[28] = temp
            
            dev.write(0x01, payload)
            
            print(f"🌡️ Ryzen 7 9800X3D: {temp}°C | Enviado via Offset 28", end="\r")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Monitoramento finalizado.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
else:
    print("❌ Dispositivo não encontrado.")
