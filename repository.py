from pathlib import Path
import json
import csv
from typing import List, Optional
from models import Lead


class LeadRepository:
    """Classe para gerenciar a persistência de leads"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(__file__).resolve().parent / data_dir
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"
    
    def _load(self) -> List[dict]:
        """Carrega os leads do arquivo JSON"""
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    
    def _save(self, leads: List[dict]) -> None:
        """Salva os leads no arquivo JSON"""
        self.db_path.write_text(
            json.dumps(leads, ensure_ascii=False, indent=2), 
            encoding="utf-8"
        )
    
    def create(self, lead: Lead) -> None:
        """Adiciona um novo lead ao repositório"""
        leads = self._load()
        leads.append(lead.to_dict())
        self._save(leads)
    
    def read_all(self) -> List[Lead]:
        """Retorna todos os leads como objetos Lead"""
        data = self._load()
        return [Lead.from_dict(item) for item in data]
    
    def search(self, query: str) -> List[tuple[int, Lead]]:
        """Busca leads por nome, empresa ou email"""
        leads = self.read_all()
        results = []
        query_lower = query.lower()
        
        for index, lead in enumerate(leads):
            search_text = f"{lead.name} {lead.company} {lead.email}".lower()
            if query_lower in search_text:
                results.append((index, lead))
        
        return results
    
    def export_to_csv(self, path: Optional[str] = None) -> Optional[Path]:
        """Exporta os leads para um arquivo CSV"""
        csv_path = Path(path) if path else (self.data_dir / "leads.csv")
        leads_data = self._load()
        
        try:
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                if leads_data:
                    fieldnames = ["name", "company", "email", "stage", "created"]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in leads_data:
                        writer.writerow(row)
            return csv_path
        except PermissionError:
            return None
    
    def update(self, index: int, lead: Lead) -> bool:
        """Atualiza um lead específico"""
        leads = self._load()
        if 0 <= index < len(leads):
            leads[index] = lead.to_dict()
            self._save(leads)
            return True
        return False
    
    def delete(self, index: int) -> bool:
        """Remove um lead específico"""
        leads = self._load()
        if 0 <= index < len(leads):
            leads.pop(index)
            self._save(leads)
            return True
        return False
    
    def count(self) -> int:
        """Retorna o número total de leads"""
        return len(self._load())
