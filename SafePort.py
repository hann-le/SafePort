import socket
import os

open_ports = []

print("Scanning ports 1 to 1024...")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex(('localhost', port))
    if result == 0:
        print(f"Port {port} is open!")
        open_ports.append(port)
    s.close()

# Generate a simple HTML report
report_content = "<html><head><title>Port Scan Report</title></head><body>"
report_content += "<h2>Open Ports on localhost (1-1024)</h2><ul>"

for port in open_ports:
    report_content += f"<li>Port {port} is open</li>"

report_content += "</ul></body></html>"

# Save report next to this script/exe
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "securiscan_report.html")
with open(report_path, "w") as f:
    f.write(report_content)

print(f"Report saved as '{report_path}'.")
