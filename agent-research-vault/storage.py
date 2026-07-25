import json
from pathlib import Path
from models import ResearchSession

class ResearchStorage:
    def __init__(self):
        self.storage_dir=Path("storage")
        self.storage_dir.mkdir(exist_ok=True)
        self.db_path = self.storage_dir / "research_db.json"

        if not self.db_path.exists():
            with open(self.db_path, "w") as file:
                json.dump([],file,indent=4)

    def load_sessions(self) -> list[ResearchSession]:

        with open(self.db_path, "r") as file:
            data = json.load(file)

        return [ResearchSession.model_validate(session) for session in data]

    def save_session(self, session:ResearchSession) -> None:

        sessions = self.load_sessions()
        sessions.append(session)
        serialized_sessions = [s.model_dump(mode="json") for s in sessions]

        with open(self.db_path, "w") as file:
            json.dump(serialized_sessions, file, indent=4)

    def find_by_topic(self, topic:str) -> list[ResearchSession]:

        sessions = self.load_sessions()

        return [session for session in sessions if session.topic.lower() == topic.lower()]

    def get_statistics(self) -> dict:

        sessions =self.load_sessions()
        total_sessions = len(sessions)
        total_results = sum(len(session.results) for session in sessions )

        source_counts = {}

        for session in sessions:
            for result in session.results:

                source = result.source

                source_counts[source] = (source_counts.get(source, 0) + 1)

        return {
            "total_sessions": total_sessions,
            "total_results": total_results,
            "source_counts": source_counts
        }
