"""
  Request Handlers

"""
from aiohttp import web, ClientSession
routes = web.RouteTableDef()


@routes.get('/cep/{cep}')
async def find_by_cep(request):
    client = ClientSession()
    cep = request.match_info.get('cep')
    async with client as session:
        async with session.get('https://viacep.com.br/ws/%s/json' % cep) as resp:
            print(resp.status)
            text = await resp.text()
    return web.Response(text=text, content_type='application/json')


@routes.get('/address/{uf}/{city}/{street}')
async def find_by_cep(request):
    client = ClientSession()
    uf = request.match_info.get('uf')
    city = request.match_info.get('city')
    street = request.match_info.get('street')

    async with client as session:
        async with session.get('https://viacep.com.br/ws/%s/%s/%s/json' % (uf, city, street)) as resp:
            print(resp.status)
            text = await resp.text()
    return web.Response(text=text, content_type='application/json')
