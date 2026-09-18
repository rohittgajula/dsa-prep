# Models, Layers & the Link Layer

`Week 6` · Computer Networks

## OSI vs TCP/IP

```mermaid
graph TB
    subgraph OSI["OSI — 7 layers (teaching model)"]
        A7[7 Application] --> A6[6 Presentation] --> A5[5 Session]
        A5 --> A4[4 Transport] --> A3[3 Network] --> A2[2 Data Link] --> A1[1 Physical]
    end
    subgraph TCPIP["TCP/IP — 4 layers (what actually runs)"]
        B4[Application<br/>HTTP, DNS, SMTP] --> B3[Transport<br/>TCP, UDP]
        B3 --> B2[Internet<br/>IP, ICMP] --> B1[Link<br/>Ethernet, WiFi]
    end
```

OSI layers 5–7 barely exist in practice. **The real internet runs the TCP/IP stack** — say that, it shows you know the difference between the model and reality.

### Encapsulation — headers added on the way down

```
  Application    │              DATA                │
                 ▼
  Transport      │ TCP hdr │    DATA                │   ← SEGMENT
                 ▼
  Network        │ IP hdr │ TCP hdr │ DATA          │   ← PACKET
                 ▼
  Link           │ Eth hdr │ IP hdr │ TCP hdr │ DATA │ Eth trailer │  ← FRAME
                 ▼
  Physical                     bits on the wire
```

Each layer treats everything above it as opaque payload. That is what lets you swap WiFi for Ethernet without touching TCP.

### Layer numbers matter in practice

| Device / term | Layer |
|---|---|
| Hub | L1 — repeats blindly to every port |
| **Switch** | **L2** — forwards by MAC |
| **Router** | **L3** — forwards by IP |
| L4 load balancer | transport — routes on IP/port, cannot see HTTP |
| L7 load balancer | application — routes on path, header, cookie |

## MAC addresses, switches and ARP

```mermaid
sequenceDiagram
    participant A as Host A<br/>192.168.1.10
    participant N as LAN (broadcast)
    participant B as Host B<br/>192.168.1.20
    A->>N: ARP: "who has 192.168.1.20?"<br/>(broadcast to everyone)
    B->>A: ARP reply: "that's me, MAC bb:bb:bb"
    Note over A: cache it in the ARP table
    A->>B: Ethernet frame to bb:bb:bb
```

A **switch** learns which MAC lives on which port by inspecting source addresses, then forwards frames only to the correct port. A **hub** repeats to every port — which is why switches eliminated collisions.

> **ARP has no authentication.** That enables ARP spoofing / man-in-the-middle on a LAN. Worth mentioning.

**Broadcasts do not cross routers** — which is exactly why ARP is strictly local, and why VLANs exist to shrink broadcast domains.

## MTU and fragmentation — a real debugging story

```
  Ethernet MTU = 1500 bytes

  packet 4000 bytes ──► router with a 1500 MTU link
                        │
       DF bit clear ────┼──► fragments into 3 pieces
                        │    (lose ONE → retransmit ALL)
       DF bit set ──────┴──► DROPS it, returns
                             ICMP "fragmentation needed"
                             → sender shrinks (Path MTU Discovery)
```

```
  ╔════════════════════════════════════════════════════════════╗
  ║ "Small requests work, large uploads hang forever"          ║
  ║                                                            ║
  ║ → a firewall is blocking ICMP, so PMTUD gets no feedback   ║
  ║ → the sender never learns to shrink its packets            ║
  ║                                                            ║
  ║ Naming this diagnosis signals real debugging experience.   ║
  ╚════════════════════════════════════════════════════════════╝
```

VPNs and tunnels reduce the effective MTU and cause the same symptom.

## Interview checklist

- [ ] Both stacks, in order, one protocol per layer
- [ ] Trace a packet down and back up through encapsulation
- [ ] Hub vs switch vs router, by layer
- [ ] What happens when two hosts on the same subnet communicate (ARP, then direct frame — **no router involved**)
- [ ] The MTU/ICMP debugging story
