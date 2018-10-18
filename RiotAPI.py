import requests
import pprint
import json

def getSummonerData(region, summonerName, APIKey):
        """소환사의 프로필 정보"""
        URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getRankedData(region, summonerID, APIKey):
        """자유랭, 솔랭 데이터"""
        URL = "https://" + region + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + summonerID + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getChampionMasteryDatas(region, summonerID, APIKey):
        """챔피언의 숙련도 데이터"""
        URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + summonerID + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getChampionMasteryData(region, summonerID, championId, APIKey):
        """특정 챔피언의 숙련도 데이터"""
        URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + summonerID + "/by-champion/" + championId + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getChampionScoreData(region, summonerID, APIKey):
        """챔피언의 숙련도 총합"""
        URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/score/by-summoner/" + summonerID + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()       

def main():
        region = (str)(input('Region: '))
        summonerName = (str)(input('Summoner Name: '))

        with open("./DEVELOPMENT_API_KEY.txt", 'r') as fout:
                APIKey = fout.readline()

        summonerDataJSON = getSummonerData(region,summonerName,APIKey)
        summonerID = str(summonerDataJSON['id'])
        jsonData = getRankedData(region, summonerID, APIKey)
        print(json.dumps(jsonData, indent=2))

def printRankData():
        region = (str)(input('Region: '))
        summonerName = (str)(input('Summoner Name: '))

        f = open("./DEVELOPMENT_API_KEY.txt", 'r')
        APIKey = f.readline()
        f.close()

        summonerDataJSON = getSummonerData(region, summonerName, APIKey)
        ID = str(summonerDataJSON['id'])
        RankedDataJSON = getRankedData(region, ID, APIKey)

        print (RankedDataJSON[1]['tier'])
        print (RankedDataJSON[1]['rank'])

if __name__ == "__main__":
    main()