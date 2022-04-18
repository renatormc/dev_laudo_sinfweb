from pathlib import Path
from typing import Optional, Union
from rlibs.report_writer.types import InitialData
from fastdoc.data_extractors.odin_pdf_parser import OdinPdfParser


def get_initial_data(workdir: Union[Path, str]) -> Optional[InitialData]:
    pics_folder = Path(workdir) / "fotos"
    d = InitialData()
    d.form_data = {
        "objects": str(pics_folder.absolute())
    }
    path = Path(workdir) / "Requisicao.pdf"
    if path.exists():
        parser = OdinPdfParser(path)
        data = parser.extract_all()
        print(data)
        p = data['pericia']
        d.form_data['pericia'] = f"{p['seq']}/{p['rg']}/{p['ano']}"
        d.form_data['requisitante'] = data['quesito']['unidade_origem']
        d.form_data['procedimento'] = f"RAI {data['rai']}"
        d.form_data['ocorrencia_odin'] = data['ocorrencia']
        d.form_data['data_odin'] = data['data_ocorrencia']
        d.form_data['numero_quesito'] = data['quesito']['numero']
        d.form_data['autoridade'] = data['autoridade']

    return d