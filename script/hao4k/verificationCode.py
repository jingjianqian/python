import ddddocr


class VerificationCodeRecognition:
    def __init__(self) -> None:
        self.VCODE = None

    def recognition(self, png_path):
        ocr = ddddocr.DdddOcr()
        with open(png_path, 'rb') as f:
            image = f.read()
        self.VCODE = ocr.classification(image)


# if __name__ == '__main__':
#     verificationCodeRecognition = VerificationCodeRecognition()
#     print(verificationCodeRecognition.Recognition())
