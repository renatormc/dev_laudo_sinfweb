from pathlib import Path
from typing import Any, Tuple
from flask_wtf import FlaskForm
from wtforms import Field, StringField, ValidationError
from fastdoc import config

class FormBase(FlaskForm):

    dfile = StringField("Arquivo documento", default=str((config.workdir / "compilado.docx").absolute()))
    
    def get_layout(self) -> list[list[Tuple[Field, int]]]:
        raise NotImplementedError("The WebForm class should implement the method \"get_layout\"!")


    def get_context(self) -> dict[str, Any]:
        context: dict[str, Any] = {}
        for row in self.get_layout():
            for field, _ in row:
                context[field.name] = field.data
        return context

    def validate_dfile(self, field):
        path = Path(self.dfile.data)
        if not path.parent.exists():
            raise ValidationError("Diretório não existente")
        if path.suffix != ".docx":
            raise ValidationError("O arquivo deve possuir extensão docx")
    