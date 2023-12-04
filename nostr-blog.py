import aionostr
import asyncio
import os 

private_key = os.environ['NOSTR_KEY']
msg_to_send = 'testing aionostr'
relay_list = ['wss://nostr.mom']
limit = 2
kinds = [1]

# TODO: test markdown file is the markdown-style-guide.md
# post this to test posting to a relay
# test_file = "./src/content/blog/markdown-style-guide.md"

async def read_from_relay(kinds: list, limit: int, relay_list: list):
    events = await aionostr.get_anything({"kinds": kinds, "limit": limit}, relays=relay_list)
    return events

async def write_to_relay(msg: str):
    event_id = await aionostr.add_event(relays=relay_list, kind=20000, content=msg, private_key=private_key)
    return event_id

async def main():
    print("testing Read from Relay")
    events = await read_from_relay(kinds, limit, relay_list)
    for event in events:
        print(event.to_json_object())
        print("\n")
    print("testing Write to Relay")
    event_id = await write_to_relay(msg_to_send)
    print(f'event id: {event_id}')


if __name__ == "__main__":
    asyncio.run(main())