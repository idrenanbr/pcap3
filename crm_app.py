from models import Lead
from repository import LeadRepository


class CRMApp:
    """Classe principal da aplicação Mini-CRM - demonstra encapsulamento"""
    
    def __init__(self):
        self.repository = LeadRepository()
        self.running = True
    
    def run(self) -> None:
        """Inicia o loop principal da aplicação"""
        print("=" * 60)
        print("Mini-CRM com Orientação a Objetos")
        print("=" * 60)
        
        while self.running:
            self.show_menu()
            option = input("\nEscolha uma opção: ").strip()
            self.handle_option(option)
    
    def show_menu(self) -> None:
        """Exibe o menu principal"""
        print("\n" + "=" * 60)
        print("MENU PRINCIPAL")
        print("=" * 60)
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[3] Buscar Lead")
        print("[4] Exportar para CSV")
        print("[5] Estatísticas")
        print("[0] Sair")
        print("=" * 60)
    
    def handle_option(self, option: str) -> None:
        """Processa a opção escolhida pelo usuário"""
        options = {
            "1": self.add_lead,
            "2": self.list_leads,
            "3": self.search_leads,
            "4": self.export_csv,
            "5": self.show_statistics,
            "0": self.exit_app
        }
        
        action = options.get(option)
        if action:
            action()
        else:
            print("\n❌ Opção inválida! Tente novamente.")
    
    def add_lead(self) -> None:
        """Adiciona um novo lead ao sistema"""
        print("\n" + "-" * 60)
        print("ADICIONAR NOVO LEAD")
        print("-" * 60)
        
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()
        
        lead = Lead(name=name, company=company, email=email)
        
        if not lead.validate():
            print("\n❌ Erro: Nome e e-mail válido são obrigatórios!")
            return
        
        self.repository.create(lead)
        print("\n✅ Lead adicionado com sucesso!")
        print(f"   {lead.get_display_info()}")
    
    def list_leads(self) -> None:
        """Lista todos os leads cadastrados"""
        leads = self.repository.read_all()
        
        print("\n" + "-" * 60)
        print("LISTA DE LEADS")
        print("-" * 60)
        
        if not leads:
            print("Nenhum lead cadastrado ainda.")
            return
        
        print(f"\n{'#':<3} | {'Nome':<20} | {'Empresa':<17} | {'E-mail':<21} | Stage")
        print("-" * 95)
        
        for index, lead in enumerate(leads):
            print(f"{index:02d}  | {lead.get_display_info()}")
        
        print(f"\nTotal: {len(leads)} lead(s)")
    
    def search_leads(self) -> None:
        """Busca leads por nome, empresa ou email"""
        print("\n" + "-" * 60)
        print("BUSCAR LEADS")
        print("-" * 60)
        
        query = input("Digite o termo de busca: ").strip()
        
        if not query:
            print("\n❌ Consulta vazia!")
            return
        
        results = self.repository.search(query)
        
        if not results:
            print(f"\n❌ Nenhum resultado encontrado para '{query}'")
            return
        
        print(f"\n{'#':<3} | {'Nome':<20} | {'Empresa':<17} | {'E-mail':<21} | Stage")
        print("-" * 95)
        
        for index, lead in results:
            print(f"{index:02d}  | {lead.get_display_info()}")
        
        print(f"\nEncontrado(s): {len(results)} lead(s)")
    
    def export_csv(self) -> None:
        """Exporta os leads para arquivo CSV"""
        print("\n" + "-" * 60)
        print("EXPORTAR LEADS PARA CSV")
        print("-" * 60)
        
        path = self.repository.export_to_csv()
        
        if path is None:
            print("\n❌ Erro ao exportar CSV!")
            print("   Verifique se o arquivo não está aberto em outro programa.")
        else:
            print(f"\n✅ Leads exportados com sucesso!")
            print(f"   Arquivo: {path}")
    
    def show_statistics(self) -> None:
        """Exibe estatísticas do sistema"""
        leads = self.repository.read_all()
        
        print("\n" + "-" * 60)
        print("ESTATÍSTICAS DO SISTEMA")
        print("-" * 60)
        
        total = len(leads)
        print(f"\nTotal de leads: {total}")
        
        if total > 0:
            stages = {}
            for lead in leads:
                stages[lead.stage] = stages.get(lead.stage, 0) + 1
            
            print("\nLeads por estágio:")
            for stage, count in sorted(stages.items()):
                percentage = (count / total) * 100
                print(f"  • {stage.capitalize()}: {count} ({percentage:.1f}%)")
    
    def exit_app(self) -> None:
        """Encerra a aplicação"""
        print("\n" + "=" * 60)
        print("Obrigado por usar o Mini-CRM!")
        print("Até logo! 👋")
        print("=" * 60)
        self.running = False
