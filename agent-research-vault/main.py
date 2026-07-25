import asyncio
from agent import ResearchAgent
from storage import ResearchStorage
from client import APIServiceUnavailableError

def display_menu():
    print("\n" + "-" * 40)
    print("AGENT RESEARCH VAULT")
    print("-" * 40)
    print("1. Research Topic")
    print("2. Show All Research")
    print("3. Search Research By Topic")
    print("4. Analytics")
    print("5. Exit")

def display_session(session):
    print("\n" + "-" * 40)
    print(f"Topic: {session.topic}")
    print(f"Timestamp: {session.timestamp}")
    print("-" * 40)

    for index, result in enumerate(session.results, start=1):
        print(f"\nResult #{index}")
        print(f"Title: {result.title}")
        print(f"Source: {result.source}")
        print(f"URL: {result.url}")

async def research_topic(agent, storage):
    topic = input("\nEnter research topic: ").strip()

    if not topic:
        print("Topic cannot be empty.")
        return

    try:
        print("\nResearching...\n")

        session = await agent.research(topic)
        storage.save_session(session)
        print("Research completed")
        print(f"Stored {len(session.results)} results")

        display_session(session)

    except APIServiceUnavailableError as e:
        print(f"\nError: {e}")

    except Exception as e:
        print(f"\nUnexpected error: {e}")


def show_all_research(storage):
    sessions = storage.load_sessions()

    if not sessions:
        print("\nNo research sessions found.")
        return

    print(f"\nFound {len(sessions)} research sessions")

    for session in sessions:
        display_session(session)


def search_by_topic(storage):
    topic = input("\nEnter topic to search: ").strip()

    sessions = storage.find_by_topic(topic)

    if not sessions:
        print("\nNo matching sessions found.")
        return

    print(f"\nFound {len(sessions)} matching session(s)")

    for session in sessions:
        display_session(session)


def show_analytics(storage):
    stats = storage.get_statistics()

    print("\n" + "-" * 40)
    print("ANALYTICS")
    print("-" * 40)
    print(f"Total Sessions: {stats['total_sessions']}")
    print(f"Total Results: {stats['total_results']}")
    print("\nSources:")
    for source, count in stats["source_counts"].items():
        print(f"  {source}: {count}")


async def main():
    agent = ResearchAgent()
    storage = ResearchStorage()

    while True:
        display_menu()

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            await research_topic(agent, storage)

        elif choice == "2":
            show_all_research(storage)

        elif choice == "3":
            search_by_topic(storage)

        elif choice == "4":
            show_analytics(storage)

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    asyncio.run(main())