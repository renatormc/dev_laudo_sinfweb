from pathlib import Path
import re
from pdfminer.high_level import extract_text
from datetime import datetime


class OdinPdfParser:
    def __init__(self, file_: str|Path) -> None:
        self.file_ = Path(file_)
        self.reg1 = r'REQUISIÇÃO DE PERÍCIA(.+)Histórico(.+)Quesitos vinculados(.+)Equipe Envolvida(.+)Pessoas(.+)Vestígios/Exames(.+)'
        self.text = extract_text(self.file_)
        self.parts_res = re.search(self.reg1, self.text, re.MULTILINE|re.DOTALL)

    def extract_all(self):
        data = {}

        text = self.parts_res.group(1)
        reg = r'SEÇÃO.*- ICLR.*?(\d+/\d+) RG (\d+/\d+).*Ocorrência: (\d+/\d+).*?(\d+/\d+/\d+).*RAI: (\d+).*Unidade Solicitante: (.+?)\s*Autoridade: (.+?)\s*Tipificações.*'
        res = re.search(reg, text, re.MULTILINE|re.DOTALL)
        
        if res:
            
            try:
                parts1 = res.group(1).split("/")
                parts2 = res.group(2).split("/")
                data['pericia'] = {
                    'seq': int(parts1[0]),
                    'rg': int(parts2[0]),
                    'ano': int(parts2[1])
                }
            except:
                data['pericia'] = None
            data['ocorrencia'] = res.group(3)
            data['data_ocorrencia'] =  res.group(4)
            data['rai'] = res.group(5)
            data['unidade_solicitante'] = res.group(6)
            data['autoridade'] = res.group(7)
        
        text = self.parts_res.group(3)
        reg = r'Quesito n.: (\d+).*Data de criação: (\d+/\d+/\d+).*Responsável pelo quesito: (.+?)\s*Unidade de origem: (.+?)\s*Unidade afeta:.*Conteúdo: (.+)'
        res = re.search(reg, text, re.MULTILINE|re.DOTALL)
        quesito = {}
        if res:
            quesito['numero'] = res.group(1)
            data['data_criacao'] =  res.group(2)
            quesito['responsavel'] = res.group(3)
            quesito['unidade_origem'] = res.group(4)
            quesito['conteudo'] = res.group(5)
        data['quesito'] = quesito

        text = self.parts_res.group(5)
        reg = r'(.+) \(.+\)'
        res = re.findall(reg, text)
        if res:
            data['pessoas'] = [p for p in res]

        return data