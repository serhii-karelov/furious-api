import uvicorn

from furious.cli.discover import import_app


def run_app(host, port):
    app = import_app()
    uvicorn.run(app, host=host, port=port)
