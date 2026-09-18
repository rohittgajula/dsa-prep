# Computer Networks

`Weeks 6–10` of the prep plan.

| # | File | Topics |
|---|---|---|
| 01 | [Models & Link Layer](01-models-and-layers.md) | OSI/TCP-IP, encapsulation, MAC, switches, ARP, MTU |
| 02 | [IP & Routing](02-ip-and-routing.md) | subnetting, CIDR, NAT, OSPF/BGP, ICMP, IPv6 |
| 03 | [TCP & UDP](03-tcp-udp.md) | handshake, TIME_WAIT, flow vs congestion control, QUIC, sockets |
| 04 | [DNS, HTTP & TLS](04-dns-http-tls.md) | resolution chain, HTTP/1-2-3, TLS, cookies, CORS, caching |
| 05 | [Troubleshooting Toolkit](05-toolkit.md) | dig/curl/ss/tcpdump, latency vs bandwidth, bufferbloat |
| 06 | [**OSI 7 Layers in Detail**](06-osi-layers-in-detail.md) | every layer: function, PDU, address, devices, protocols, headers |
| 07 | [Architectures & Topologies](07-architectures-and-topologies.md) | client-server vs P2P, tiers, topologies, switching, VLAN, VPN, STUN/TURN, firewalls, WiFi |
| 08 | [Subnetting Practice](08-subnetting-practice.md) | the method, the CIDR table, 3 worked examples, a practice set with answers |

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
| DNS, CDN, proxies | System Design — the whole edge layer |
| TIME_WAIT / port exhaustion | System Design — connection pooling |
| TLS, CORS, cookies | System Design — the security section |
| Latency is physics | System Design — why CDNs and edge caches exist |
