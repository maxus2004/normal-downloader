from flask import Flask, request, send_from_directory
import subprocess
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/download')
def download():
    url = request.args['url'] 
    resolution = request.args['res'] 
    format = request.args['fmt'] 
    id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    if format=="mp4":
        subprocess.run(["yt-dlp", url, "-f", "bestvideo[height<="+resolution+"][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", "-o", "videos/"+id+".mp4"])
        return send_from_directory("videos", id+".mp4", as_attachment=True)
    else:
        subprocess.run(["yt-dlp", url, "-f", "bestvideo[height<="+resolution+"]+bestaudio", "-o", "videos/"+id+".webm"])
        return send_from_directory("videos", id+".webm", as_attachment=True)

if __name__ == '__main__':
   app.run()