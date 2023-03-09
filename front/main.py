import asyncio

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(port = 8080)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())