import requests
import json

data_path = 'data.json'

# Leitura do arquivo JSON
with open(data_path, 'r') as file:
    try:
        dic_response = json.load(file)

        for game in dic_response['data']:
            data = game['date']
            weather_report = game.get('weatherReport', {})
            temperature = weather_report.get('temperature', "N/A")
            condition = weather_report.get('condition', "N/A")
            humidity = weather_report.get('humidity', "N/A")
            wind = weather_report.get('wind', "N/A")

            homeTeam = game['homeTeam']['name']
            awayTeam = game['awayTeam']['name']

            league = game['league']['name']
            local = game['additionalInfo']['venue']

            homeTeamScore = game['scores']['homeTeamScore']
            awayTeamScore = game['scores']['awayTeamScore']

            minute = game['currentTime']['minute']
            second = game['currentTime']['second']

            probabilities = game.get('probabilities', {})
            at_over_0_5 = probabilities.get('AT_over_0_5')
            at_over_1_5 = probabilities.get('AT_over_1_5')
            at_under_0_5 = probabilities.get('AT_under_0_5')
            at_under_1_5 = probabilities.get('AT_under_1_5')
            ht_over_0_5 = probabilities.get('HT_over_0_5')
            ht_over_1_5 = probabilities.get('HT_over_1_5')
            ht_under_0_5 = probabilities.get('HT_under_0_5')
            ht_under_1_5 = probabilities.get('HT_under_1_5')
            probabilidade = game['league'].get('predictability')

            if probabilidade == 'high':
                text = f'''
                    {data}
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


    except json.JSONDecodeError as e:
        print(f"Erro na decodificação do JSON: {e}")

