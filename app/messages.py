def set_message(name, selected_time, message_type):

        start = f"""
Olá {name}! Sou seu monitor da infinity. 
Você agendou o horario de {selected_time}.
"""     
        forms = f"\nSegue o link para avaliação da monitoria: https://forms.gle/PDtXt2a6EcNE6j8f8 (Preencha ao fim)"
        
        selection = None

        match message_type:
            case "replacement":
                selection = "Reposição"
            case "tutoring":    
                selection = "Reforço"
            case "introduction":
                selection = "Introdução"
            case "undeclared": 
                return f"{start} \nGostaria de confirmar sua presença na monitoria. Não consegui visualizar exatamente sobre qual assunto vamos tratar, Você conseguiria me especificar? \n{forms}."

        return f"{start} \nGostaria de confirmar a sua presença na sua aula de {selection}. Qual o assunto especificamente você gostaria de tratar na sua monitoria? \n{forms}."
    