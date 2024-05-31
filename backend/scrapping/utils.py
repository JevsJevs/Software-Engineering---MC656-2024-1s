def get_event_id(evento: str, sport: str):
    match sport.lower():
                case "judo" | "karate" | "taekwondo":
                    evento = evento.replace('-', '')
    evento_url = (evento.lower()
        .replace(' ', '-').replace('/', '-').replace("'", '-').replace(':', '-')
        .replace(',', '').replace('(', '').replace(')', '')
        .replace('+', 'over-').replace('é', 'e'))
    return evento_url