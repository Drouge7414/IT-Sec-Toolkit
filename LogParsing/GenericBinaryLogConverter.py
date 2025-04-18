import struct
import socket

def parse_log(filename):
    with open(filename, 'rb') as file:
        with open('parsed_output.txt', 'w') as output_file:
            while True:
                # Try to read 4 bytes for the username length
                length_bytes = file.read(4)
                if len(length_bytes) < 4:
                    break  # End of file or corrupted entry

                username_length = struct.unpack('>I', length_bytes)[0]

                username = file.read(username_length)
                if len(username) < username_length:
                    break  # Corrupted entry

                username = username.decode('utf-8')

                ip_bytes = file.read(4)
                if len(ip_bytes) < 4:
                    break
                ip = socket.inet_ntoa(ip_bytes)

                timestamp_bytes = file.read(4)
                if len(timestamp_bytes) < 4:
                    break
                timestamp = struct.unpack('>I', timestamp_bytes)[0]

                success_byte = file.read(1)
                if len(success_byte) < 1:
                    break
                success = bool(struct.unpack('>B', success_byte)[0])

                output_file.write(f"Username: {username}, IP: {ip}, Timestamp: {timestamp}, Success: {success}\n")

# Run the function
parse_log('logins(1).bin')
