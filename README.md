# resonance-capture
雷索纳斯抓包获取商品信息

通过中间人拦截代理进行抓包（为了绕过http请求里的加密验证参数）能获取当前站点卖的所有商品的价格信息和全游戏所有商品卖到该站点的价格信息（不需要你包里有这些商品），所以通过将9个小号放在9个站点，就能抓到游戏里所有的商品价格信息了。

MuMuX模拟器
分辨率：平板版-1280*720（DPI：240）
设置代理：设置-网络和互联网-互联网-wlan0-右上角编辑-代理：手动-代理主机名：本机局域网IP-代理端口：8080

启动抓包程序，输出商品信息
mitmdump -s ./capture.py

商品id需要和商品名称找到对应关系。
还在写，先上传一版给个思路

启动脚本，9个号轮流登录，账号密码写入配置文件config.toml（未完成）
python ./main.py