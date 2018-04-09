#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, abort

# import camera driver
#if os.environ.get('CAMERA'):
#    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
#    from camera import Camera
try:
    from camera_pi import Camera
except Exception as e:
    from flask_app.camera_pi import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)
_routes = []


@app.route('/<path:url>', methods=['GET', 'POST'])
def route(url):
    print(url)
    if url in _routes:
        return render_template('index.html', url=url)
    abort(404)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/<path:url>/video_feed', methods=['GET', 'POST'])
def video_feed(url):
    if url in _routes:
        return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
    abort(404)


def addroute(url):
    _routes.append(url)
