# Custom Lightweight Multi-Threaded HTTP/1.1 Web Server from Scratch

A high-performance, modular, concurrent HTTP/1.1 web server built entirely from scratch in Python using low-level socket APIs (`socket`) and POSIX-style threading (`threading`). This project avoids high-level web frameworks (like Django, Flask, or FastAPI) to implement core network protocols, stream buffering, request-response parsing pipelines, and critical security mechanisms manually.

---

## 🏗️ Architectural Overview & System Flow

The architecture follows a strictly decoupled **Modular Framework Design** to mimic modern enterprise monoliths. The data pipeline handles execution sequentially through dedicated abstractions:


<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/31af4bf6-ae80-4aa0-8558-856a32bc08b2" />


# 📂 Project Structure
```text
├── server.py             
├── request_parser.py    
├── response_builder.py   
├── router.py           
├── handlers.py     
├── mime_types.py        
├── utils.py              
├── .gitignore            
└── www/                  

```

# 📈 Next Milestones (C++ Engine Migration)
- Transitioning from Python strings to custom fixed-size memory Char Buffers to explore low-overhead parsing
- Eliminating Python's Global Interpreter Lock (GIL) by utilizing low-level POSIX threads (pthread) or std::jthread
- Handling direct raw OS primitives(sys/socket.h) and structural memory pointer management without garbage collection overhead.
