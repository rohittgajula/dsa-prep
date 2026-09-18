# Computer Networks

`Weeks 6–10` of the prep plan.

| # | File | Topics |
|---|---|---|
| 01 | [Models & Link Layer](01-models-and-layers.md) | OSI/TCP-IP, encapsulation, MAC, switches, ARP, MTU |
| 02 | [IP & Routing](02-ip-and-routing.md) | subnetting, CIDR, NAT, OSPF/BGP overview, ICMP, IPv6 |
| 03 | [TCP & UDP](03-tcp-udp.md) | handshake, TIME_WAIT, flow vs congestion control, QUIC, sockets |
| 04 | [DNS, HTTP & TLS](04-dns-http-tls.md) | resolution chain, HTTP/1-2-3, TLS, cookies, CORS, caching |
| 05 | [Troubleshooting Toolkit](05-toolkit.md) | dig/curl/ss/tcpdump, latency vs bandwidth, bufferbloat |
| 06 | [**OSI 7 Layers in Detail**](06-osi-layers-in-detail.md) | every layer: function, PDU, address, devices, protocols, headers |
| 07 | [Architectures & Topologies](07-architectures-and-topologies.md) | client-server vs P2P, tiers, topologies, switching, VLAN, VPN, STUN/TURN, firewalls, WiFi |
| 08 | [Subnetting Practice](08-subnetting-practice.md) | the method, the CIDR table, worked examples, a practice set with answers |
| 09 | [**Routing Protocols**](09-routing-protocols.md) | RIP & count-to-infinity, OSPF areas & Dijkstra, BGP path selection & hijacks, anycast |
| 10 | [**Network Security**](10-network-security.md) | ARP spoofing, DNS attacks, DDoS & SYN cookies, TLS in depth, IPsec, WiFi, zero trust |
| 11 | [**Application Protocols**](11-application-protocols.md) | SMTP/IMAP/POP3, SPF/DKIM/DMARC, FTP modes, SSH tunnels, WebSockets, gRPC, DHCP, NTP |
| 12 | [**Performance & Modern**](12-performance-and-modern-networking.md) | congestion algorithms, BDP, QoS, SDN, VXLAN overlays, Kubernetes networking, QUIC |

## The five that come up most

1. **"What happens when you type google.com"** — rehearse the 3-minute version
2. **Subnetting** — given a CIDR, state mask, host count, ranges
3. **TCP handshake + TIME_WAIT** — draw it, explain why 3 and why 4
4. **TLS handshake** — and *why* both asymmetric and symmetric crypto
5. **TCP vs UDP** — the table, plus why DNS uses UDP

## Connections to the rest of the prep

| Networking concept | Where it reappears |
|---|---|
| OSPF runs **Dijkstra** | [Dijkstra pattern](../../patterns/graphs/dijkstra.md) |
| DNS, CDN, proxies, anycast | [System Design: edge](../system-design/02-edge-and-load-balancing.md) |
| TIME_WAIT / port exhaustion | [System Design](../system-design/03-scaling.md) — connection pooling |
| TLS, CORS, cookies | [System Design: security](../system-design/09-apis-and-security.md) |
| WebSocket backplane | [System Design: messaging](../system-design/06-messaging-and-kafka.md) |
| Latency is physics | why CDNs and edge caches exist |
| Kubernetes networking | [OS: containers](../os/09-virtualisation-and-security.md) |
| Clock skew | [Coordination: Snowflake IDs](../system-design/07-coordination-and-consistency.md) |
