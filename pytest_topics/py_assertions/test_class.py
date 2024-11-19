class Testmystuff():
    def test_type(self):
        assert type(1) == int

    def test_strs(self):
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'

    