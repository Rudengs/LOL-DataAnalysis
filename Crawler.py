import RiotAPI as api
import json

def main():
        region = (str)(input('Region: '))
        summonerName = (str)(input('Summoner Name: '))

        with open("./DEVELOPMENT_API_KEY.txt", 'r') as fout:
                APIKey = fout.readline()

        summonerDataJSON = api.getSummonerData(region,summonerName,APIKey)
        summonerID = str(summonerDataJSON['id'])
        jsonData = api.getPositionsData(region, summonerID, APIKey)
        print_pretty_json(jsonData)
        

def print_pretty_json(jsonData):
    print(json.dumps(jsonData, indent=2))

if __name__ == "__main__":
    main()