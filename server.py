from aiohttp import web
import argparse
import aiohttp_jinja2
import jinja2
import pathlib
parser = argparse.ArgumentParser(description='Parameter def')
parser.add_argument('--port', default=8080)
args = parser.parse_args()
app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.jinja2')
async def hello(request):
    return {'count': 27}


args = parser.parse_args()
print(routes)
app.add_routes(routes)
app.router.add_static(
    "/", path=str(pathlib.Path(__file__).parent / "templates"), name="static")
web.run_app(app, port=args.port)
