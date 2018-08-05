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
    #region = (str)(input('Region: '))
    #summonerName = (str)(input('Summoner Name: '))
    #APIKey = (str)(input('Key: '))
    
    region = (str)('kr')
    summonerName = (str)('루뎅a')

    f = open("./DEVELOPMENT_API_KEY.txt", 'r')
    APIKey = f.readline()
    f.close()

    responseJSON = requestSummonerData(region, summonerName, APIKey)
    ID = responseJSON['id']
    ID = str(ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)

    print (responseJSON2[1]['tier'])
    print (responseJSON2[1]['rank'])

if __name__ == "__main__":
    main()