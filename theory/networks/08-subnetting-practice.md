# Subnetting — Worked Practice

`Week 7` · Computer Networks

Guaranteed marks in a written round. This is drill material — work through it with a pen.

---

## The method

```
  1. Convert the CIDR to a mask
  2. Block size = 256 − (the interesting mask octet)
  3. Subnets start at multiples of the block size
  4. Usable hosts = 2^(host bits) − 2
       (all-zeros = network ID, all-ones = broadcast)
```

## The table to memorise

| CIDR | Mask | Block | Hosts | Subnets in a /24 |
|---|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 | 1 |
| /25 | 255.255.255.128 | 128 | 126 | 2 |
| /26 | 255.255.255.192 | 64 | 62 | 4 |
| /27 | 255.255.255.224 | 32 | 30 | 8 |
| /28 | 255.255.255.240 | 16 | 14 | 16 |
| /29 | 255.255.255.248 | 8 | 6 | 32 |
| /30 | 255.255.255.252 | 4 | **2** | 64 |
| /31 | 255.255.255.254 | 2 | 2* | point-to-point only |
| /32 | 255.255.255.255 | 1 | 1 | single host |

\* /31 is a special case (RFC 3021) — no network/broadcast, both addresses usable on point-to-point links.

---

## Worked example 1

> **Given `192.168.10.0/26`, list all subnets with their ranges.**

```
  /26 → 26 network bits, 6 host bits
  mask       = 255.255.255.192       (192 = 11000000)
  block size = 256 − 192 = 64
  hosts      = 2^6 − 2 = 62

  Subnet 1:  192.168.10.0    – .63
             network .0      broadcast .63     usable .1   – .62
  Subnet 2:  192.168.10.64   – .127
             network .64     broadcast .127    usable .65  – .126
  Subnet 3:  192.168.10.128  – .191
             network .128    broadcast .191    usable .129 – .190
  Subnet 4:  192.168.10.192  – .255
             network .192    broadcast .255    usable .193 – .254
```

---

## Worked example 2

> **Which subnet does `172.16.35.123/20` belong to?**

```
  /20 → the interesting octet is the THIRD (20 = 8 + 8 + 4)
  third octet mask = 11110000 = 240
  block size = 256 − 240 = 16

  Third-octet boundaries: 0, 16, 32, 48, 64, ...
  35 falls between 32 and 47

  network   = 172.16.32.0
  broadcast = 172.16.47.255
  usable    = 172.16.32.1  –  172.16.47.254
  hosts     = 2^12 − 2 = 4094
```

---

## Worked example 3 — VLSM (variable length)

> **You have `192.168.1.0/24`. Allocate: Sales 100 hosts, Eng 50, Ops 25, two point-to-point links.**

```
  ALWAYS ALLOCATE LARGEST FIRST — otherwise you fragment the space.

  Sales  100 hosts → need 126 → /25   192.168.1.0/25     (.0   – .127)
  Eng     50 hosts → need  62 → /26   192.168.1.128/26   (.128 – .191)
  Ops     25 hosts → need  30 → /27   192.168.1.192/27   (.192 – .223)
  Link 1   2 hosts → need   2 → /30   192.168.1.224/30   (.224 – .227)
  Link 2   2 hosts → need   2 → /30   192.168.1.228/30   (.228 – .231)

  remaining .232 – .255 free for future use

  ┌────────────/25────────────┬──────/26─────┬───/27──┬/30┬/30┬ free ┐
  0                          127            191      223 227 231    255
```

---

## Practice set — do these by hand

| # | Question |
|---|---|
| 1 | `10.0.0.0/22` — how many hosts? What is the broadcast address? |
| 2 | Which subnet contains `192.168.5.200/27`? |
| 3 | Split `172.20.0.0/16` into subnets of 500 hosts each. What CIDR? How many subnets? |
| 4 | Is `10.1.1.5/24` on the same network as `10.1.2.5/24`? |
| 5 | You need 6 subnets from `192.168.100.0/24`. What mask? |

<details>
<summary>Answers</summary>

1. /22 → 10 host bits → 1022 hosts. Block size 4 in the third octet → network `10.0.0.0`, broadcast `10.0.3.255`.
2. /27 → block 32. Boundaries 192, 224. 200 falls in 192–223 → network `192.168.5.192`, broadcast `192.168.5.223`.
3. 500 hosts → need 512 → 9 host bits → **/23**. From /16 that is 2^(23−16) = **128 subnets**.
4. **No.** With /24 the network is the first three octets — `10.1.1.0` vs `10.1.2.0` are different networks and need a router.
5. 6 subnets → need 8 → 3 subnet bits → **/27** (255.255.255.224), giving 8 subnets of 30 hosts.

</details>

---

## Cloud gotcha

```
  ╔════════════════════════════════════════════════════════════╗
  ║ AWS RESERVES 5 ADDRESSES PER SUBNET, NOT 2.                ║
  ║                                                            ║
  ║   .0  network        .1  VPC router      .2  DNS           ║
  ║   .3  reserved       .255 broadcast (unused but reserved)  ║
  ║                                                            ║
  ║ A /28 gives you 11 usable addresses in AWS, not 14.        ║
  ║ Catches people out when sizing subnets for EKS pods.       ║
  ╚════════════════════════════════════════════════════════════╝
```

Common VPC pattern: `/16` for the VPC, `/24` per subnet, one subnet per availability zone.

---

## Interview checklist

- [ ] The CIDR table from memory
- [ ] Block size = 256 − mask octet
- [ ] Given any IP/CIDR, state network, broadcast, usable range, host count
- [ ] VLSM — allocate largest first
- [ ] AWS reserves 5
