import requests

server_url = "http://localhost:5000"

def send_message(content):
    data = {"content": content}
    response = requests.post(f"{server_url}/send", json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")

def receive_messages():
    response = requests.get(f"{server_url}/receive")
    if response.status_code == 200:
        messages = response.json().get("messages", [])
        print("Received Messages:")
        for message in messages:
            print(f"- {message}")
    else:
        print("Failed to retrieve messages.")

if __name__ == '__main__':
    while True:
        choice = input("Choose an action (send/receive/exit): ").lower()
        
        if choice == "send":
            content = input("Enter message to send: ")
            send_message(content)
        elif choice == "receive":
            receive_messages()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please try again.")
