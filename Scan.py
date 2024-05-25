import socket
from scapy.all import Ether, ARP, srp, IP, TCP, sr1

def arp_scan(interface, ip_range):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)

    answered, unanswered = srp(arp_request, timeout=2, iface=interface, inter=0.1)

    devices = []

    for pkt in answered:
        ip = pkt[1][ARP].psrc
        mac = pkt[1][ARP].hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "N/A"
        devices.append((ip, mac, hostname))

    return devices

def port_scan(target_ip, port):
    open_ports = []
    # Crear un paquete TCP para el puerto 8080
    tcp_syn = IP(dst=target_ip) / TCP(dport=port, flags="S")
    # Enviar el paquete y esperar la respuesta
    response = sr1(tcp_syn, timeout=1, verbose=0)
    # Verificar si el puerto 8080 está abierto
    if response and response.haslayer(TCP) and response[TCP].flags == 18:
        open_ports.append(port)
    return open_ports

def detect_os(target_ip):
    # No necesitas modificar esta función, ya que solo verifica si el puerto 8080 está abierto
    open_ports = port_scan(target_ip, 8080)  # Solo escanea el puerto 8080
    os_info = "Unknown"
    if 8080 in open_ports:
        os_info = "Probablemente un servidor web"
    return os_info

def main():
    interface = input("Ingresa el nombre de la interfaz de red (por ejemplo, Wi-Fi): ")
    ip_range = input("Ingresa el rango de IP a escanear (por ejemplo, 192.168.1.0/24): ")

    print("Escaneando dispositivos en la red...")
    devices = arp_scan(interface, ip_range)

    print("Dispositivos encontrados:")
    for device in devices:
        print("IP:", device[0], "\tMAC:", device[1], "\tHostname:", device[2])
        
        # Escanear el puerto 8080 en el dispositivo
        open_ports = port_scan(device[0], 8080)
        if open_ports:
            print("Puerto 8080 abierto en el dispositivo.")
        else:
            print("El puerto 8080 está cerrado en el dispositivo.")
        
        # Detectar el sistema operativo del dispositivo
        os_info = detect_os(device[0])
        print("Sistema operativo:", os_info)

if __name__ == "__main__":
    main()
