#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from funcs import ocr
from funcs import ocr_frame
from funcs import ocr_text_detect

__credits__ = ["Adrian Rosebrock"]


if __name__ == "__main__":
    ocr.img_to_text(img_path="data/test-1.png")
    ocr.img_to_text(img_path="data/test-2.png", process="blur")

    pages = ocr.pdf_to_jpg(pdf_name="test-5.pdf", pdf_path="data/")
    ocr.img_to_text(img_path="data/{}".format(pages[0]), process="blur")
