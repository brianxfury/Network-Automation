from netmiko import ConnectHandler

connection = ConnectHandler(
    host="172.16.10.12", username="admin", password="cisco", device_type="cisco_ios"
)
output = connection.send_command("show ip interface brief")
print(output)
connection.disconnect()