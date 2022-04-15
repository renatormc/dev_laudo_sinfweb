from pathlib import Path
from typing import Any, Callable, Optional, Tuple
from flask_wtf import FlaskForm
from wtforms import Field, StringField, ValidationError
from fastdoc import config
from fastdoc.custom_types import ModelInfo
from rlibs.report_writer.custom_types import InitialData
import importlib


class FormBase(FlaskForm):

    dfile = StringField("Arquivo documento", default=str((config.workdir / "compilado.docx").absolute()))

    def __init__(self, model_info: ModelInfo, *args, **kwargs):
        self.model_info = model_info
        self.initial_data: Optional[InitialData] = None
        super().__init__(*args, **kwargs)
        self.converters: dict[str, Callable] = {field.name: conv for field, conv in self.get_converters()}
    
    def get_layout(self) -> list[list[Tuple[Field, int]]]:
        raise NotImplementedError("The WebForm class should implement the method \"get_layout\"!")


    def get_context(self) -> dict[str, Any]:
        context: dict[str, Any] = {}
        for row in self.get_layout():
            for field, _ in row:
                try:
                    context[field.name] = self.converters[field.name](self, field)
                except KeyError:
                    context[field.name] = field.data
        return context

    def get_converters(self) -> list[Tuple[Field, Callable]]:
        return []

    def validate_dfile(self, field):
        path = Path(self.dfile.data)
        if not path.parent.exists():
            raise ValidationError("Diretório não existente")
        if path.suffix != ".docx":
            raise ValidationError("O arquivo deve possuir extensão docx")
            

    def load_initial_data(self) -> None:
        initial_feeder = importlib.import_module(f"models.{self.model_info.name}.initial_feeder")
        self.initial_data = initial_feeder.get_initial_data(config.workdir)
        if self.initial_data is not None:
            for key, value in self.initial_data.form_data.items():
                getattr(self, key).raw_data = value



    def validate(self, extra_validators=None):
        if extra_validators is None:
            extra_validators = {}
        for name, conv in self.converters.items():
            try:
                extra_validators[name].append(conv)
            except KeyError:
                extra_validators[name] = [conv]
        return super().validate(extra_validators=extra_validators)

    

    

