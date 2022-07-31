from prometheus_client import make_wsgi_app, Counter
from wsgiref.simple_server import make_server
import http.server

HIT_COUNT = Counter("hit_count", "total app http request count", ["app_name", "endpoint"])
metrics_app = make_wsgi_app()

def my_app(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        return metrics_app(environ, start_fn)
    HIT_COUNT.labels("prom_python_app",environ['PATH_INFO']).inc()
    start_fn('200 OK', [])
    with open('index.html') as f:
      content = f.read()
    return [bytes(content, "utf-8")]

if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8080, my_app)
    httpd.serve_forever()
