
import socket

def scan_ports():
    open_ports = []
    for port in range(1, 1025):  # common ports range
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex(("localhost", port)) == 0:
            open_ports.append(port)
        s.close()
    return open_ports

def create_html_report(open_ports):
    with open("securiscan_report.html", "w") as report:
        report.write("<html><head><title>SecuriScan Report</title></head><body>")
        report.write("<h1>SecuriScan - Port Scan Report</h1>")
        if open_ports:
            report.write("<p>The following ports are open:</p><ul>")
            for port in open_ports:
                report.write(f"<li>Port {port}</li>")
            report.write("</ul>")
        else:
            report.write("<p>No open ports found.</p>")
        report.write("</body></html>")
    print("Report saved as 'securiscan_report.html'.")

def main():
    print("Scanning ports 1 to 1024...")
    ports = scan_ports()
    create_html_report(ports)

if __name__ == "__main__":
    main()
