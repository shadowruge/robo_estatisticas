from flask import Flask, render_template
import json
import os
import testes


app = Flask(__name__)

@app.route('/')
def index():
    data_path = os.path.join(app.root_path, 'static', 'data.json')

    with open(data_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Erro na decodificação do JSON: {e}")
            data = []

    formatted_data = format_data(data)

    return render_template('index.html', data=formatted_data)
# Função que estrutura a exibição do dados
def format_data(data):
    formatted_data = []
    for game in data['data']:
        league = game['league']['name']
        local = game['additionalInfo']['venue']
        minute = game['currentTime']['minute']
        second = game['currentTime']['second']
        homeTeam = game['homeTeam']['name']
        homeTeamScore = game['scores']['homeTeamScore']
        awayTeam = game['awayTeam']['name']
        awayTeamScore = game['scores']['awayTeamScore']
        ht_over_0_5 = game['probabilities'].get('HT_over_0_5')
        ht_over_1_5 = game['probabilities'].get('HT_over_1_5')
        ht_under_0_5 = game['probabilities'].get('HT_under_0_5')
        ht_under_1_5 = game['probabilities'].get('HT_under_1_5')
        at_over_0_5 = game['probabilities'].get('AT_over_0_5')
        at_over_1_5 = game['probabilities'].get('AT_over_1_5')
        at_under_0_5 = game['probabilities'].get('AT_under_0_5')
        at_under_1_5 = game['probabilities'].get('AT_under_1_5')
        temperature = game.get('weatherReport', {}).get('temperature', "N/A")
        humidity = game.get('weatherReport', {}).get('humidity', "N/A")
        wind = game.get('weatherReport', {}).get('wind', "N/A")

        formatted_game = f'''
            🤑 Boa probabilidade de ganhos!🚨

            🏆 Campeonato: {league}
            🏟 {local}
            ⏰ {minute}:{second} Tempo decorrido
            🅰 {homeTeam} = {homeTeamScore}
            🅱 {awayTeam} = {awayTeamScore}

            🔢 HT over 0.5: {ht_over_0_5}
            🔢 HT over 1.5: {ht_over_1_5}
            🔢 HT under 0.5: {ht_under_0_5}
            🔢 HT under 1.5: {ht_under_1_5}

            🔢 AT over 0.5: {at_over_0_5}
            🔢 AT over 1.5: {at_over_1_5}
            🔢 AT under 0.5: {at_under_0_5}
            🔢 AT under 1.5: {at_under_1_5}

            🌡 Temperatura: {temperature}
            💧 Humidade: {humidity}
            🌬 Ventos: {wind}
        '''

        formatted_data.append(formatted_game)

    return formatted_data
# Retire quando colocar em produção
if __name__ == '__main__':
    app.run()
# Chama o comando script teste
app.testes()
