import cv2
import numpy as np


def findColor(
    img,
    color,
    options={"region": None},
):
    """模板匹配，返回结果，图片为高*宽

    Args:
        image {Image} 图片
        color {number} | {string} 要寻找的颜色的RGB值。如果是一个整数，则以0xRRGGBB的形式代表RGB值（A通道会被忽略）；如果是字符串，则以"#RRGGBB"代表其RGB值。
        options {Object} 选项包括：
            region {Array} 找图区域。参见findColor函数关于region的说明。

    Returns:
        tuple: 返回坐标或none
    """
    # 1.设置region
    if options["region"]:
        [region_x, region_y, region_width, region_height] = options["region"]
    else:
        region_x = 0
        region_y = 0
        region_height, region_width = img.shape[:2]
    # 2.寻找颜色
    for y in range(region_y, region_y + region_height):
        for x in range(region_x, region_x + region_width):
            if (np.flip(img[y][x]) == np.array(color)).all():
                return (x, y)
    return False


def findColorInRegion(img, color, x=None, y=None, width=None, height=None):
    img_height, img_width = img.shape[:2]
    if x is None:
        x = 0
    if y is None:
        y = 0
    if width is None:
        width = img_width
    if height is None:
        height = img_height
    return findColor(
        img,
        color,
        options={"region": [x, y, width, height]},
    )


def findImage(
    img,
    template,
    options={"threshold": 0.9, "region": None},
):
    """模板匹配，返回结果，图片为高*宽

    Args:
        img {Image} 大图片
        template {Image} 小图片（模板）
        options {Object} 选项包括：
            threshold {number} 图片相似度。取值范围为0~1的浮点数。默认值为0.9。
            region {Array} 找图区域。参见findColor函数关于region的说明。

    Returns:
        tuple: 返回坐标或none
    """
    # 1.设置region
    if options["region"]:
        [region_x, region_y, region_width, region_height] = options["region"]
    else:
        region_x = 0
        region_y = 0
        region_height, region_width = img.shape[:2]
    regionImg = img[
        region_y : region_y + region_height, region_x : region_x + region_width
    ]
    # 2.模板匹配
    res = cv2.matchTemplate(regionImg, template, cv2.TM_CCOEFF_NORMED)
    # 3.获取匹配结果
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
    confidence = maxVal  # 可信度
    if confidence <= options["threshold"]:
        return False
    else:
        # 4.标记匹配结果
        # cv2.imwrite("log/%s.png" % (uuid.uuid1()), imSearch)
        # cv2.rectangle(
        #     imSearch, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (0, 255, 0), 3,
        # )
        # cv2.imshow("res", imSearch)
        # cv2.waitKey(1000)
        # cv2.destroyAllWindows()
        # 5.求点击位置
        deltaX, deltaY = maxLoc
        templ_height, templ_width = template.shape[:2]
        pos = (
            deltaX + region_x + int(templ_width / 2),
            deltaY + region_y + int(templ_height / 2),
        )
        return pos


def findImageInRegion(
    img, template, x=None, y=None, width=None, height=None, threshold=0.9
):
    img_height, img_width = img.shape[:2]
    if x is None:
        x = 0
    if y is None:
        y = 0
    if width is None:
        width = img_width
    if height is None:
        height = img_height
    return findImage(
        img,
        template,
        options={"threshold": threshold, "region": [x, y, width, height]},
    )
