# 🌐 Computer Networks Projects - Spring 2022

[![Made With](https://img.shields.io/badge/Made%20with-Python%20%26%20Mininet-blue)]()
[![University](https://img.shields.io/badge/University-IUT-orange)]()

---

## 📚 Table of Contents

- [About The Repository](#about-the-repository)
- [Projects](#projects)
  - [Project 1: Basic Mininet Topology and Commands](#project-1-basic-mininet-topology-and-commands)
  - [Project 2: Traffic Analysis with Wireshark](#project-2-traffic-analysis-with-wireshark)
  - [Project 3: Custom Topology and Flow Configuration](#project-3-custom-topology-and-flow-configuration)
- [How to Use](#how-to-use)

---

## 📖 About The Repository

This repository contains projects completed for the **Computer Networks** course at **Isfahan University of Technology (Spring 2022)**.

All projects are focused on **network simulation using Mininet**, including network traffic capturing, analyzing flow behaviors, designing custom topologies, and configuring OpenFlow rules.

---

## 📁 Projects

### Project 1: Basic Mininet Topology and Commands
- Install and set up **Mininet**.
- Use the built-in **single** topology (one switch, multiple hosts).
- Execute and analyze outputs from the following commands:
  - `nodes`
  - `net`
  - `dump`
- Create and explain **three different Mininet topologies** besides the default one.
- Provide diagrams and analysis for each custom topology.

📄 Reference: [`پروژه یک-4002.pdf`](./path/to/پروژه%20یک-%204002.pdf)

---

### Project 2: Traffic Analysis with Wireshark
- Install **Wireshark** and capture packets in a Mininet simulated network.
- Identify and explain network control messages like:
  - `hello`
  - `feature request` and `feature reply`
  - `packet_in`
- Simulate **ICMP (ping)** traffic and analyze the captured ICMP packets.
- Measure and analyze **link performance** using `iperf` in Mininet.

📄 Reference: [`پروژه دو-4002.pdf`](./path/to/پروژه%20دو-4002.pdf)

---

### Project 3: Custom Topology and Flow Configuration
- Create a **custom topology** in Mininet using **Python scripting**:
  - At least **11 hosts and 11 switches**.
- Test host connectivity using `ping`.
- Analyze outputs of:
  - `nodes`
  - `net`
  - `dump`
- Measure link performance with `iperf`.
- Define **three flow paths** with minimum intersection.
- Configure **flow entries manually** in OpenFlow switches.
- Explain the behavior and forwarding paths of the defined flows.

📄 Reference: [`پروژه سه-4002.pdf`](./path/to/پروژه%20سه%20-%204002.pdf)

---

## 🚀 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ARSH2001/Computer-Networks.git
2. Install necessary tools:
   - Mininet
   - Wireshark
3. Navigate into project folders and follow the instructions or provided codes for simulation.

