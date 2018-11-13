import RiotAPI as api
import json
import csv


MATCHLIST_COLLECTION = "matchlist"
MATCH_COLLECTION = "match"
MATCHLIST_PAGE_LIMIT = 60

def main():
        with open("./DEVELOPMENT_API_KEY.txt", 'r') as fout:
                APIKey = fout.readline()
        # CHallenger, Master 아이디 수집
        #challenger_crawl(APIKey)
        # 
        search_summoner(APIKey)
        # Total Game 숫자가 이상함... API가 잘못된건지..
        #crawl_complete_matchlist(1258501, 'kr', APIKey)

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


def crawl_complete_matchlist(summoner_id,  region, APIKey):
        more_matches=True

        ## Start with empty matchlist
        matchlist={"matches": [], "totalGames": 0}
        begin_index=0
        while more_matches:
                new_matchlist = api.getMatchListsToIndex(region, summoner_id, begin_index, begin_index + MATCHLIST_PAGE_LIMIT, APIKey)
                if "matches" in new_matchlist.keys():
                        matchlist["matches"] = matchlist["matches"] + new_matchlist["matches"]
                        matchlist["totalGames"] = matchlist["totalGames"] + new_matchlist["totalGames"]
                        begin_index += MATCHLIST_PAGE_LIMIT
                else:
                        more_matches=False

        #region = region if region else region
        #matchlist["extractions"] = {"region": region}
        #self._store(identifier=summoner_id, entity_type=MATCHLIST_COLLECTION, entity=matchlist, upsert=True)
        #self.summoner_ids_done.append(summoner_id)
        #match_ids = [x['gameId'] for x in matchlist['matches']]
        #self.match_ids.extend(match_ids)
        #return match_ids

def search_summoner(APIKey):
        region = 'kr'#(str)(input('Region: '))
        summonerName = 'timon'#(str)(input('Summoner Name: '))

        summonerDataJSON = api.getSummonerData(region,summonerName,APIKey)
        summonerID = str(summonerDataJSON['id'])
        jsonData = api.getPositionsData(region, summonerID, APIKey)
        print_pretty_json(jsonData)


def print_pretty_json(jsonData):
    print(json.dumps(jsonData, indent=2))

if __name__ == "__main__":
    main()