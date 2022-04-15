from pathlib import Path
from typing import Optional, Union
from rlibs.report_writer.custom_types import InitialData


def get_initial_data(workdir: Union[Path, str]) -> Optional[InitialData]:
    pics_folder = Path(workdir) / "fotos"
    d = InitialData()
    d.form_data = {
        "objects": str(pics_folder.absolute())
    }
    return d