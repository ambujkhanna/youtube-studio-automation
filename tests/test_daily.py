import json, sys, tempfile, unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline"))
import daily


class DailyEpisodeSelectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.episode_dir = self.root / "ep020-sample"
        self.episode_dir.mkdir()
        (self.episode_dir / "episode.json").write_text(
            json.dumps({"id": "ep020", "title": "Sample episode", "status": "ready"}),
            encoding="utf-8",
        )
        self.patch_dir = patch.object(daily, "EPDIR", str(self.root))
        self.patch_dir.start()

    def tearDown(self):
        self.patch_dir.stop()
        self.temp.cleanup()

    def test_forced_episode_id_is_case_insensitive(self):
        selected = daily.pick({"episodes": {}}, "EP020")
        self.assertEqual(selected["id"], "ep020")
        self.assertEqual(selected["title"], "Sample episode")

    def test_unknown_forced_episode_has_actionable_error(self):
        with self.assertRaisesRegex(ValueError, "Available IDs: ep020"):
            daily.pick({"episodes": {}}, "EP999")


if __name__ == "__main__":
    unittest.main()
