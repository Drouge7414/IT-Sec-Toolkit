# Wireshark Cheat Sheet

## General Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `ip.addr == X.X.X.X` | Filters packets where the IP address (source or destination) is `X.X.X.X` | `ip.addr == 192.168.108.128` |
| `ip.src == X.X.X.X` | Filters packets with `X.X.X.X` as the source IP | `ip.src == 192.168.108.128` |
| `ip.dst == X.X.X.X` | Filters packets with `X.X.X.X` as the destination IP | `ip.dst == 192.168.108.129` |
| `tcp.port == 80` | Filters packets with a TCP destination port of `80` (HTTP) | `tcp.port == 80` |
| `tcp.flags.reset == 1` | Filters TCP packets with the RST (reset) flag set | `tcp.flags.reset == 1` |
| `tcp.flags.syn == 1` | Filters TCP packets with the SYN flag set (beginning of connection) | `tcp.flags.syn == 1` |
| `tcp.flags.fin == 1` | Filters TCP packets with the FIN flag set (end of connection) | `tcp.flags.fin == 1` |
| `tcp.seq == X` | Filters packets with the exact sequence number `X` | `tcp.seq == 12345678` |
| `ip.proto == 17` | Filters UDP traffic (Protocol 17) | `ip.proto == 17` |
| `icmp` | Filters ICMP traffic (ping and related protocols) | `icmp` |
| `http` | Filters HTTP traffic | `http` |
| `http.request` | Filters HTTP request messages | `http.request` |
| `http.response` | Filters HTTP response messages | `http.response` |
| `dns` | Filters DNS traffic | `dns` |
| `frame.len == X` | Filters packets with a frame length of exactly `X` bytes | `frame.len == 1500` |
| `frame.len >= X` | Filters packets with a frame length greater than or equal to `X` | `frame.len >= 2000` |
| `frame.len <= X` | Filters packets with a frame length less than or equal to `X` | `frame.len <= 500` |
| `tcp.analysis.retransmission` | Filters TCP retransmissions | `tcp.analysis.retransmission` |
| `tcp.analysis.out_of_order` | Filters out-of-order TCP packets | `tcp.analysis.out_of_order` |
| `tcp.analysis.duplicate_ack` | Filters TCP duplicate ACK packets | `tcp.analysis.duplicate_ack` |
| `ip.src != X.X.X.X` | Excludes packets with `X.X.X.X` as the source IP | `ip.src != 192.168.108.128` |
| `ip.dst != X.X.X.X` | Excludes packets with `X.X.X.X` as the destination IP | `ip.dst != 192.168.108.129` |
| `not ip.addr == X.X.X.X` | Excludes packets from or to `X.X.X.X` | `not ip.addr == 192.168.108.128` |
| `frame.time >= "YYYY-MM-DD HH:MM:SS"` | Filters packets from a specific time onward | `frame.time >= "2025-04-17 10:00:00"` |

## TCP-specific Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Filters the initial TCP SYN packets (connection request) | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| `tcp.flags.syn == 1 && tcp.flags.ack == 1` | Filters the second TCP packet in the 3-way handshake (SYN-ACK) | `tcp.flags.syn == 1 && tcp.flags.ack == 1` |
| `tcp.flags.fin == 1 && tcp.flags.ack == 1` | Filters the TCP FIN-ACK packet (connection teardown) | `tcp.flags.fin == 1 && tcp.flags.ack == 1` |
| `tcp.flags.rst == 1` | Filters TCP packets with the RST (reset) flag set | `tcp.flags.rst == 1` |
| `tcp.analysis.initial_rtt` | Filters TCP packets with initial round-trip time (RTT) values | `tcp.analysis.initial_rtt` |
| `tcp.analysis.fast_retransmission` | Filters TCP packets that are retransmissions (fast retransmission) | `tcp.analysis.fast_retransmission` |

## Protocol-specific Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `dns.qry.name == "example.com"` | Filters DNS query for the domain "example.com" | `dns.qry.name == "example.com"` |
| `http.request.uri contains "login"` | Filters HTTP requests containing the word "login" in the URI | `http.request.uri contains "login"` |
| `http.response.code == 200` | Filters HTTP responses with a status code 200 (OK) | `http.response.code == 200` |
| `http.response.code == 404` | Filters HTTP responses with a status code 404 (Not Found) | `http.response.code == 404` |
| `dns.flags.response == 1` | Filters DNS response packets | `dns.flags.response == 1` |

## Flow and Behavior Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `tcp.analysis.lost_segment` | Filters TCP packets that indicate lost segments (can help identify retransmission) | `tcp.analysis.lost_segment` |
| `tcp.analysis.ack_rtt` | Filters packets with Round-Trip Time (RTT) for TCP ACK packets | `tcp.analysis.ack_rtt` |
| `frame.time_delta` | Filters based on the time difference between consecutive packets | `frame.time_delta > 0.5` (for delays greater than 0.5 seconds) |

## Common Terms in Wireshark Analysis

| Term | Definition |
|------|------------|
| **SYN** | The TCP flag that initiates the 3-way handshake to establish a connection (SYN is sent to start communication). |
| **ACK** | The TCP flag used to acknowledge receipt of data in TCP connections (ACK is part of the handshake and connection teardown). |
| **RST** | Reset flag that indicates the connection should be reset (can happen if a packet is corrupted, out-of-order, or an error occurs). |
| **FIN** | The TCP flag that indicates the sender wants to terminate the connection gracefully (end of data transfer). |
| **Retransmission** | Occurs when a packet is sent again due to the sender not receiving an acknowledgment (usually due to packet loss or network congestion). |
| **Out-of-Order** | Refers to packets that arrive in a different sequence than expected, possibly due to network re-routing or congestion. |
| **Duplicate ACK** | A duplicate acknowledgment from the receiver indicating the receipt of data, but no new data since the last acknowledgment. |
| **RTT (Round-Trip Time)** | The time it takes for a signal to go from the sender to the receiver and back (can indicate network performance issues). |
| **HMAC (Hash-based Message Authentication Code)** | A method used to verify data integrity and authenticity by computing a hash of the message using a secret key. |
    """,
