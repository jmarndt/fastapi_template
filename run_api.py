import uvicorn
import argparse


RUN_API = "api.main:api"
DEFAULT_DEV_PORT = 5001
DEFAULT_PROD_PORT = 8181
DEFAULT_PROD_HOST = "0.0.0.0"


parser = argparse.ArgumentParser(
    prog = 'run_api.py',
    description = 'Runs the Fast API for different environments',
    epilog=f'If no options provided API will run in development mode on port {DEFAULT_DEV_PORT}'
)
parser.add_argument('--port', help='port number to use', type=int, dest="port")
parser.add_argument('--host', help='host address to use (only used in production mode)', type=str, dest="host")
parser.add_argument('--prod', help='runs api in production mode', action='store_true', dest="production")


def run_dev(use_port):
    if use_port == None:
        use_port = DEFAULT_DEV_PORT
    uvicorn.run(RUN_API, port=use_port, reload=True, log_level="debug")


def run_prod(use_host, use_port):
    if use_port == None:
        use_port = DEFAULT_PROD_PORT
    if use_host == None:
        use_host = DEFAULT_PROD_HOST
    uvicorn.run(RUN_API, host=use_host, port=use_port)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.production:
        run_prod(args.host, args.port)
    else:
        run_dev(args.port)
