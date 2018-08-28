import requests

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def main():
    region = (str)(input('Region: '))
    summonerName = (str)(input('Summoner Name: '))

    f = open("./DEVELOPMENT_API_KEY.txt", 'r')
    APIKey = f.readline()
    f.close()

    summonerDataJSON = requestSummonerData(region, summonerName, APIKey)
    ID = str(summonerDataJSON['id'])
    RankedDataJSON = requestRankedData(region, ID, APIKey)

    print (RankedDataJSON[1]['tier'])
    print (RankedDataJSON[1]['rank'])

if __name__ == "__main__":
    main()