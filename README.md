# 5G System Setup with Encoder Integration

This repository presents a setup design for a small-scale project aimed at simplifying the deployment of a complete 5G system. It integrates encoders into the 5G pipeline to evaluate their impact on network performance, resource usage, and packet loss prevention. This setup allows researchers or engineers to better understand how different encoder types and configurations affect radio resources and overall system efficiency.

## Project Purpose

The project focuses on showing:
- How encoders can help prevent packet loss in a 5G network
- How various encoders consume system resources
- The impact of encoder parameter variations on radio resource allocation

This setup is particularly useful for small research environments or labs interested in low-cost yet functional 5G testbeds.

## System Requirements and Deployment

The system can be deployed either on:
- A **single machine** (for quick testing), or
- **Three separate systems** connected via a network switch (for a clearer understanding of each component)

We use the **OpenAirInterface (OAI)** framework to deploy the 5G system. The Git repository for OAI can be found at:

👉 https://gitlab.eurecom.fr/oai/openairinterface5g

### Operating System Support

- Older versions of OAI run on **Ubuntu 20.04**
- The latest versions also support **Ubuntu 24.04**

## Building the System

To build the system, first download the OAI repository from the link above. Once downloaded, navigate to the `cmake_targets` directory and use the following command to build the necessary components:

```bash
./build_oai -I --gNB --nrUE

## About 5G Systems

5G is the fifth generation of mobile network technology, offering significantly improved performance over previous generations. It enables ultra-high-speed communication, extremely low latency, and supports a massive number of connected devices. These features make 5G essential for modern applications such as autonomous vehicles, remote surgery, industrial automation, and high-bandwidth streaming.

A typical 5G system is composed of three major components:

- **Core Network (5G CN):** Handles authentication, session management, data routing, and connectivity to external networks. In our project, the core is deployed as a set of Docker containers.
  
- **gNB (Next-Generation NodeB):** Acts as the base station responsible for radio access and connecting UEs to the core network.
  
- **UE (User Equipment):** Represents end-user devices, like phones or embedded sensors, which connect to the gNB to access 5G services.

One key focus of modern 5G research is **optimizing the user plane**, where data traffic flows. Integrating encoders at this layer helps analyze how different encoding schemes affect overall system efficiency, delay, and resource allocation.

In this project, by placing the encoder between the Ext-DN and UPF, we gain control over traffic compression and can assess encoder effects on:
- Bandwidth usage
- Packet loss
- CPU and memory utilization
- Quality of Experience (QoE) for users

This testbed design provides a flexible platform for evaluating encoding strategies within real 5G network components using OpenAirInterface.




