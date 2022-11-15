import uvicorn
import argparse


DEFAULT_DEV_PORT = 5001
DEFAULT_PROD_PORT = 8181


parser = argparse.ArgumentParser(
    prog = 'run_api.py',
    description = 'Runs the Fast API for different environments',
    epilog=f'If no options provided API will run in dev mode on port {DEFAULT_DEV_PORT}'
)
parser.add_argument('-p', '--port', help='api port', type=int, dest="port")
parser.add_argument('--prod', '--production', help='runs api in production mode', action='store_true', dest="production")


def run_dev(use_port):
    if use_port == None:
        use_port = DEFAULT_DEV_PORT
    uvicorn.run("api.main:api", port=use_port, reload=True, log_level="debug")


def run_prod(use_port):
    if use_port == None:
        use_port = DEFAULT_PROD_PORT
    uvicorn.run("api.main:api", port=use_port)


if __name__ == "__main__":
    args = parser.parse_args()

    run_prod(args.port) if args.production else run_dev(args.port)