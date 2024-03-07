class Capture:
    def __init__(self):
        pass

    def response(self, flow):
        if (
            flow.request.url == "http://reso-online-ddos.soli-reso.com:9001/api/"
            and "method=station.goods_info" in flow.request.content.decode("utf-8")
        ):
            goods_info = eval(flow.response.content.decode("utf-8"))
            print(goods_info)


addons = [Capture()]
