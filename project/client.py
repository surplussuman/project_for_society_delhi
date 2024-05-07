import cv2
from imutils.video import VideoStream
import time
import socket

SERVER = "172.16.23.71" #server ip address
PORT = 8080 #port same as server listen port
ADDR = (SERVER, PORT)

# RTSP URL
#rtsp_url = "rtsp://admin:admin@123@172.16.21.100:554/cam/realmonitor?channel=3&subtype=0&unicast=true&proto=Onvif"
rtps_url = "rtsp://admin:LYDLKK@192.168.0.169:554/H.264"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("connected")

print("capturing camera stream")
# Create VideoStream object
vs = VideoStream(rtsp_url).start()
print("started")

time.sleep(1.0)

while True:
    try:
        # Read the next frame from the stream
        frame = vs.read()

        # Convert to frame to byte stream
        success, bytes_data = cv2.imencode('.jpg', frame)

        # Send bytes
        client.sendall(bytes_data)

    except Exception as e:
        if e == KeyboardInterrupt:
            # close on keyboard intrupt
            print("Exiting")
            break
    else:
        pass


# Cleanup
client.close()
cv2.destroyAllWindows()
vs.stop()
'''
import cv2
from imutils.video import VideoStream
import socket
import time

#SERVER = "172.16.23.71"  # Server IP address
SERVER = "192.168.1.4"
PORT = 8080  # Port same as server listen port
ADDR = (SERVER, PORT)

# RTSP URL
rtsp_url = "rtsp://admin:admin@123@172.16.21.100:554/cam/realmonitor?channel=3&subtype=0&unicast=true&proto=Onvif"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("Connected")

print("Capturing camera stream")
# Create VideoStream object
vs = VideoStream(0).start()
print("Started")

# Initialize buffer and frame counter
buffer = []
frame_count = 0

while True:
    try:
        # Read the next frame from the stream
        frame = vs.read()

        # Convert frame to byte stream
        success, bytes_data = cv2.imencode('.jpg', frame)

        # Add frame to buffer
        buffer.append(bytes_data)

        # Send frames in buffer
        if len(buffer) > 0:
            client.sendall(buffer.pop(0))

        # Reset frame count and buffer if needed
        if frame_count == 30:  # Adjust frame count as needed for your desired frame rate
            frame_count = 0
            buffer = []
        else:
            frame_count += 1

    except Exception as e:
        print(f"Error: {e}")
        break

# Cleanup
client.close()
cv2.destroyAllWindows()
vs.stop()
'''