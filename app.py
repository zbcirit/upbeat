from flask import Flask, render_template, request, abort

app = Flask(__name__)
videos = {"1":160, "2":120, "3":140}
@app.route("/")
def index():
    print("hello")
    return render_template("root.html")

@app.route("/<video_id>")
def video_request(video_id):
    if video_id  not in videos:
        abort(404, description = "Video id not found")
    else:
        return {
            "id": video_id,
            "BPM": videos[video_id]
        }