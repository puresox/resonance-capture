# resonance-capture
雷索纳斯抓包获取商品信息

由于本人精力有限，并且已经有其他项目进度更快，请移步至[https://github.com/kmou424/resonance-resodata](https://github.com/kmou424/resonance-resodata)，游戏解包数据（包括但不限于商品ID、基础价格等）请移步至[https://github.com/milkory/rsns-data](https://github.com/milkory/rsns-data)。

## 思路
通过中间人拦截代理进行抓包（为了绕过http请求里的数字签名）能获取当前站点卖的所有商品的价格信息和全游戏所有商品卖到该站点的价格信息（不需要你包里有这些商品），所以通过将9个小号放在9个站点，就能抓到游戏里所有的商品价格信息了。**抓包到的商品信息没有商品名，是以商品ID作为唯一标识，所以需要收集商品ID和商品名的对应关系，且每个商品在不同站点拥有不同的ID，请移步至[雷索纳斯解包数据](https://github.com/milkory/rsns-data)。**

## 模拟器设置
MuMu模拟器
- 分辨率：平板版-1280*720（DPI：240）
- 设置代理：设置-网络和互联网-互联网-wlan0-右上角编辑-代理：手动-代理主机名：本机局域网IP-代理端口：8080

## 运行
启动抓包程序，输出商品信息
```python
mitmdump -s ./capture.py
```

启动脚本，9个号轮流登录，账号密码写入配置文件config.toml（未完成）
```python
python ./main.py
```
## 打包
打包命令：`python -m nuitka main.py --standalone --mingw64 --include-data-dir=templ=templ --include-data-files=<source>=<target> --onefile`
https://nuitka.net/doc/user-manual.html#use-case-4-program-distribution