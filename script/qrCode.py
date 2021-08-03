import os
import shutil
import time

import qrcode
import requests
from lxml import etree
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from selenium import webdriver

from Utils.MyUtils import mkdir

base_url = 'http://zjls.spj.gxls.gov.cn:23002/html/notify/work.html?type=3&code='
qrCodeBaseUrl = 'http://zjls.spj.gxls.gov.cn:23002/html/notify/'

dept_list = ['11450721008116032D', '114507210081160408', '11450721MB1558380Y', '11450721008115451U',
             '11450721MB1504681F',
             '114507210081152081', '11450721008115128D', '11450721MB1987329Y', '11450721008115195B',
             'TE4507211000000006',
             'TE4507211000000003', '11450721MB164908XR', '12450700499743101K', '11450721348531435D',
             '11450721008115363D',
             '114507210081152599', '11450721MB1765785C', '11450721355887368D', '114507210081154949',
             '11450721667015665C',
             '114507210081153718', '1145072100811503XR', '11450721MB15260202', '11450721MA15329226',
             '11450721MB15580811',
             '12450000499738185G', '11450721008115339W', '13450721008115267X', '114507210081150992',
             '114507210081168846',
             '914507212012007000', 'TE4507211000000001', '114507217399610370', '11450721MB1852037T',
             '12450721008115443X']


def getHtmlBychromium(targetUrl):
    # 谷歌浏览器插件
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    chromeBrower = webdriver.Chrome(options=option)
    chromeBrower.get(targetUrl)
    time.sleep(2)
    page_source = chromeBrower.page_source
    html = etree.HTML(page_source)
    deptName = \
        html.xpath("/html/body/div[@class='body-work']/div[@class='work-header']/div[@class='work-title']/text()")[0]

    hrefs = html.xpath(
        "/html/body/div[@class='body-work']/div[@class='main-work']/div[@class='work-content']/div[@class='work-con-row']/ul[@class='work-row-con']/li/a/@href")
    hrefs_name = html.xpath(
        "/html/body/div[@class='body-work']/div[@class='main-work']/div[@class='work-content']/div[@class='work-con-row']/ul[@class='work-row-con']/li/a/text()")
    print(hrefs_name)
    chromeBrower.close()
    return deptName, hrefs, hrefs_name


def getDeptGuidanceHref():
    for deptCode in dept_list:
        deptName, hrefs, hrefs_name = getHtmlBychromium(base_url + deptCode)
        print('开始生成-', deptName, '-部门事项二维码')
        for href, href_name in zip(hrefs, hrefs_name):
            temp_img = generatorURLqrCode(qrCodeBaseUrl + href)

            if os.path.exists("D:/kpy/code/lingshan/svn/code/qrCode/" + deptName + "/"):
                pass
            else:
                os.makedirs("D:/kpy/code/lingshan/svn/code/qrCode/" + deptName + "/")
            temp_img.save("D:/kpy/code/lingshan/svn/code/qrCode/" + deptName + "/" + href_name + ".png")
    return None


def generatorURLqrCode(target_url):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=3, )
    qr.add_data(target_url)
    qr.make(fit=True)
    # module_drawer=SquareModuleDrawer() default ,RoundedModuleDrawer(),GappedSquareModuleDrawer(),CircleModuleDrawer(),
    # module_drawer=VerticalBarsDrawer(),HorizontalBarsDrawer()
    # color_mask=SolidFillColorMask(),RadialGradiantColorMask(),SquareGradiantColorMask(),HorizontalGradiantcolorMask()
    # color_mask=VerticalGradiantColorMask(),ImageColorMask()
    return qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage,
                         module_drawer=GappedSquareModuleDrawer(),
                         color_mask=SolidFillColorMask())


if __name__ == '__main__':
    url = 'http://zjls.spj.gxls.gov.cn:23002/html/notify/window_notify.html?deptCode=114507210081152081&ywcode' \
          '=114507210081152081400201420400102 '

    img = generatorURLqrCode(base_url)
    img.save('D:/kpy/code/lingshan/server/nginx/test.png')

    print(getDeptGuidanceHref())
