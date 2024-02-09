from barcode import Code128
from barcode.writer import ImageWriter

# nao daremos acesso a biblioteca mas sim ao processo como um todo
# se a lib precisar de manutenção, será feita aqui e não no código todo
class BarcodeHandler:
    def create_barcode (self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)

        return path_from_tag
