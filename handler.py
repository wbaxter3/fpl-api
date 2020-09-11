import json
import requests
import boto3

from dynamodb_json import json_util
#def main(event, context):
def main():


    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
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
    tablename="2019_whole_season_data"
    table = dynamodb.Table(tablename)

    raw_player_data = table.scan()

    player_data = {}
    for player in raw_player_data['Items']:
        player_data['player_name'] = player['player_name'],
        player_data['games_played'] = player['games']
        print(player['player_name'])
    #url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    #r = requests.get(url)
    # json = r.json()
    # for player in json['elements']:
    #     print(player['first_name'] + " " + player['second_name'])
    # body = {
    #     "players":"test",
    #     "input":event
    # }


    response = {
        "statusCode":200,
        "body": json.dumps(dynamodb_json)
    }
    #print(players)
    return response

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
if __name__ == "__main__":
    main()
    #asyncio.run(main(event,context))
    #asyncio.run(main())
