# **Traceroute Tool** 🚀

A simple **Python-based Traceroute tool** that tracks the route packets take to reach a destination. This tool helps identify network hops and latency between them using **ICMP packets**.

## 📌 **Features**

✔ Tracks the path packets take to reach a destination.  
✔ Displays the IP address of each hop.  
✔ Handles unreachable hops gracefully.  
✔ Lightweight and easy to use.

---

## 🛠 **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Traceroute-Tool.git
   cd Traceroute-Tool
   ```
2. **Install Dependencies:**
   ```bash
   pip install scapy
   ```

---

## 🚀 **Usage**

Run the script from the terminal:

```bash
python Traceroute.py <destination>
```

**Example:**

```bash
python Traceroute.py google.com
```

**Output Example:**

```
Tracing route to google.com

1: 192.168.1.1
2: 203.0.113.1
3: 8.8.8.8
Trace complete.
```

---

## 🔧 **How It Works**

1. Sends **ICMP Echo Request** packets with increasing `TTL` values.
2. Each router along the path decrements the TTL and sends a **Time Exceeded** response.
3. The process repeats until the target is reached.

---

## 📌 **Future Enhancements**

🔹 Add **GeoIP Lookup** to show the location of each hop.  
🔹 Implement **multi-threading** for faster results.  
🔹 Create a **GUI version** using Tkinter.

---

## 📜 **License**

This project is licensed under the **MIT License** – feel free to use and modify it.
