
# 5G System Setup with Encoder Integration

This repository presents a setup design for a small-scale project aimed at simplifying the deployment of a complete 5G system. It integrates encoders into the 5G pipeline to evaluate their impact on network performance, resource usage, and packet loss prevention. This setup allows researchers or engineers to better understand how different encoder types and configurations affect radio resources and overall system efficiency.

---

## Project Purpose

The project focuses on showing:
- How encoders can help prevent packet loss in a 5G network
- How various encoders consume system resources
- The impact of encoder parameter variations on radio resource allocation

This setup is particularly useful for small research environments or labs interested in low-cost yet functional 5G testbeds.

---

## System Requirements and Deployment

The system can be deployed either on:
- A **single machine** (for quick testing), or
- **Three separate systems** connected via a network switch (for a clearer understanding of each component)

We use the **OpenAirInterface (OAI)** framework to deploy the 5G system. The Git repository for OAI can be found at:

👉 https://gitlab.eurecom.fr/oai/openairinterface5g

### Operating System Support

- Older versions of OAI run on **Ubuntu 20.04**
- The latest versions also support **Ubuntu 24.04**

---

## Building the System

To build the system, first download the OAI repository from the link above. Once downloaded, navigate to the `cmake_targets` directory and use the following command to build the necessary components:

```bash
./build_oai -I --gNB --nrUE
```

The 5G system consists of three major parts:
1. **Core**
2. **gNB (Next-generation Node B)**
3. **UE (User Equipment)**

---

## Core Network and Encoder Placement

We deployed the **5G Core** using **Docker containers**, making it easier to manage and run. The gNB and UE components are deployed directly on **bare metal** for performance and hardware testing.

The encoder is placed **between the External Data Network (Ext-DN) and the User Plane Function (UPF)**. This placement is strategic and provides a simplified way to analyze how encoders interact with traffic flow and how they affect the user experience under different conditions.

The `oai-cn5g` folder included in this repository contains the Docker-based core setup, including a `docker-compose` file for launching the system.

> 🔐 **Note:** We use a **paid version of the encoder** (Netcode-IMG). You must purchase the required license in order to run the encoder within this system.

---

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


## How to Implement and Run the Complete System

### Running the Core Network

The 5G core is deployed as a Docker container. To start it, navigate to the `oai-cn5g` directory in your repository and run:

```bash
docker-compose up -d
```

This command will launch all necessary core network components in the background.

### Running gNB and UE on Bare Metal

The gNB and UE run directly on hardware (bare metal). After downloading and building the OpenAirInterface repository, navigate to:

```
cmake_targets/ran_build/build/
```

Open two terminal windows (if running on the same PC):

- **Terminal 1:** Run the gNB with the following command:

  ```bash
  sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 5 --rfsim --sa -E
  ```

- **Terminal 2:** Run the UE with this command:

  ```bash
  sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --rfsim --uicc0.imsi 001010000000001 --rfsimulator.serveraddr 127.0.0.1 -E
  ```

---

With these steps completed, your full 5G system with integrated encoder and decoder will be up and running.

## Final Steps: Running Encoder, Decoder, and Transmitting Data

Once your system is fully up and running, with the UE successfully attached to the gNB and recognized by the core, you can begin data transmission.

### Step 1: Confirm UE and gNB Attachment

To verify that the gNB and UE are correctly registered in the core, check the logs of the Access and Mobility Management Function (AMF):

```bash
docker logs oai-amf
```

This log should show details about connected gNBs and UEs.

---

### Step 2: Load the Encoder Image

On both the **core (Ext-DN side)** and the **UE side**, load the encoder Docker image:

```bash
sudo docker load -i encoder.tar
```

This command will load the pre-purchased Netcode-IMG encoder image into Docker.

---

### Step 3: Start Encoder and Decoder Containers

1. **Enter the Ext-DN container:**

   ```bash
   docker exec -it oai-ext-dn bash
   ```

2. **Enter the Encoder container (running separately):**

   ```bash
   docker exec -it hcs-encoder bash
   ```

3. **Run your desired encoder with chosen settings** (details provided with your Netcode-IMG license).

4. **On the UE side**, run the decoder with a matching configuration. This is also based on the purchased image.

---

### Step 4: Send Packets from Ext-DN to UE

We use a PCAP file to simulate packet transmission from the Ext-DN to the UE.

1. **Copy the traffic replay tool and PCAP file into the Ext-DN container:**

   ```bash
   sudo docker cp tcpreplay-4.4.2 oai-ext-dn:/tmp/
   sudo docker cp ENCODER_vid_1080.pcap oai-ext-dn:/tmp/
   ```

2. **Inside the Ext-DN container**, use `tcpreplay` to send the packets:

   ```bash
   cd /tmp/
   ./tcpreplay -i eth0 ENCODER_vid_1080.pcap
   ```

3. **At the UE**, ensure your decoder is running to receive and decode the transmitted data.

---

With this setup, you should now see packets being transmitted from the Ext-DN, encoded, passed through the 5G pipeline, and finally decoded at the UE. This completes a full data flow through a live 5G network integrated with encoder-decoder modules.


---



## Analyzing Radio Resource Usage with FlexRIC

To analyze how different encoder settings affect radio resource usage, we integrate **FlexRIC**, a near real-time RAN Intelligent Controller (RIC). FlexRIC allows monitoring and control of various RAN parameters via xApps.

🔗 **FlexRIC GitLab Repo**: [https://gitlab.eurecom.fr/mosaic5g/flexric](https://gitlab.eurecom.fr/mosaic5g/flexric)  
📺 **FlexRIC Tutorial Webinar**: [FlexRIC xApp Development Tutorial](https://openairinterface.org/flexric-tutorial-xapp-development/)

### Steps to Use FlexRIC:

1. **Install and build FlexRIC** by cloning the repository and navigating to the root directory:

   ```bash
   ./build/examples/ric/nearRT-RIC
   ```

2. **Run the xApp for KPM (Key Performance Metrics) Monitoring**:

   ```bash
   ./build/examples/xApp/c/monitor/xapp_kpm_moni
   ```

   This xApp monitors real-time KPIs related to resource block usage, PRB allocation, throughput, etc. It helps you understand the effect of different encoders and their parameters on RAN resource efficiency.

   > ✅ You can also explore other xApps within the FlexRIC project to analyze different metrics.

---

With this integration, your setup provides full visibility into how the encoder influences the 5G radio layer, from end-to-end packet transmission to resource consumption analytics.
