import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline"))
import playlist_plan

class PlaylistPlanTests(unittest.TestCase):
    def test_video_can_be_in_topic_and_language_playlists(self):
        meta = {"abc": {"title": "Why Do Plants Need Sunlight?", "language": "default", "episode_id": "ep1", "content_type": "short"}}
        rows = playlist_plan.assignments(meta)
        names = {r["playlist"] for r in rows}
        self.assertIn("English", names)
        if playlist_plan.KIDS:
            self.assertIn("Nature & Plants", names)
        else:
            self.assertIn("Needs manual topic review", names)

    def test_unmatched_topic_is_never_guessed(self):
        rows = playlist_plan.assignments({"x": {"title": "Unmapped episode title", "language": "default"}})
        self.assertIn("Needs manual topic review", {r["playlist"] for r in rows})

    def test_no_duplicate_upload_rows_for_same_playlist(self):
        rows = playlist_plan.assignments({"x": {"title": "What Is AI? ChatGPT prompts", "language": "default"}})
        keys = [(r["video_id"], r["playlist"]) for r in rows]
        self.assertEqual(len(keys), len(set(keys)))

    def test_obvious_ai_topics_get_topic_assignments(self):
        if playlist_plan.KIDS:
            self.skipTest("AInation topic taxonomy only")
        cases = {
            "What Is a Neural Network?": "AI Explained",
            "How Voice Assistants Understand You": "AI Tools & Workflows",
            "Why YouTube Knows What You Like": "AI in Everyday Life",
            "What Is Machine Learning?": "AI Explained",
        }
        for title, expected in cases.items():
            with self.subTest(title=title):
                rows = playlist_plan.assignments({"x": {"title": title, "language": "default"}})
                names = {r["playlist"] for r in rows}
                self.assertIn(expected, names)
                self.assertNotIn("Needs manual topic review", names)

if __name__ == "__main__":
    unittest.main()
