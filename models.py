from datetime import date
from typing import Optional


class Contact:
    """Classe base para contatos - demonstra herança e polimorfismo"""
    
    def __init__(self, name: str, company: str, email: str, created: Optional[str] = None):
        self.name = name
        self.company = company
        self.email = email
        self.created = created or date.today().isoformat()
    
    def to_dict(self) -> dict:
        """Converte o contato para dicionário - método polimórfico"""
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "created": self.created
        }
    
    def get_display_info(self) -> str:
        """Retorna informação formatada - método polimórfico"""
        return f"{self.name} | {self.company} | {self.email}"
    
    def validate(self) -> bool:
        """Valida os dados do contato"""
        return bool(self.name and self.email and "@" in self.email)
    
    def __str__(self) -> str:
        return self.get_display_info()


class Lead(Contact):
    """Classe Lead que herda de Contact - representa um lead no CRM"""
    
    STAGES = ["novo", "contatado", "qualificado", "convertido", "perdido"]
    
    def __init__(self, name: str, company: str, email: str, 
                 stage: str = "novo", created: Optional[str] = None):
        super().__init__(name, company, email, created)
        self.stage = stage if stage in self.STAGES else "novo"
    
    def to_dict(self) -> dict:
        """Override do método to_dict para incluir stage"""
        data = super().to_dict()
        data["stage"] = self.stage
        return data
    
    def get_display_info(self) -> str:
        """Override do método get_display_info para incluir stage"""
        return f"{self.name:<20} | {self.company:<17} | {self.email:<21} | {self.stage}"
    
    def update_stage(self, new_stage: str) -> bool:
        """Atualiza o estágio do lead"""
        if new_stage in self.STAGES:
            self.stage = new_stage
            return True
        return False
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Lead':
        """Cria um Lead a partir de um dicionário"""
        return cls(
            name=data.get("name", ""),
            company=data.get("company", ""),
            email=data.get("email", ""),
            stage=data.get("stage", "novo"),
            created=data.get("created")
        )


class Customer(Contact):
    """Classe Customer que herda de Contact - demonstra polimorfismo"""
    
    def __init__(self, name: str, company: str, email: str, 
                 total_purchases: float = 0.0, created: Optional[str] = None):
        super().__init__(name, company, email, created)
        self.total_purchases = total_purchases
    
    def to_dict(self) -> dict:
        """Override do método to_dict para incluir total_purchases"""
        data = super().to_dict()
        data["total_purchases"] = self.total_purchases
        return data
    
    def get_display_info(self) -> str:
        """Override do método get_display_info para incluir compras"""
        return f"{self.name:<20} | {self.company:<17} | {self.email:<21} | R$ {self.total_purchases:.2f}"
    
    def add_purchase(self, amount: float) -> None:
        """Adiciona uma compra ao total"""
        self.total_purchases += amount
