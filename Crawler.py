import RiotAPI as api
import json
import csv

def main():
        with open("./DEVELOPMENT_API_KEY.txt", 'r') as fout:
                APIKey = fout.readline()

        challenger_crawl(APIKey)
        #search_summoner(APIKey)

def challenger_crawl(APIKey):
        challengerData = api.getChallengerLeaguesData('kr','RANKED_SOLO_5x5',APIKey)
        masterData = api.getMasterLeaguesData('kr','RANKED_SOLO_5x5',APIKey)

        challengerEntries = challengerData['entries']
        masterEntries = masterData['entries']

        with open('ma_chal.csv', 'w', encoding='utf-8', newline='') as f:
                wr = csv.writer(f)

                for data in challengerEntries:
                        wr.writerow([data['playerOrTeamId'], data['playerOrTeamName']])
                for data in masterEntries:
                        wr.writerow([data['playerOrTeamId'], data['playerOrTeamName']])


def search_summoner(APIKey):
        region = (str)(input('Region: '))
        summonerName = (str)(input('Summoner Name: '))

        summonerDataJSON = api.getSummonerData(region,summonerName,APIKey)
        summonerID = str(summonerDataJSON['id'])
        jsonData = api.getPositionsData(region, summonerID, APIKey)
        print_pretty_json(jsonData)


def print_pretty_json(jsonData):
    print(json.dumps(jsonData, indent=2))

if __name__ == "__main__":
    main()