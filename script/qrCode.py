import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import  SolidFillColorMask
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer

base_url = 'http://zjls.spj.gxls.gov.cn:23002/html/notify/choose-service.html'


def generatorURLqrCode(target_url):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=3,)
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
    img.save('test2.png')
