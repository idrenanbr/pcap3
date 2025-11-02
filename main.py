"""
Mini-CRM com Orientação a Objetos
PCP - 2SEM-CP3
Autor: Alexandre Russi

Este sistema demonstra:
- Classes e Objetos
- Atributos e Métodos
- Herança (Contact -> Lead, Customer)
- Polimorfismo (métodos to_dict, get_display_info)
- Encapsulamento
"""

from crm_app import CRMApp


def main():
    """Função principal - ponto de entrada da aplicação"""
    app = CRMApp()
    app.run()


if __name__ == "__main__":
    main()
