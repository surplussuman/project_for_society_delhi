import socket
import cv2
import numpy as np

SERVER = "192.168.0.143" #socket ip
PORT = 8080 #server listen port
HEADER = 6220800

ADDR = (SERVER, PORT)

# Creating socket
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
except:
    with socket.error as e:
        print(str(e))

# Listening for new connections
server.listen(2)
print("listening....")

# Accept connection
connection_socket, addr = server.accept()
print("accepted")

# Convert bytes data to frame
def bytes_to_opencv_frame(byte_data):
    np_array = np.frombuffer(byte_data, np.uint8)
    frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return frame

while True:
    try:
        # Recive data
        bytes_data = connection_socket.recv(HEADER)
        frame = bytes_to_opencv_frame(bytes_data)

        # Show camera stream
        cv2.imshow("Frame", frame)

        # Exit on pressing "q"
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    except:
        pass
# Cleanup
server.close()
cv2.destroyAllWindows()
'''
import socket
import cv2
import numpy as np

SERVER = "192.168.1.4"  # Socket IP
PORT = 8080  # Server listen port
HEADER = 6220800

ADDR = (SERVER, PORT)

# Creating socket
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
except Exception as e:
    print(f"Error: {e}")

# Listening for new connections
server.listen(2)
print("Listening....")

# Accept connection
connection_socket, addr = server.accept()
print("Accepted")

while True:
    try:
        # Receive data
        bytes_data = connection_socket.recv(HEADER)

        # Check if bytes_data is empty
        if not bytes_data:
            continue

        # Decode bytes to frame
        np_array = np.frombuffer(bytes_data, np.uint8)
        frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        # Check if frame is valid
        if frame is None or frame.size == 0:
            print("Invalid frame received")
            print(f"Frame size: {frame.shape if frame is not None else 'None'}")
            continue

        # Process and display frame
        cv2.imshow("Frame", frame)

        # Exit on pressing "q"
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    except Exception as e:
        print(f"Error: {e}")
        break

# Cleanup
server.close()
cv2.destroyAllWindows()
'''