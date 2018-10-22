import requests
import pprint
import json

def getSummonerData(region, summonerName, APIKey):
        """소환사의 프로필 정보"""
        URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

# Mastery
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

# Champion
def getChampionRotationsData(region, APIKey):
        """챔피언 로테이션"""
        URL = "https://" + region + ".api.riotgames.com/lol/platform/v3/champion-rotations" + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()       

# League
def getCallengerLeaguesData(region, queue, APIKey):
        """Challeger League의 모든 소환사 데이터, queue: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLES_TT"""
        URL = "https://" + region + ".api.riotgames.com/lol/league/v3/challengerleagues/by-queue/"+ queue + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getLeaguesData(region, leagueId, APIKey):
        """League의 모든 소환사 데이터"""
        URL = "https://" + region + ".api.riotgames.com/lol/league/v3/leagues/" + leagueId + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()  

def getMasterLeaguesData(region, queue, APIKey):
        """Master League의 모든 소환사 데이터, queue: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLES_TT"""
        URL = "https://" + region + ".api.riotgames.com/lol/league/v3/masterleagues/by-queue/"+ queue + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getPositionsData(region, summonerID, APIKey):
        """자유랭, 솔랭 데이터"""
        URL = "https://" + region + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + summonerID + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

# LOL-Status
def getShardData(region, APIKey):
        """Riot Server 상태"""
        URL = "https://" + region + ".api.riotgames.com/lol/status/v3/shard-data?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

# Match
def getMatchesData(region, matchId, APIKey):
        """Match 상세 정보"""
        URL = "https://" + region + ".api.riotgames.com/lol/match/v3/matches/"+ matchId + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getMatchListsData(region, accountId, APIKey):
        """소환사의 Match Lists - Optional: endTime, beginIndex, beginTime, champion, endIndex, queue, season"""
        URL = "https://" + region + ".api.riotgames.com/lol/match/v3/matchlists/by-account/"+ accountId + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def getTimeLineData(region, matchId, APIKey):
        """Match TimeLine"""
        URL = "https://" + region + ".api.riotgames.com/lol/match/v3/timelines/by-match/"+ matchId + "?api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

def main():
        region = (str)(input('Region: '))
        summonerName = (str)(input('Summoner Name: '))

        with open("./DEVELOPMENT_API_KEY.txt", 'r') as fout:
                APIKey = fout.readline()

        summonerDataJSON = getSummonerData(region,summonerName,APIKey)
        summonerID = str(summonerDataJSON['id'])
        jsonData = getTimeLineData(region, '3327578638', APIKey)
        print(json.dumps(jsonData, indent=2))

if __name__ == "__main__":
    main()