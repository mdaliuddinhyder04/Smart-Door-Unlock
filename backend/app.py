from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import os, json, base64, random, time

# Serve frontend static files from ../frontend
app = Flask(__name__, static_folder="../frontend", static_url_path="/")

# Files (stored in backend folder)
CODE_FILE = "code_data.json"
ALERT_FILE = "alert.json"
LOG_FILE = "access_log.json"
EXPIRY_TIME = 180  # seconds (3 minutes)

# Directory under frontend to save snapshots (so they could also be served as files if desired)
SNAP_DIR = os.path.join(app.static_folder, "snapshots")
os.makedirs(SNAP_DIR, exist_ok=True)

# Keep a pointer to last snapshot filename (optional)
LAST_SNAPSHOT_NAME = None

# ----------------- Utility -----------------
def generate_code():
    return str(random.randint(100000, 999999))

def save_code(code):
    with open(CODE_FILE, "w") as f:
        json.dump({"code": code, "created": time.time()}, f)

def load_code():
    if not os.path.exists(CODE_FILE):
        return None
    with open(CODE_FILE) as f:
        return json.load(f)

def append_log(entry):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.insert(0, entry)  # newest first
    # keep last 100 entries to avoid file growth
    with open(LOG_FILE, "w") as f:
        json.dump(logs[:100], f, indent=2)

# ----------------- Snapshot APIs -----------------
@app.route("/api/visitor_snapshot", methods=["POST"])
def visitor_snapshot():
    global LAST_SNAPSHOT_NAME
    data = request.data
    if not data:
        return jsonify({"saved": False, "error": "no-data"}), 400
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"snapshot_{ts}.jpg"
    path = os.path.join(SNAP_DIR, filename)
    with open(path, "wb") as f:
        f.write(data)
    LAST_SNAPSHOT_NAME = filename
    # also prepare base64 for quick returning if needed
    b64 = base64.b64encode(data).decode()
    return jsonify({"saved": True, "file": filename, "b64": "data:image/jpeg;base64," + b64})

@app.route("/api/get_snapshot", methods=["GET"])
def get_snapshot():
    if not LAST_SNAPSHOT_NAME:
        return jsonify({"img": None})
    path = os.path.join(SNAP_DIR, LAST_SNAPSHOT_NAME)
    if not os.path.exists(path):
        return jsonify({"img": None})
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return jsonify({"img": "data:image/jpeg;base64," + b64, "file": LAST_SNAPSHOT_NAME})

@app.route("/api/clear_snapshot", methods=["POST"])
def clear_snapshot():
    global LAST_SNAPSHOT_NAME
    # do not delete files (keeps history), just forget last pointer
    LAST_SNAPSHOT_NAME = None
    return jsonify({"cleared": True})

# ----------------- Request / Alert APIs -----------------
@app.route("/api/visitor_request", methods=["POST"])
def visitor_request():
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    with open(ALERT_FILE, "w") as f:
        json.dump({"pending": True, "time": now}, f)
    return jsonify({"message": "Owner alerted", "time": now})

@app.route("/api/check_requests", methods=["GET"])
def check_requests():
    if not os.path.exists(ALERT_FILE):
        return jsonify({"pending": False, "time": ""})
    with open(ALERT_FILE) as f:
        return jsonify(json.load(f))

@app.route("/api/clear_requests", methods=["POST"])
def clear_requests():
    if os.path.exists(ALERT_FILE):
        os.remove(ALERT_FILE)
    return jsonify({"cleared": True})

# ----------------- Code APIs -----------------
@app.route("/api/request_code", methods=["POST"])
def request_code():
    code = generate_code()
    save_code(code)
    return jsonify({"message": "Code generated", "code": code})

@app.route("/api/get_code", methods=["GET"])
def get_code():
    data = load_code()
    if not data or time.time() - data["created"] > EXPIRY_TIME:
        return jsonify({"code": None})
    return jsonify({"code": data["code"]})

@app.route("/api/verify_code", methods=["POST"])
def verify_code():
    payload = request.get_json() or {}
    entered = str(payload.get("code", "")).strip()
    saved = load_code()
    # determine status
    if not saved or time.time() - saved["created"] > EXPIRY_TIME:
        status = "expired"
        # log without image (or with current snapshot if exists)
        img_b64 = None
        if LAST_SNAPSHOT_NAME:
            p = os.path.join(SNAP_DIR, LAST_SNAPSHOT_NAME)
            if os.path.exists(p):
                with open(p, "rb") as f:
                    img_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
        append_log({"time": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
                    "result": status, "img": img_b64})
        return jsonify({"result": "expired"})
    # otherwise compare
    if entered == saved["code"]:
        status = "success"
    else:
        status = "fail"
    # get current snapshot base64 if exists
    img_b64 = None
    if LAST_SNAPSHOT_NAME:
        p = os.path.join(SNAP_DIR, LAST_SNAPSHOT_NAME)
        if os.path.exists(p):
            with open(p, "rb") as f:
                img_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    append_log({"time": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
                "result": status, "img": img_b64})
    return jsonify({"result": status})

# ----------------- Logs -----------------
@app.route("/api/get_logs", methods=["GET"])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify([])
    with open(LOG_FILE) as f:
        try:
            logs = json.load(f)
        except:
            logs = []
    return jsonify(logs)

# ----------------- Serve frontend pages -----------------
@app.route("/")
def visitor_page():
    return app.send_static_file("index.html")

@app.route("/owner")
def owner_page():
    return app.send_static_file("owner.html")

@app.route("/<path:p>")
def static_files(p):
    # allow serving static files under frontend
    return send_from_directory(app.static_folder, p)

if __name__ == "__main__":
    app.run(debug=True)
