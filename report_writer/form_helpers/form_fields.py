from wtforms import Field, IntegerField
from wtforms.widgets import TextInput
from datetime import datetime


class SDateTimeField(Field):
    widget = TextInput()

    def __init__(self, *args, format="%d/%m/%Y %H:%M:%S", **kargs):
        super().__init__(*args, **kargs)
        self.format = format

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return self.data.strftime(self.format)
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            self.data = datetime.strptime(valuelist[0], self.format)
        except Exception as e:
            self.data = None
            raise ValueError(
                "O valor deve ser um valor de data/hora válido (ex: 12/12/2019 12:15:13)")


class SDateField(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return self.data.strftime("%d/%m/%Y")
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            self.data = datetime.strptime(valuelist[0], "%d/%m/%Y")
        except Exception as e:
            self.data = None
            raise ValueError(
                "Data inválida")


class SFloat(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data is not None:
            return str(self.data).replace(".", ",")
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            text = valuelist[0].replace(",", ".")
        except IndexError:
            return
        try:
            self.data = float(text)
        except Exception as e:
            # self.data = None
            raise ValueError(
                "Valor inválido")


# class STimeIntervalField(Field):
#     widget = TextInput()

#     def _value(self):
#         if self.raw_data:
#             return self.raw_data[0]
#         elif self.data:
#             return str(self.data)
#         else:
#             return u''

#     def process_formdata(self, valuelist):
#         try:
#             self.data = str2timedelta(valuelist[0])
#         except Exception as e:
#             self.data = None
#             raise ValueError(
#                 'O campo deve conter um valor de tempo (ex: 01:02:13)')


# class FileSizeField(Field):
#     widget = TextInput()

#     def _value(self):
#         if self.raw_data:
#             return self.raw_data[0]
#         elif self.data:
#             return format_size(self.data)
#         else:
#             return u''

#     def process_formdata(self, valuelist):
#         try:
#             self.data = parse_filesize(valuelist[0])
#         except humanfriendly.InvalidSize:
#             self.data = None
#             raise ValueError('Formato inválido.')


class SPositiveInteger(IntegerField):

    def process_formdata(self, valuelist):
        try:
            self.data = int(valuelist[0])
            if self.data < 0:
                raise ValueError("Deve ser um inteiro positivo")
        except Exception as e:
            self.data = None
            raise ValueError("Deve ser um inteiro positivo")


class SIntegerInterval(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return str(self.data[0]) if self.data[0] == self.data[1] else f"{self.data[0]}-{self.data[1]}"
        else:
            return u''

    def process_formdata(self, valuelist):
        if not valuelist:
            return
        value = valuelist[0].replace(" ", "")
        try:
            data = int(value)
            self.data = (data, data)
        except ValueError:
            try:
                parts = value.split("-")
                self.data = int(parts[0]), int(parts[1])
            except (ValueError, IndexError) as e:
                raise ValueError('Valor ou intervalo de valores inválido.')


class SDateInterval(Field):
    widget = TextInput()

    def __init__(self, label='', validators=None, format="%d/%m/%Y", **kwargs):
        super(SDateInterval, self).__init__(label, validators, **kwargs)
        self.format = format

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return self.data[0].strftime(self.format) if self.data[0] == self.data[
                1] else f"{self.data[0].strftime(self.format)}-{self.data[1].strftime(self.format)}"
        else:
            return u''

    def process_formdata(self, valuelist):
        if not valuelist:
            return
        value = valuelist[0].replace(" ", "")
        try:
            data = datetime.strptime(value, self.format)
            self.data = (data, data)
        except ValueError:
            try:
                parts = value.split("-")
                self.data = datetime.strptime(
                    parts[0], self.format), datetime.strptime(parts[1], self.format)
            except (ValueError, IndexError) as e:
                raise ValueError('Data ou intervalo de datas inválido.')
