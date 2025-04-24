import struct     # For interpreting binary data as C-style data structures
import socket     # For converting raw IP addresses into human-readable form

def parse_log(filename):
    # Open the binary log file for reading in binary mode ('rb')
    with open(filename, 'rb') as file:
        # Open (or create) a text file to write the parsed output
        with open('parsed_output.txt', 'w') as output_file:
            while True:
                # --- Read Username Length ---
                # Read the first 4 bytes to get the length of the username
                length_bytes = file.read(4)
                if len(length_bytes) < 4:
                    break  # Exit if end of file is reached or data is incomplete

                # Unpack the 4 bytes as a big-endian unsigned integer ('>I')
                username_length = struct.unpack('>I', length_bytes)[0]

                # --- Read Username String ---
                # Now read the actual username using the previously read length
                username = file.read(username_length)
                if len(username) < username_length:
                    break  # Exit if the entry is corrupted or incomplete

                # Decode the username from bytes to a string (UTF-8 encoding)
                username = username.decode('utf-8')

                # --- Read IP Address ---
                # Next 4 bytes represent an IPv4 address
                ip_bytes = file.read(4)
                if len(ip_bytes) < 4:
                    break  # Incomplete entry

                # Convert raw 4-byte IP to dotted-decimal string (e.g., 192.168.1.1)
                ip = socket.inet_ntoa(ip_bytes)

                # --- Read Timestamp ---
                # Next 4 bytes represent a timestamp as an unsigned integer
                timestamp_bytes = file.read(4)
                if len(timestamp_bytes) < 4:
                    break  # Incomplete entry

                # Unpack the timestamp (again, big-endian 4-byte integer)
                timestamp = struct.unpack('>I', timestamp_bytes)[0]

                # --- Read Success Byte ---
                # Next 1 byte tells whether the login was successful (1) or not (0)
                success_byte = file.read(1)
                if len(success_byte) < 1:
                    break  # Incomplete entry

                # Unpack the byte into a boolean (1 = True, 0 = False)
                success = bool(struct.unpack('>B', success_byte)[0])

                # --- Write to Output File ---
                # Write the parsed values in human-readable format to the text file
                output_file.write(
                    f"Username: {username}, IP: {ip}, Timestamp: {timestamp}, Success: {success}\n"
                )

# Call the function with the filename
parse_log('logins(1).bin')
