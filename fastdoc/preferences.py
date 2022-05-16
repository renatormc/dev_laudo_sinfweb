from typing import TypedDict, Union
from marshmallow import Schema, fields, EXCLUDE
from fastdoc import config
import json
import subprocess
import os


class FastdocPreferences(TypedDict):
    doc_in_workdir: bool
    doc_default_name: str


class PreferencesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    doc_in_workdir = fields.Bool(missing=False)
    doc_default_name = fields.Str(missing="compilado.docx")


class PreferencesManager:
    _instance: Union['PreferencesManager', None] = None

    def __init__(self) -> None:
        self._preferences: FastdocPreferences | None = None

    @classmethod
    def instance(cls) -> 'PreferencesManager':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def preferences(self) -> FastdocPreferences:
        if self._preferences is None:
            raise Exception("Preferences was not loaded")
        return self._preferences

    def save_preferences(self) -> None:
        with config.PREFERENCES_PATH.open("w") as f:
            f.write(json.dumps(self._preferences, ensure_ascii=False, indent=4))

    def load_preferences(self) -> FastdocPreferences:
        schema = PreferencesSchema()
        try:
            with config.PREFERENCES_PATH.open("r") as f:
                raw_data = json.load(f)
            data: FastdocPreferences = schema.load(raw_data)
            self._preferences = data
        except FileNotFoundError:
            self._preferences = schema.load({})
        return self.preferences

    def edit_preferences(self) -> None:
        self.load_preferences()
        self.save_preferences()
        items = ['notepad++', 'notepad'] if os.name == 'nt' else ['gedit', 'kate', 'xed']
        for item in items:
            try:
                subprocess.run([item, str(config.PREFERENCES_PATH)])
                self.load_preferences()
                break
            except FileNotFoundError:
                pass
