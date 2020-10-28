import json
import requests
import boto3

import sys
sys.path.append("/opt/python-modules")
import asyncio
import aiohttp
from dynamodb_json import json_util
from understat import Understat




async def main():
#async def main():

    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        data = await understat.get_league_players("epl", 2018, {"team_title": "Manchester United"})

    response = {
    "statusCode":200,
    "players":json.dumps(data)
    }

    return response

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    # if event['year'] == "2014":
    #     tablename = "2014_whole_season_data"
    # elif event['year'] == "2015":
    #     tablename = "2015_whole_season_data"
    # elif event['year'] == "2016":
    #     tablename = "2016_whole_season_data"
    # elif event['year'] == "2017":
    #     tablename = "2017_whole_season_data"
    # elif event['year'] == "2018":
    #     tablename = "2018_whole_season_data"
    # elif event['year'] == "2019":
    #     tablename = "2019_whole_season_data"
    # #tablename="2019_whole_season_data"
    # table = dynamodb.Table(tablename)
    #
    # player_data = table.scan()
    # #dynamodb_json = json_util.dumps(player_data)
    # #print(dynamodb_json)
    #
    # #url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    # #r = requests.get(url)
    # # json = r.json()
    # # for player in json['elements']:
    # #     print(player['first_name'] + " " + player['second_name'])
    # # body = {
    # #     "players":"test",
    # #     "input":event
    # # }
    #
    # players = []
    # for item in player_data['Items']:
    #     player = {}
    #     player['player_name'] = item['player_name']
    #     player['goals_season'] = item['goals_season']
    #     player['assists_season'] = item['assists_season']
    #     player['games'] = item['games']
    #     player['key_passes_Season'] = item['key_passes_Season']
    #     player['npg_season'] = item['npg_season']
    #     player['npxG_season'] = item['npxG_season']
    #     player['position'] = item['position']
    #     player['red_cards'] = item['red_cards']
    #     player['shots_season'] = item['shots_season']
    #     player['team_title'] = item['team_title']
    #     player['time'] = item['time']
    #     player['xA_season'] = item['xA_season']
    #     player['xGBuildup'] = item['xGBuildup']
    #     player['xGChain'] = item['xGChain']
    #     player['xG_season'] = item['xG_season']
    #     player['yellow_cards'] = item['yellow_cards']
    #     players.append(player)
    # data = {"players":players}
    #
    #
    # response = {
    #     "statusCode":200,
    #     "players": players
    # }
    # #print(players)
    # return response

#
# def main(event, context):
#     body = {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "input": event
#     }
#
#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }
#     return response
#async withaiohttp.ClientSession as session:
#     return response
#
#     # Use this code if you don't use the http event with the LAMBDA-PROXY
#     # integration
#     """
#     return {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "event": event
#     }
#     """
# if __name__ == "__main__":
#
#     asyncio.run(main(event,context))
#     #asyncio.run(main())


def handler(event, context):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
