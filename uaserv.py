import web

urls = ('/', 'ua')
f =open('uas','w')

app = web.application(urls, globals())
uas = []

class ua:
    def GET(self):
        try:
            u = web.ctx.env['HTTP_USER_AGENT']
            if u not in uas:
                uas.append(u)
                f.write(u)
                f.write("\n")
                f.flush()
                print "write"
            return "Thanks, lol"
        except e:
            print "ono"
            return "plz give user agent, thx"

if __name__ == "__main__":
    app.run()
