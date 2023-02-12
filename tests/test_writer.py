from tussik.zpl import ZplWriter


class TestWriter:
    def test_basic(self) -> None:
        zpl = ZplWriter()
        zpl.font(8)
        zpl.text('Message', 30, 50)
        assert zpl.saveas("basic.pdf")
