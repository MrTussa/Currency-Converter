from sanic.response import HTTPResponse, text, json
from sanic.request import Request
from sanic import Sanic
from sanic_ext import render
from test1 import currencies
from sanic_jinja2 import SanicJinja2 
app = Sanic('app')
app.update_config("config/configer.py")
DBNAME, ADMINS = app.config.CONFIGER.DBNAME, app.config.CONFIGER.ADMINS
temlpates = SanicJinja2(app)
app.static('/static', 'static/')


# @app.route('/', methods=['POST'])
# async def handler(request: Request):
#     print(request.form)
#     curr = await currencies()
#     print(curr)
#     context = {'database': DBNAME, 'admins': ADMINS, 'curr': curr}
#     return temlpates.render("foo.html", request)

@app.route('/', methods=['GET', 'POST'])
async def handler_get(request: Request):
    if request.method == 'POST':
        print("hello")
        print(request.form)
        curr = await currencies()
        print(curr)
        context = {'database': DBNAME, 'admins': ADMINS, 'curr': curr}
        return temlpates.render("foo.html", request)
    curr = await currencies()
    context = {'database': DBNAME, 'admins': ADMINS, 'curr': curr}
    return await render(
        "foo.html", context=context
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
 
 