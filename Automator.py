from time import sleep

import uiautomator2 as u2

from cv.images import findColorInRegion, findImageInRegion


class Automator:
    def __init__(self, devicesName, appName):
        self.devicesName = devicesName
        self.d = u2.connect(devicesName)
        self.sleepTime = 0.5
        self.d.app_start(appName)

    # 获取截图
    def captureScreen(self):
        return self.d.screenshot(format="opencv")

    # 点击
    def click(self, pos):
        self.d.click(pos[0], pos[1])
        sleep(self.sleepTime)

    # 滑动
    def swipe(self, pos1, pos2):
        self.d.swipe(pos1[0], pos1[1], pos2[0], pos2[1])
        sleep(self.sleepTime)

    # 颜色是否存在
    def color_exist(self, color, x, y, width, height):
        pos = findColorInRegion(self.captureScreen(), color, x, y, width, height)
        if pos:
            return True
        else:
            return False

    # 解决意外
    def accidentResolve(self):
        self.click((450, 1590))

    # 点击模板（如果存在）
    def color_click(self, color, x, y, width, height):
        pos = findColorInRegion(self.captureScreen(), color, x, y, width, height)
        if pos:
            self.click(pos)
            return True
        else:
            return False

    # 点击模板直到消失（如果存在）
    def color_clickToAnother(self, color, x, y, width, height):
        pos = findColorInRegion(self.captureScreen(), color, x, y, width, height)
        if not pos:
            return False
        else:
            while pos:
                self.click(pos)
                pos = findColorInRegion(
                    self.captureScreen(), color, x, y, width, height
                )
            return True

    # 模板是否存在
    def templ_exist(self, template, x, y, width, height, threshold=0.9):
        pos = findImageInRegion(
            self.captureScreen(), template, x, y, width, height, threshold
        )
        if pos:
            return True
        else:
            return False

    # 点击模板（如果存在）
    def templ_click(self, template, x, y, width, height, threshold=0.9):
        pos = findImageInRegion(
            self.captureScreen(), template, x, y, width, height, threshold
        )
        if pos:
            self.click(pos)
            return True
        else:
            return False

    # 点击模板直到消失（如果存在）
    def templ_clickToAnother(self, template, x, y, width, height, threshold=0.9):
        pos = findImageInRegion(
            self.captureScreen(), template, x, y, width, height, threshold
        )
        if not pos:
            return False
        else:
            while pos:
                self.click(pos)
                pos = findImageInRegion(
                    self.captureScreen(), template, x, y, width, height, threshold
                )
            return True

    # 等待模板出现，点击模板
    def templ_waitForClick(self, template, x, y, width, height, threshold=0.9):
        pos = findImageInRegion(
            self.captureScreen(), template, x, y, width, height, threshold
        )
        while not pos:
            pos = findImageInRegion(
                self.captureScreen(), template, x, y, width, height, threshold
            )
        self.click(pos)

    # 等待模板出现，点击模板直到消失
    def templ_waitForClickToAnother(self, template, x, y, width, height, threshold=0.9):
        pos = findImageInRegion(
            self.captureScreen(), template, x, y, width, height, threshold
        )
        while not pos:
            pos = findImageInRegion(
                self.captureScreen(), template, x, y, width, height, threshold
            )
        while pos:
            self.click(pos)
            pos = findImageInRegion(
                self.captureScreen(), template, x, y, width, height, threshold
            )

    # def showToast(self, message):
    #     self.d.toast.show(message)
