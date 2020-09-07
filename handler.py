import json
from fpl import FPL
import aiohttp
import asyncio

# async def main(event, context):
async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    players = await fpl.get_players(return_json=True)
    await session.close()


    body = {
        "players":players
    }


    response = {
        "statusCode":200,
        "body":players
    }
    print(players)
    return response


# def hello(event, context):
#     body = {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "input": event
#     }
#
#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }
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

    # asyncio.run(main(event,context))
    asyncio.run(main())
